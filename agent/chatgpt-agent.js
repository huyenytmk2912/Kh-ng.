import { chromium } from 'playwright';

const MESSAGE = process.env.MESSAGE || '';
const URL = process.env.CHATGPT_URL || 'https://chatgpt.com/';
const PROFILE = process.env.CHATGPT_PROFILE || './chatgpt-profile';
const COUNT = Math.max(1, Number(process.env.COUNT || 1));
const DELAY = Math.max(1, Number(process.env.DELAY || 10)) * 1000;

async function visible(locator) { return await locator.count() && await locator.first().isVisible().catch(() => false); }
async function composer(page) {
  for (const l of [page.locator('textarea').first(), page.locator('[contenteditable="true"]').first(), page.getByRole('textbox').first()]) if (await visible(l)) return l;
  return null;
}
async function sendButton(page) {
  for (const l of [page.getByRole('button', {name:/send|gửi/i}).last(), page.locator('button[data-testid*="send"]').last()]) if (await visible(l)) return l;
  return null;
}
const context = await chromium.launchPersistentContext(PROFILE, { headless: true });
const page = context.pages()[0] || await context.newPage();
await page.goto(URL, {waitUntil:'domcontentloaded'});
console.log('Log in once using this persistent profile before unattended use.');
for (let i=0;i<COUNT;i++) {
  const box = await composer(page); if (!box) throw new Error('Message composer not found');
  await box.click(); await page.keyboard.insertText(MESSAGE);
  const send = await sendButton(page);
  if (send) await send.click(); else await page.keyboard.press('Enter');
  console.log(`Sent ${i+1}/${COUNT}`);
  if (i+1<COUNT) await page.waitForTimeout(DELAY);
}
await context.close();
