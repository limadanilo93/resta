"""Entry point for the restaurant menu loader.

Fetches a JSON array from a user-supplied URL, builds one
:class:`~Modelos.Re.Restaurante` per unique company found in the data,
and prints each restaurant's menu.

Expected JSON shape (list of objects)::

    [
        {
            "Company": "Plaza mais",
            "Item": "Pãozinho",
            "price": 3.0,
            "description": "Pão delicia baiano"
        },
        ...
    ]
"""

import requests
from Modelos.Re import Restaurante
from Modelos.Menus.it_me import ItMe


def load_from_url(url: str) -> list[dict]:
    """Fetches and parses a JSON array from the given URL.

    Args:
        url: HTTP/HTTPS URL pointing to a JSON array of menu entries.

    Returns:
        A list of dicts, one per menu entry.

    Raises:
        requests.HTTPError: If the server returns a non-2xx status code.
    """
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def build_restaurants(data: list[dict]) -> list[Restaurante]:
    """Builds :class:`~Modelos.Re.Restaurante` instances from raw JSON data.

    Groups entries by ``Company``, creates one restaurant per company, and
    adds a menu item for each entry using :meth:`~Modelos.Menus.it_me.ItMe.from_dict`.

    Args:
        data: List of dicts with keys ``Company``, ``Item``, ``price``,
            and either ``description`` or ``size``.

    Returns:
        List of populated :class:`~Modelos.Re.Restaurante` instances.
    """
    restaurants: dict[str, Restaurante] = {}
    for entry in data:
        company = entry['Company']
        if company not in restaurants:
            restaurants[company] = Restaurante(company, 'Geral')
            restaurants[company].change_status()
        item = ItMe.from_dict(entry)
        restaurants[company].add_item_menu(item)
    return list(restaurants.values())


def main():
    """Prompts for a URL, loads the data, and prints all restaurant menus."""
    url = input('Source URL: ')
    data = load_from_url(url)
    restaurants = build_restaurants(data)
    for rest in restaurants:
        rest.show_menu


if __name__ == '__main__':
    main()
