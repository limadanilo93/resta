"""Abstract base class for all menu items."""

from abc import ABC, abstractmethod


class ItMe(ABC):
    """Represents a generic menu item.

    All concrete menu items (plates, beverages, etc.) must inherit from
    this class and implement `apply_disc`.

    Attributes:
        _name: Display name of the item.
        _price: Current price of the item in BRL.
    """

    def __init__(self, name: str, price: float):
        """Initializes a menu item with a name and price.

        Args:
            name: Display name of the item.
            price: Price of the item in BRL.
        """
        self._name = name
        self._price = price

    def __str__(self) -> str:
        return self._name

    @classmethod
    def from_dict(cls, data: dict) -> 'ItMe':
        """Creates the appropriate item subclass from a JSON-sourced dict.

        Inspects the dict keys to decide the item type:
        - ``description`` key → returns a :class:`Plate`.
        - ``size`` key → returns a :class:`Bev`.

        Args:
            data: Dict with keys ``Item``, ``price``, and either
                ``description`` (plate) or ``size`` (beverage).

        Returns:
            A concrete :class:`ItMe` subclass instance.

        Raises:
            ValueError: If the dict does not contain a recognised type key.

        Example::

            item = ItMe.from_dict({
                "Item": "Pãozinho",
                "price": 3.0,
                "description": "Pão baiano"
            })
        """
        from Modelos.Menus.plate import Plate
        from Modelos.Menus.bev import Bev
        if 'description' in data:
            return Plate(data['Item'], data['price'], data['description'])
        elif 'size' in data:
            return Bev(data['Item'], data['price'], data['size'])
        raise ValueError(f"Cannot determine item type from keys: {list(data.keys())}")

    @abstractmethod
    def apply_disc(self):
        """Applies the item-specific discount to ``_price`` in place."""
        pass
