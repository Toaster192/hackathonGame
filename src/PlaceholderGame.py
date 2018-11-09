import pygame
from src.Game import Game


class PlaceholderGame(Game):
    def __init__(self):
        pass

    # Gets called at game end (pressed [X])
    def clean_up(self):
        pass

    # Gets called on PyGame event
    def handle_event(self, event):
        pass

    # Called every frame, dt is time between frames
    def loop(self, dt):
        pass

    # Called after loop(), renders the game screen
    def render(self):
        pass
