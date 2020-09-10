import simpy
import random

time_stamps = []


def work_item_process(env, team_skills, item_id):
    t = []
    t.append(env.now)

    for activity in ["specify", "build", "verify"]:
        resource = team_skills[activity]
        with resource.request() as req:
            yield req                                       # Wait for access to the capability
            # mark time of starting activity
            t.append(env.now)
            yield env.timeout(sample_activity_duration())   # Do work
            # mark time of ending activity
            t.append(env.now)

    time_stamps.append(t)


def work_generator(env, team_skills):
    item_id = 0
    while True:
        item_id += 1
        env.process(work_item_process(env, team_skills, item_id))
        yield env.timeout(sample_activity_duration())


def sample_activity_duration():
    # best sample this from your own data
    return random.randrange(1, 5)


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
