import math
import random
import time
from copy import deepcopy

import pygame
from brain import Brain


class Dot:
    max_velocity = 100000

    def __init__(
        self,
        screen,
        velocity: pygame.Vector2 = pygame.Vector2(0, 0),
        acceleration: pygame.Vector2 = pygame.Vector2(0, 0),
        goal: pygame.Vector2 = pygame.Vector2(0, 0),
    ):
        self.brain = Brain(400)
        self.dead = False
        self.reached_goal = False
        self.is_best = False

        self.screen = screen
        self.position = pygame.Vector2(screen.get_width() / 2, screen.get_height() - 10)
        self.velocity = velocity
        self.acceleration = acceleration
        self.goal = goal

    def show(self):
        if self.is_best:
            pygame.draw.circle(self.screen, "white", self.position, 5)
        else:
            pygame.draw.circle(self.screen, "red", self.position, 5)

    def move(self):
        if len(self.brain.directions) > self.brain.step:
            self.acceleration = self.brain.directions[self.brain.step]
            self.brain.step += 1
        else:
            self.dead = True

        self.velocity = self.velocity + self.acceleration
        if self.velocity.length() > self.max_velocity:
            self.velocity.scale_to_length(self.max_velocity)
        self.position = self.position + self.velocity

    def update(self):
        if self.dead or self.reached_goal:
            return
        self.move()
        if (
            self.position.x < 1
            or self.position.y < 1
            or self.position.x > self.screen.get_width() - 1
            or self.position.y > self.screen.get_height() - 1
        ):
            self.dead = True
        elif self.position.distance_to(self.goal) < 20:
            self.reached_goal = True

    def calculate_fitness(self):
        if self.reached_goal:
            self.fitness = 1 / 16 + 10000 / self.brain.step**2
        else:
            distance_to_goal = self.position.distance_squared_to(self.goal)
            self.fitness = 1 / (distance_to_goal)

    def create_descent(self):
        dot = Dot(self.screen, goal=self.goal)
        dot.brain = deepcopy(self.brain)
        dot.brain.step = 0
        return dot
