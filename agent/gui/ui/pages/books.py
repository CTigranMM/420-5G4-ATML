"""Books catalog page matching Page Livre.png mockup."""

import customtkinter as ctk

from theme import COLORS, FONTS, RADIUS
from ui.icons import ICON_ADD, ICON_SEARCH
from ui.pages.base import BasePage
from ui.table import ScrollableList
from ui.widgets import ItemRowCard


class BooksPage(BasePage):
    """Displays the book catalog with search, availability filter, and actions."""

    def __init__(self, master, api) -> None:
        super().__init__(master, api)
        self.grid_rowconfigure(1, weight=1)

        toolbar = ctk.CTkFrame(self, fg_color="transparent")
        toolbar.grid(row=0, column=0, padx=24, pady=(20, 10), sticky="ew")

        ctk.CTkLabel(
            toolbar,
            text="ISBN",
            font=FONTS["body"],
            text_color=COLORS["text_light"],
        ).grid(row=0, column=0, padx=(0, 10))

        self.search_var = ctk.StringVar()
        self.search_entry = ctk.CTkEntry(
            toolbar,
            textvariable=self.search_var,
            placeholder_text=ICON_SEARCH,
            width=200,
            height=34,
            corner_radius=RADIUS["input"],
            fg_color=COLORS["bg_input"],
            text_color=COLORS["text_primary"],
            border_width=0,
        )
        self.search_entry.grid(row=0, column=1, padx=(0, 14))
        self.search_var.trace_add("write", lambda *_: self.refresh())

        self.add_btn = ctk.CTkButton(
            toolbar,
            text=ICON_ADD,
            width=110,
            height=34,
            corner_radius=RADIUS["button"],
            fg_color=COLORS["bg_button"],
            hover_color=COLORS["bg_button_hover"],
            text_color=COLORS["text_primary"],
            font=FONTS["body"],
            command=self._on_add_clicked,
        )
        self.add_btn.grid(row=0, column=2, padx=(0, 16))

        self.available_only_var = ctk.BooleanVar(value=False)
        self.available_check = ctk.CTkCheckBox(
            toolbar,
            text="Livre disponible",
            variable=self.available_only_var,
            text_color=COLORS["text_light"],
            font=FONTS["body"],
            fg_color=COLORS["bg_button"],
            checkmark_color=COLORS["text_primary"],
            command=self.refresh,
        )
        self.available_check.grid(row=0, column=3, padx=(0, 8))

        self.list_frame = ScrollableList(self)
        self.list_frame.grid(row=1, column=0, padx=18, pady=(0, 18), sticky="nsew")

    def refresh(self) -> None:
        self.list_frame.clear()
        query = self.search_var.get().strip().lower()
        only_avail = self.available_only_var.get()

        for book in self.api.get_all_books():
            if only_avail and not book.is_available:
                continue
            if query and query not in book.isbn.lower() and query not in book.title.lower():
                continue
            status = "Disponible" if book.is_available else f"Emprunté ({book.borrower_id})"
            text = f"{book.title} — {book.author} | ISBN: {book.isbn} | {status}"
            row = ItemRowCard(
                self.list_frame,
                text=text,
                on_delete=lambda isbn=book.isbn: self._on_delete_clicked(isbn),
            )
            self.list_frame.add_row(row)

    def _on_add_clicked(self) -> None:
        pass

    def _on_delete_clicked(self, isbn: str) -> None:
        pass
