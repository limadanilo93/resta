"""Concrete menu item representing a food plate."""

from Modelos.Menus.it_me import ItMe


class Plate(ItMe):
    """A food plate with a description.

    Applies a 10 % discount when :meth:`apply_disc` is called.

    Attributes:
        _desc: Allergen or ingredient description for the plate.
    """

    def __init__(self, name: str, price: float, desc: str):
        """Initializes a plate.

        Args:
            name: Display name of the plate.
            price: Price in BRL before any discount.
            desc: Description shown on the menu (ingredients, allergens, etc.).
        """
        super().__init__(name, price)
        self._desc = desc

    def apply_disc(self):
        """Applies a 10 % discount to the plate price."""
        self._price -= self._price * 0.1
