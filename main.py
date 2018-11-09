from src.PlaceholderGame import PlaceholderGame


def main():
    game = PlaceholderGame()
    game.init('Cool game', (512, 640))
    game.run()


if __name__ == '__main__':
    main()
