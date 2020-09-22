"""
This example simulates a developer 
turning some product backlog into product increment.
"""

import simpy
import random


def developer(env):
    count = 0
    while True:
        print("Picking the next ready work item to start on ...")
        duration = sample_development_duration()
        print(f"Developing for {duration} days ...")
        yield env.timeout(duration)
        count += 1
        print(f"Done! ({count} items on day {env.now})")


def sample_development_duration():
    return random.randrange(1, 5)


if __name__ == "__main__":
    print("Hello world!")
    random.seed(1)
    env = simpy.Environment()
    env.process(developer(env))
    env.run(until=42)
    print("Simulation done.")
