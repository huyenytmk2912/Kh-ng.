import { chromium } from 'playwright';
import fs from 'node:fs';
import path from 'node:path';

const MESSAGE = process.env.MESSAGE || '';
const URL = process.env.CHATGPT_URL || 'https://chatgpt.com/';
const PROFILE = process.env.CHATGPT_PROFILE || './chatgpt-profile';
const COUNT = Math.max(1, Number(process.env.COUNT || 1));
const DELAY = Math.max(1, Number(process.env.DELAY || 10)) * 1000;
const RESPONSE_TIMEOUT = Math.max(10, Number(process.env.RESPONSE_TIMEOUT || 180)) * 1000;
const LOGIN_TIMEOUT = Math.max(30, Number(process.env.LOGIN_TIMEOUT || 300)) * 1000;
const HEADLESS = !/^(0|false|no)$/i.test(process.env.HEADLESS || 'true');
const SHOT_DIR = process.env.SCREENSHOT_DIR || './web/screenshots';

if (!MESSAGE.trim()) throw new Error('MESSAGE is required');
fs.mkdirSync(PROFILE, { recursive: true });
fs.mkdirSync(SHOT_DIR, { recursive: true });

async function visible(locator) {
  return (await locator.count()) > 0 && await locator.first().isVisible().catch(() => false);
}

async function composer(page) {
  const candidates = [
    page.locator('textarea').first(),
    page.locator('[contenteditable="true"]').first(),
    page.getByRole('textbox').first(),
  ];
  for (const locator of candidates) if (await visible(locator)) return locator;
  return null;
}

async function sendButton(page) {
  const candidates = [
    page.getByRole('button', { name: /send|gửi/i }).last(),
    page.locator('button[data-testid*="send"]').last(),
    page.locator('button[aria-label*="Send"]').last(),
  ];
  for (const locator of candidates) if (await visible(locator)) return locator;
  return null;
}

async function screenshot(page, name = 'latest') {
  await page.screenshot({ path: path.join(SHOT_DIR, `${name}.png`), fullPage: false }).catch(() => {});
}

async function waitForComposer(page, timeout = LOGIN_TIMEOUT) {
  const deadline = Date.now() + timeout;
  while (Date.now() < deadline) {
    const box = await composer(page);
    if (box) return box;
    await page.waitForTimeout(1000);
  }
  return null;
}

async function waitForResponse(page, beforeText, timeout = RESPONSE_TIMEOUT) {
  const deadline = Date.now() + timeout;
  while (Date.now() < deadline) {
    const box = await composer(page);
    const bodyText = await page.locator('body').innerText().catch(() => '');
    const hasBusy = await page.locator('[aria-label*="Stop"], button:has-text("Stop generating")').count().catch(() => 0);
    if (box && !hasBusy && bodyText !== beforeText) return true;
    await page.waitForTimeout(1000);
  }
  return false;
}

const context = await chromium.launchPersistentContext(PROFILE, {
  headless: HEADLESS,
  viewport: { width: 1440, height: 1000 },
});

try {
  const page = context.pages()[0] || await context.newPage();
  page.setDefaultTimeout(15000);
  await page.goto(URL, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await screenshot(page, 'startup');

  let box = await waitForComposer(page, 10000);
  if (!box) {
    console.log('ChatGPT session is not ready. Complete login in the persistent browser profile, then the agent will continue.');
    if (HEADLESS) console.log('HEADLESS=true: use a pre-authenticated profile or run once with HEADLESS=false.');
    box = await waitForComposer(page, LOGIN_TIMEOUT);
  }
  if (!box) {
    await screenshot(page, 'login-timeout');
    throw new Error('ChatGPT composer not found; login/session may be required');
  }

  for (let i = 0; i < COUNT; i++) {
    box = await composer(page);
    if (!box) throw new Error('Message composer disappeared');

    await box.click();
    await box.fill('').catch(() => {});
    await page.keyboard.insertText(MESSAGE);
    await screenshot(page, `before-send-${i + 1}`);

    const beforeText = await page.locator('body').innerText().catch(() => '');
    const send = await sendButton(page);
    if (send) await send.click();
    else await page.keyboard.press('Enter');

    const completed = await waitForResponse(page, beforeText);
    await screenshot(page, `after-send-${i + 1}`);
    if (!completed) throw new Error(`Response timeout on message ${i + 1}/${COUNT}`);

    console.log(`Completed ${i + 1}/${COUNT}`);
    if (i + 1 < COUNT) await page.waitForTimeout(DELAY);
  }
} finally {
  await context.close();
}
