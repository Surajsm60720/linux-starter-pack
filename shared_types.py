from typing import List

class SharedCart:
    """Shared cart state between screens"""
    items: List[str] = []

    @classmethod
    def add_item(cls, item: str) -> None:
        if item not in cls.items:
            cls.items.append(item)

    @classmethod
    def remove_item(cls, item: str) -> None:
        if item in cls.items:
            cls.items.remove(item)

    @classmethod
    def get_items(cls) -> List[str]:
        return cls.items.copy()

    @classmethod
    def clear(cls) -> None:
        cls.items.clear()

    @classmethod
    def is_in_cart(cls, item: str) -> bool:
        return item in cls.items