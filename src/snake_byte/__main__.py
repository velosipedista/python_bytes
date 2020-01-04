import sys
from game import game
import pygame

def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]

    snake = game();
    snake.setViewPort(640,80);
    snake.setDefaultBG();
    clock = pygame.time.Clock()
    while 1:
        clock.tick(60)

    # Do argument parsing here (eg. with argparse) and anything else
    # you want your project to do.

if __name__ == "__main__":
    main()