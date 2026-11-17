"""Python facade for the Bibliothèque C++ library (starter stub)."""

from dataclasses import dataclass, field
from typing import List


@dataclass
class BookDTO:
    title: str
    author: str
    isbn: str
    is_available: bool = True
    borrower_id: str = ""


@dataclass
class UserDTO:
    name: str
    user_id: str
    borrowed_books: List[str] = field(default_factory=list)


class BibliothequeAPI:
    """Starter API facade; will later wrap the pybind11 C++ module."""

    def __init__(self) -> None:
        self._books: List[BookDTO] = [
            BookDTO("1984", "George Orwell", "978-0451524935", True),
            BookDTO("Le Petit Prince", "Antoine de Saint-Exupéry", "978-2070612758", False, "U001"),
            BookDTO("Dune", "Frank Herbert", "978-0441172719", True),
        ]
        self._users: List[UserDTO] = [
            UserDTO("Alice Martin", "U001", ["978-2070612758"]),
            UserDTO("Bob Tremblay", "U002", []),
            UserDTO("Claire Gagnon", "U003", []),
        ]

    def get_all_books(self) -> List[BookDTO]:
        return list(self._books)

    def get_all_users(self) -> List[UserDTO]:
        return list(self._users)
