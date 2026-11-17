"""Loans and returns / settings starter page."""

import customtkinter as ctk

from theme import COLORS, FONTS
from ui.pages.base import BasePage


class SettingsPage(BasePage):
    """Starter page for loans/returns or application settings."""

    def __init__(self, master, api) -> None:
        super().__init__(master, api)
        self.grid_rowconfigure(0, weight=1)

        label = ctk.CTkLabel(
            self,
            text="Prêt & retours — à implémenter",
            font=FONTS["title"],
            text_color=COLORS["text_light"],
        )
        label.grid(row=0, column=0, padx=24, pady=24)
