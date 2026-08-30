from scripts.khuong_doctor import command_version


def test_doctor_can_query_missing_or_available_command():
    result = command_version("command-that-should-not-exist-khuong", ["--version"])
    assert result is None
