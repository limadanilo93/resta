"""Restaurant model with menu management and evaluation tracking."""

from Modelos.eval import Eval
from Modelos.Menus.it_me import ItMe


class Restaurante:
    """Represents a restaurant with its menu and evaluations.

    Maintains a class-level registry of all created restaurants so they
    can be listed together via :meth:`list_rest`.

    Attributes:
        restaurantes: Class-level list containing every
            :class:`Restaurante` instance created so far.
    """

    restaurantes: list = []

    def __init__(self, name: str, category: str):
        """Initializes a restaurant and registers it in the class registry.

        Args:
            name: Restaurant name (stored as title-case).
            category: Cuisine category (stored as upper-case).
        """
        self._name = name.title()
        self._category = category.upper()
        self._status = False
        self._eval: list[Eval] = []
        self._menu: list[ItMe] = []
        Restaurante.restaurantes.append(self)

    def __str__(self) -> str:
        return f'{self._name} | {self._category}'

    @classmethod
    def list_rest(cls):
        """Prints a formatted table of all registered restaurants."""
        print(f'{"RESTAURANTE".ljust(25)} | {"CATEGORIA".ljust(25)} | {"STATUS".ljust(15)} | {"AVALIAÇÃO".ljust(15)}')
        for rest in cls.restaurantes:
            print(f'{rest._name.ljust(25)} | {rest._category.ljust(25)} | {rest.status.ljust(15)} | {str(rest.av_eval).ljust(15)}')

    @property
    def status(self) -> str:
        """Returns ``'ATIVO'`` if open, otherwise ``'DESATIVADO'``."""
        return 'ATIVO' if self._status else 'DESATIVADO'

    def change_status(self):
        """Toggles the restaurant's open/closed status."""
        self._status = not self._status

    def rec_eval(self, client: str, score: float):
        """Records a client evaluation if the score is in range [0, 5].

        Args:
            client: Name or identifier of the client.
            score: Score between 0 and 5; silently ignored otherwise.
        """
        if 0 <= score <= 5:
            self._eval.append(Eval(client, score))

    @property
    def av_eval(self) -> float | str:
        """Returns the average evaluation score, or ``'Sem avaliações'`` if none."""
        if not self._eval:
            return 'Sem avaliações'
        return round(sum(item._score for item in self._eval) / len(self._eval), 1)

    def add_item_menu(self, item: ItMe):
        """Adds an item to the menu if it is a valid :class:`ItMe` instance.

        Args:
            item: The menu item to add.
        """
        if isinstance(item, ItMe):
            self._menu.append(item)

    @property
    def show_menu(self):
        """Prints the full menu for this restaurant."""
        print(f'Cardápio do Restaurante {self._name}\n')
        for i, item in enumerate(self._menu, start=1):
            if hasattr(item, '_desc'):
                print(f'{i}. Nome: {item._name} | Preço: R${item._price:.2f} | {item._desc}')
            if hasattr(item, '_size'):
                print(f'{i}. Nome: {item._name} | Preço: R${item._price:.2f} | Tamanho: {item._size:.1f}ml')
