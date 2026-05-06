"""Concrete menu item representing a beverage."""

from Modelos.Menus.it_me import ItMe


class Bev(ItMe):
    """A beverage with a volume size.

    Applies an 8 % discount when :meth:`apply_disc` is called.

    Attributes:
        _size: Volume of the beverage in millilitres.
    """

    def __init__(self, name: str, price: float, size: float):
        """Initializes a beverage.

        Args:
            name: Display name of the beverage.
            price: Price in BRL before any discount.
            size: Volume in millilitres (e.g. 500 for 500 ml).
        """
        super().__init__(name, price)
        self._size = size

    def apply_disc(self):
        """Applies an 8 % discount to the beverage price."""
        self._price -= self._price * 0.08
