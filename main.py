from src.PlaceholderGame import PlaceholderGame
import src.Config as Config


def main():
    game = PlaceholderGame()
    game.init('Cool game', (Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))
    game.run()


if __name__ == '__main__':
    main()
