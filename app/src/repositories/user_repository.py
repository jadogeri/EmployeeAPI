"""
Player Repository Module
------------------------
Description: Concrete implementation of BaseRepository for handling
             Player entity persistence logic.

Author: Joseph Adogeri
Version: 1.0.0
Since: 2024-05-20
File: player_repository.py
License: MIT
"""
from __future__ import annotations
from src.models.player_model import PlayerModel
from src.repositories.base_repository import BaseRepository


class PlayerRepository(BaseRepository[PlayerModel]):
    def __init__(self):
        """
        Initializes the PlayerRepository with the Player model.
        """
        super().__init__(PlayerModel)

    def get_by_username(self, username: str) -> PlayerModel | None:
        """
        Specific query to find a player by their unique username.

        Args:
            username (str): The username to search for.

        Returns:
            PlayerModel | None: The player instance if found.
        """
        return self.model.query.filter_by(username=username).first()