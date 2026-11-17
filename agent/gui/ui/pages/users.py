"""Users management page matching Page Membre.png mockup."""

import customtkinter as ctk

from theme import COLORS, FONTS, RADIUS
from ui.icons import ICON_ADD, ICON_SEARCH
from ui.pages.base import BasePage
from ui.table import ScrollableList
from ui.widgets import ItemRowCard


class UsersPage(BasePage):
    """Displays library members with search, add, edit, and delete actions."""

    def __init__(self, master, api) -> None:
        super().__init__(master, api)
        self.grid_rowconfigure(1, weight=1)

        toolbar = ctk.CTkFrame(self, fg_color="transparent")
        toolbar.grid(row=0, column=0, padx=24, pady=(20, 10), sticky="ew")

        ctk.CTkLabel(
            toolbar,
            text="ID",
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
        self.add_btn.grid(row=0, column=2, padx=(0, 8))

        self.list_frame = ScrollableList(self)
        self.list_frame.grid(row=1, column=0, padx=18, pady=(0, 18), sticky="nsew")

    def refresh(self) -> None:
        self.list_frame.clear()
        query = self.search_var.get().strip().lower()

        for user in self.api.get_all_users():
            if query and query not in user.user_id.lower() and query not in user.name.lower():
                continue
            count = len(user.borrowed_books)
            text = f"{user.name} ({user.user_id}) — {count} livre(s) emprunté(s)"
            row = ItemRowCard(
                self.list_frame,
                text=text,
                on_delete=lambda uid=user.user_id: self._on_delete_clicked(uid),
                on_edit=lambda uid=user.user_id: self._on_edit_clicked(uid),
            )
            self.list_frame.add_row(row)

    def _on_add_clicked(self) -> None:
        pass

    def _on_delete_clicked(self, user_id: str) -> None:
        pass

    def _on_edit_clicked(self, user_id: str) -> None:
        pass
