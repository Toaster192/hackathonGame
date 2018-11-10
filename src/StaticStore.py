import src.Config as Config
from src.Vector import Vector2


class StaticStore:
    offset = Vector2(0, 0)
    screen_shake = 0
    smoothed_offset = Vector2(0, 0)
    displacement_offset = Vector2(0, 0)

    @staticmethod
    def update_offset(pos):
        StaticStore.displacement_offset.y = max(
            StaticStore.displacement_offset.y,
            Config.SCREEN_HEIGHT // 2 - pos.y)
