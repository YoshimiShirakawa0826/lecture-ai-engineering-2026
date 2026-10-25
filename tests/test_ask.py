from types import SimpleNamespace
from unittest.mock import patch

from app.ask import ask


def test_ask_prints_input_and_output_token_counts(capsys):
    response = SimpleNamespace(
        usage_metadata=SimpleNamespace(
            prompt_token_count=23,
            candidates_token_count=7,
        ),
        text="answer",
    )
    client = SimpleNamespace(
        models=SimpleNamespace(generate_content=lambda **kwargs: response)
    )

    with (
        patch("app.ask.genai.Client", return_value=client),
        patch("app.ask.get_api_key", return_value="test-key"),
    ):
        assert ask("question") == "answer"

    assert capsys.readouterr().out == "[トークン数] 入力: 23, 出力: 7\n"
