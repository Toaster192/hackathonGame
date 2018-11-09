from src.PlaceholderGame import PlaceholderGame


def main():
    game = PlaceholderGame()
    game.init_screen((640, 480))
    game.run()


if __name__ == '__main__':
    main()
