import log_analyzer


def test_main():
    assert log_analyzer.main("app.log","2023-03-01 09:05:30","01-03-2023 08:20:05")
