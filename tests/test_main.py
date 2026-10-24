from unittest.mock import patch

import app.main


def test_run_prints_result_from_add(capsys):
    with patch("app.main.add", return_value=99):
        app.main.run()

    assert "2 + 3 = 99" in capsys.readouterr().out
