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
import matplotlib.pyplot as plt

activities = ["specify", "build", "verify"]
time_stamps = {}

output_cycle_time_file_name = './output/02_cycle_times.csv'


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


def run(create_figures=False, until=42*42):
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
    env.run(until=until)

    print("Simulation done.")

    df = metrics.cycle_times(activities, time_stamps)

    # save cycle times to csv file:
    df.to_csv(output_cycle_time_file_name, index=False)

    if create_figures:
        # create cycle time figures
        cycle_time_figures, (ax1, ax2) = plt.subplots(nrows=2)
        cycle_time_figures.set_size_inches(8.27, 11.69)  # A4

        ax1 = metrics.cycle_time_scatter_plot(df, ax=ax1)
        ax2 = metrics.cycle_time_histogram_plot(df, ax=ax2)

        cycle_time_figures.savefig('./output/02_cycle_time_plots.pdf')


if __name__ == "__main__":
    run()
