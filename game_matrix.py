import numpy
import random
from enum import Enum

class Direction(Enum):
    kUp, kRight, kDown, kLeft = range(4)

class GameMatrix(object):
    def __init__(self, dim):
        self.dim = dim
        self.matrix = numpy.zeros((dim, dim))
        self.init_matrix()

        self.tube = []

    def init_matrix(self):
        indices = [i for i in range(self.dim * self.dim)]
        random.shuffle(indices)
        pick_number = random.choices([2, 4], k=2)
        self.matrix[indices[0] // self.dim][indices[0] % self.dim] = pick_number[0]
        self.matrix[indices[1] // self.dim][indices[1] % self.dim] = pick_number[1]

    def random_pick_empty(self):
        empty_spots = []
        for i in range(self.dim):
            for j in range(self.dim):
                if self.matrix[i][j] == 0:
                    empty_spots.append([i, j])

        return random.choices(empty_spots)[0]

    def random_add_one(self):
        my_pick = self.random_pick_empty()
        self.matrix[my_pick[0]][my_pick[1]] = random.choices([2, 4], weights=[.5, .5])[0]

    def tube_append(self, elem):
        if elem != 0:
            if len(self.tube) != 0 and self.tube[-1] == elem:
                self.tube[-1] *= 2
            else:
                self.tube.append(elem)

    def move(self, direction):
        if direction == Direction.kDown:
            for j in range(self.dim):
                for i in range(self.dim):
                    elem = self.matrix[self.dim - 1 - i][j]
                    self.tube_append(elem)
                    self.matrix[self.dim - 1 - i][j] = 0

                for i in range(len(self.tube)):
                    self.matrix[self.dim - 1 - i][j] = self.tube[i]

                self.tube.clear()
        elif direction == Direction.kUp:
            for j in range(self.dim):
                for i in range(self.dim):
                    elem = self.matrix[i][j]
                    self.tube_append(elem)
                    self.matrix[i][j] = 0

                for i in range(len(self.tube)):
                    self.matrix[i][j] = self.tube[i]

                self.tube.clear()
        elif direction == Direction.kLeft:
            for i in range(self.dim):
                for j in range(self.dim):
                    elem = self.matrix[i][j]
                    self.tube_append(elem)
                    self.matrix[i][j] = 0

                for j in range(len(self.tube)):
                    self.matrix[i][j] = self.tube[j]

                self.tube.clear()
        elif direction == Direction.kRight:
            for i in range(self.dim):
                for j in range(self.dim):
                    elem = self.matrix[i][self.dim - 1 - j]
                    self.tube_append(elem)
                    self.matrix[i][self.dim - 1 - j] = 0

                for j in range(len(self.tube)):
                    self.matrix[i][self.dim - 1 - j] = self.tube[j]

                self.tube.clear()
