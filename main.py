from src.PlaceholderGame import PlaceholderGame


def main():
    game = PlaceholderGame()
    game.init_screen('Cool game', (1024, 512))
    game.run()


if __name__ == '__main__':
    main()
