import math
import random
import time

import numpy as np
import pygame


class Brain:
    mutation_rate = 0.01

    def __init__(self, size):
        self.step = 0
        self.directions = []
        self.size = size
        random.seed(time.time())
        self.randomize()

    def randomize(self):
        for _ in range(self.size):
            angle = random.random() * 2 * math.pi
            self.directions.append(pygame.Vector2(math.cos(angle), math.sin(angle)))

    def mutate(self):
        for i in range(len(self.directions)):
            if random.random() < self.mutation_rate:
                angle = random.random() * 2 * math.pi
                self.directions[i] = pygame.Vector2(math.cos(angle), math.sin(angle))
