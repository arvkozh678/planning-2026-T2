import numpy as np
import pickle
from environment import State, ManipulatorEnv, check_collision_traj
from rrt import RRTPlanner
from video_util import animate_plan


# Task2A


    

# You are free to change any interfaces for your needs.

# Main
def main():
    with open("data.pickle", "rb") as handle:
        data = pickle.load(handle)

    start_state = State(np.array(data["start_state"]))
    goal_state = State(np.array(data["goal_state"]))

    # Task 1A
    env_start = ManipulatorEnv(obstacles=np.array(data["obstacles"]),
                         initial_state=start_state,
                         collision_threshold=data["collision_threshold"])
    # env_start.render()

    env_target = ManipulatorEnv(obstacles=np.array(data["obstacles"]),
                            initial_state=goal_state,
                            collision_threshold=data["collision_threshold"])
    # env_target.render()
    # Comments
    # The environment is ceaseless. Obstacles are softer than used to be. The power of the new environment is larger than of the discrete one (ie more points here, not cells)

    # Task 1B
    # print(data)
    # No collision
    state1, state2 = State(np.array([1,1,1,1])), State(np.array([-50,0,0,0]))
    env_state1 = ManipulatorEnv(obstacles=np.array(data["obstacles"]),
                            initial_state=state1,
                            collision_threshold=data["collision_threshold"])
    # env_state1.render()
    env_state2 = ManipulatorEnv(obstacles=np.array(data["obstacles"]),
                            initial_state=state2,
                            collision_threshold=data["collision_threshold"])
    # env_state2.render()
    # Collision
    state3, state4 = State(np.array([30,0,0,0])), State(np.array([-40,0,0,0]))
    env_state3 = ManipulatorEnv(obstacles=np.array(data["obstacles"]),
                            initial_state=state3,
                            collision_threshold=data["collision_threshold"])
    # env_state3.render()
    env_state4 = ManipulatorEnv(obstacles=np.array(data["obstacles"]),
                            initial_state=state4,
                            collision_threshold=data["collision_threshold"])
    # env_state4.render()
    states = (state1, state2, state3, state4)
    # for i, state in enumerate((env_state1, env_state2, env_state3, env_state4)):
    #     print(f'State #{i} collision: ', state.check_collision(states[i]))

    # Comments
    # Render results correspond to the check_collision()'s output

    # planner = RRTPlanner(env)

    # plan = planner.plan(start_state, goal_state)
    # print("RRT planner has finished successfully")

    # animate_plan(env, plan)

    # Task2A
    rng = np.random.default_rng()
    q = rng.uniform(-180, 180, size=4)
    f = q + 50
    check_collision_traj(q, f, 10, obstacles=np.array(data["obstacles"]),
                         collision_thr=data["collision_threshold"])
    # Comments:
    # Will add up positive and negative sequence later. Steps=10 chosen to see more various results.


if __name__ == '__main__':
    main()
