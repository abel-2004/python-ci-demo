from typing import Callable

RateProvider = Callable[[str, str], float]


class CurrencyConverter:
    def __init__(self, rate_provider: RateProvider) -> None:
        self._rate_provider = rate_provider

    def convert(self, amount: float, src: str, dst: str) -> float:
        if amount < 0:
            raise ValueError("amount must be non-negative")
        if src == dst:
            return amount
        rate = self._rate_provider(src, dst)
        return round(amount * rate, 2)
