import pygame

class TitleBoard(object):
    def __init__(self, screen, rect):
        self.screen = screen
        self.background_color = (250, 248, 239)
        self.rect = rect

        self.title_font = pygame.font.SysFont('comicsansms', 36)
        self.title_color = (118, 110, 101)
        self.title_text = self.title_font.render("Game 2048", True, self.title_color)

    def display(self):
        pygame.draw.rect(self.screen, self.background_color, self.rect)
        self.screen.blit(self.title_text, (self.rect.left + self.rect.width / 2 - self.title_text.get_width() /2, self.rect.top + self.rect.height / 2 ))
