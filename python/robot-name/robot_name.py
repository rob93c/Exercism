import random
from string import ascii_uppercase as letters, digits

class Robot(object):
    robots = set()

    def __init__(self):
        self.name = None
        self.reset()

    def reset(self):
        while self.name is None or self.name in self.robots:
            self.name = Robot.generate_name()
        self.robots.add(self.name)

    @staticmethod
    def generate_name():
    	part1 = ''.join(random.choice(letters) for i in range(2))
    	part2 = ''.join(random.choice(digits) for i in range(3))
    	return part1 + str(part2)
