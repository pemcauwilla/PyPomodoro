from .observer import Observer

class Subject():
    def __init__(self):
        self.observers: list[Observer] = []

    def attach(self, obs : Observer) -> None:
        if obs not in self.observers:
            self.observers.append(obs)

    def notify(self) -> None:
        """Call update method on each of the current observers"""
        for obs in self.observers:
            obs.refresh_data()

            