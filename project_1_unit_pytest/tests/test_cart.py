import pytest

from src.cart import Cart


@pytest.fixture
def cart():
    c = Cart()
    c.add_price(100)
    c.add_price(50)
    return c


def test_total(cart):
    assert cart.total() == 150


@pytest.mark.parametrize(
    "percent,expected",
    [
        (0, 150),
        (10, 135),
        (100, 0),
    ],
)
def test_apply_discount(cart, percent, expected):
    assert cart.apply_discount(percent) == expected


def test_add_negative_price_raises_error():
    c = Cart()
    with pytest.raises(ValueError, match="negative"):
        c.add_price(-1)

