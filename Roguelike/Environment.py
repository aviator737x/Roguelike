class Environment:
    def __init__(self, mapGenerator, size):
        self.map = mapGenerator.generate_map()

