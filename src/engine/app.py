import sys

import pygame
import pygame.freetype as ft


class App:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        # TODO: fix font & bake into exe
        self.font = ft.SysFont(ft.get_default_font(), 18)
        self.dt = 0.0
        self.running = False

    def update(self):
        pygame.display.flip()
        self.dt = self.clock.tick() * 0.001

    def draw(self):
        self.screen.fill("black")
        self.draw_fps()

    def check_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

    def draw_fps(self) -> None:
        fps = f"{self.clock.get_fps() :.0f} FPS"
        self.font.render_to(self.screen, (0,0), text=fps, fgcolor="white", bgcolor="black")

    def run(self) -> None:
        self.running = True

        while True:
            self.check_events()
            self.update()
            self.draw()

            #self.clock.tick(60)  # limits FPS to 60


if __name__ == "__main__":
    app = App()
    app.run()
