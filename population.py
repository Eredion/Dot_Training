import random

from dot import Dot


class Population:
    def __init__(self, screen, goal, size):
        self.sceen = screen
        self.goal = goal
        self.generation = 0
        self.min_step = 400

        self.dots: list[Dot] = []
        for _ in range(size):
            self.dots.append(Dot(screen, goal=goal))

    def show(self):
        for dot in self.dots:
            dot.show()

    def update(self):
        for dot in self.dots:
            if dot.brain.step > self.min_step:
                dot.dead = True
            else:
                dot.update()

    def calculate_fitness(self):
        for dot in self.dots:
            dot.calculate_fitness()

    def all_dots_dead(self):
        for dot in self.dots:
            if not dot.dead and not dot.reached_goal:
                return False
        return True

    def natural_selection(self):
        new_dots = []
        self.set_best_dot()
        new_dots.append(self.best_dot.create_descent())
        new_dots[0].is_best = True
        for _ in range(len(self.dots) - 1):
            parent = self.select_parent()
            descent = parent.create_descent()
            new_dots.append(descent)

        self.dots = new_dots
        self.generation += 1

    def calculate_fitness_sum(self):
        return sum([dot.fitness for dot in self.dots])

    def select_parent(self):
        rand = random.uniform(0, self.calculate_fitness_sum())
        running_sum = 0

        for dot in self.dots:
            running_sum += dot.fitness
            if running_sum > rand:
                return dot

    def mutate(self):
        for dot in self.dots[1:]:
            dot.brain.mutate()

    def set_best_dot(self):
        self.best_dot = self.dots[0]
        for dot in self.dots:
            if dot.fitness > self.best_dot.fitness:
                self.best_dot = dot

        if self.best_dot.reached_goal:
            self.min_step = self.best_dot.brain.step
