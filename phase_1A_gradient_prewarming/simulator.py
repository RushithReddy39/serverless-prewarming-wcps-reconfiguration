# simulator.py

from collections import deque

class Container:
    def __init__(self, id):
        self.id = id
        self.status = "IDLE"

class ContainerManager:
    def __init__(self, max_containers):
        self.containers = deque()
        self.max_containers = max_containers
        self.next_id = 0

    def create_container(self):
        if len(self.containers) < self.max_containers:
            c = Container(self.next_id)
            self.next_id += 1
            self.containers.append(c)

    def get_alive_count(self):
        return len(self.containers)

    def prewarm(self, count):
        for _ in range(count):
            self.create_container()

    def terminate_idle(self, count):
        for _ in range(count):
            if self.containers:
                self.containers.popleft()  # Remove the oldest idle container
