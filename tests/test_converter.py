from unittest.mock import Mock

import pytest

from app.converter import CurrencyConverter


def test_convert_uses_provider_rate():
    provider = Mock(return_value=1.1)
    converter = CurrencyConverter(provider)

    assert converter.convert(10, "EUR", "USD") == 11.0
    provider.assert_called_once_with("EUR", "USD")


def test_same_currency_skips_provider():
    provider = Mock()

    assert CurrencyConverter(provider).convert(5, "USD", "USD") == 5
    provider.assert_not_called()


def test_negative_amount_rejected():
    converter = CurrencyConverter(Mock())

    with pytest.raises(ValueError):
        converter.convert(-1, "EUR", "USD")


def test_provider_failure_propagates():
    provider = Mock(side_effect=ConnectionError("rate service timeout"))

    with pytest.raises(ConnectionError):
        CurrencyConverter(provider).convert(1, "EUR", "USD")
