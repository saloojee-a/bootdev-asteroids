from textwrap import fill

import pygame
from pygame import display

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)

    clock = pygame.time.Clock()
    dt = 0.0
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        fill("black")
        player.draw(screen)
        display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
