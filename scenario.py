"""
Scenario Creator
AI-Based Digital Twin for Water Leak Impact & Response Optimisation
"""

import random
import config


class LeakScenario:
    def __init__(self):

        # Choose a valid junction directly
        self.junction = random.choice([
            "J1", "J2", "J3", "J4",
            "J5", "J6", "J7", "J8"
        ])

        self.leak_size = random.choice(
            list(config.LEAK_SIZES.keys())
        )

        self.demand = random.choice(
            list(config.DEMAND_LEVELS.keys())
        )

        self.start_hour = random.randint(0, 23)

        self.duration = random.randint(1, 6)

    def display(self):
        print("=" * 40)
        print("DIGITAL TWIN SCENARIO")
        print("=" * 40)
        print(f"Leak Junction : {self.junction}")
        print(f"Leak Size     : {self.leak_size}")
        print(f"Demand Level  : {self.demand}")
        print(f"Start Hour    : {self.start_hour}:00")
        print(f"Duration      : {self.duration} hour(s)")
        print("=" * 40)


if __name__ == "__main__":
    scenario = LeakScenario()
    scenario.display()
