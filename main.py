from src import TetrisGame
import src.Config as Config


def main():
    game = TetrisGame()
    game.init('Cool game', (Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))
    while game.run() == "restart":
        game = TetrisGame()
        game.init('Restarted game', (Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))


if __name__ == '__main__':
    main()
