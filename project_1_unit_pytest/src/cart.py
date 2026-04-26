class Cart:
    def __init__(self) -> None:
        self._items: list[float] = []

    def add_price(self, price: float) -> None:
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self._items.append(price)

    def total(self) -> float:
        return sum(self._items)

    def apply_discount(self, percent: float) -> float:
        if percent < 0 or percent > 100:
            raise ValueError("Discount must be between 0 and 100.")
        discount_factor = (100 - percent) / 100
        return self.total() * discount_factor

