import pygame

class NumImage(object):
    def __init__(self, lib_path, numner_img_width):
        self.lib_path = lib_path
        self.numner_img_width = numner_img_width
        self.number_img_book = {}
        self.load_images()

    def load_images(self):
        nums = [pow(2, i) for i in range(0, 14)]
        nums[0] = 0
        for num in nums:
            self.number_img_book[num] = pygame.transform.scale(pygame.image.load(self.lib_path + str(num) + '.bmp'), (self.numner_img_width, self.numner_img_width))
