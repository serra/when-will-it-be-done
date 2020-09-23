"""
This examples simulates a team with constrained capabilities.

The purpose of this simulation is to:

 * demonstrate the use of constrained resources
 * demonstrate a simple way to collect data on work items that you could apply in real life too
 * demonstrate how you could turn the collected data into meaningful charts

"""

import simpy
import random
from wwibd import metrics

activities = ["specify", "build", "verify"]
time_stamps = {}


def work_item_process(env, team_skills, item_id):
    # timestamps for this item
    t = []
    time_stamps[item_id] = t

    # log starting the work
    t.append(env.now)

    for activity in activities:
        resource = team_skills[activity]
        with resource.request() as req:
            yield req                                       # Wait for access to the capability
            # mark time of starting activity
            t.append(env.now)
            yield env.timeout(sample_activity_duration())   # Do work
            # mark time of ending activity
            t.append(env.now)


def work_generator(env, team_skills):
    item_id = 0
    while True:
        item_id += 1
        env.process(work_item_process(env, team_skills, item_id))
        yield env.timeout(sample_activity_duration())


def sample_activity_duration():
    # best sample this from your own data
    return random.random() * 5.0


if __name__ == "__main__":
    print("Hello world!")
    random.seed(1)
    env = simpy.Environment()

    # the team
    team_skills = {
        "specify": simpy.Resource(env, 2),
        "build": simpy.Resource(env, 2),
        "verify": simpy.Resource(env, 2)
    }

    env.process(work_generator(env, team_skills))
    env.run(until=42*42)

    print("Simulation done.")

    df = metrics.cycle_times(activities, time_stamps)

    # save cycle times to csv file:
    df.to_csv('./output/02_cycle_times.csv')

    # create and save plot
    axes = metrics.cycle_time_scatter_plot(df)
    metrics.save_plot(axes, './output/02_cycle_time_scatter_plot.png')
