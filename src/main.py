import pygame
from json import load

pygame.init()
screen = pygame.display.set_mode((512, 512))
settings = load(open("./data/settings.json", "r", encoding="utf-8"))

dark_square = pygame.Color(int(settings["dark_squares"], 16) << 8)
light_square = pygame.Color(int(settings["light_squares"], 16) << 8)

def draw_board():
    for file in range(8):
        for rank in range(8):
            rect = pygame.Rect(file*64, rank*64, 64, 64)

            if (file % 2) == (rank % 2):
                pygame.draw.rect(screen, light_square, rect)
            else:
                pygame.draw.rect(screen, dark_square, rect)

#exit()

def main():
    while True:
        draw_board()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return


if __name__ == "__main__":
    main()
