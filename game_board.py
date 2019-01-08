import pygame
from game_matrix import GameMatrix
from num_image import NumImage

class GameBoard(object):
    def __init__(self, screen, rect, dim):
        self.dim = dim
        self.screen = screen
        self.background_color = (186, 172, 159)
        self.rect = rect

        self.num_imgs_width = 0
        self.num_imgs_margin = 0
        self.num_imgs_layout = [[None] * dim for i in range(dim)]
        self.config_num_imgs_layout()

        self.num_imgs = NumImage('./imgs/', self.num_imgs_width).number_img_book

        self.game_matrix = GameMatrix(dim)

    def display(self):
        pygame.draw.rect(self.screen, self.background_color, self.rect)

        for i in range(self.dim):
            for j in range(self.dim):
                self.screen.blit(self.num_imgs[int(self.game_matrix.matrix[i][j])], self.num_imgs_layout[i][j])

    def config_num_imgs_layout(self):
        self.num_imgs_margin = self.rect.width / 30
        self.num_imgs_width = int((self.rect.width - self.num_imgs_margin * (self.dim + 1)) / self.dim)
        for i in range(self.dim):
            for j in range(self.dim):
                top = self.rect.top + self.num_imgs_margin * (i + 1) + self.num_imgs_width * i
                left = self.rect.left + self.num_imgs_margin * (j + 1) + self.num_imgs_width * j
                self.num_imgs_layout[i][j] = (left, top)

    def move(self, direction):
        self.game_matrix.move(direction)
        self.game_matrix.random_add_one()
