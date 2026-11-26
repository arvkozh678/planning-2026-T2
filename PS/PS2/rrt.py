from typing import List, Callable
import numpy as np
import random as rd
from environment import State, ManipulatorEnv, check_collision_traj

Nattempts = 100 # max attempts for the RRT

class RRTPlanner:

    def __init__(self,
                 env: ManipulatorEnv,
                 distance_fn: Callable,
                 max_angle_step: float = 10.0):
        """
        :param env: manipulator environment
        :param distance_fn: function distance_fn(state1, state2) -> float
        :param max_angle_step: max allowed step for each joint in degrees
        """
        self._env = env
        self._distance_fn = distance_fn
        self._max_angle_step = max_angle_step

    @staticmethod
    def sample(rng: Generator):
        q = rng.uniform(-180, 180, size=4)
        return State(q)

    def find_nearest(self, qrand: State, Graph):
        idx_nearest = None
        min_distance = 1000000
        for pair in Graph:
            if idx_nearest == None:
                idx_nearest = Graph.index(pair)
                min_distance = self._distance_fn(pair[0], qrand)
            else:
                if self._distance_fn(pair[0], qrand) < min_distance:
                    idx_nearest = Graph.index(pair)
                    min_distance = self._distance_fn(pair[0], qrand)

        return Graph[idx_nearest]

    def steer(self, qrand, qnear):
        return qnear + (qrand - qnear)*self._max_angle_step
    
    def plan(self,
             start_state: State,
             goal_state: State) -> List[State]:
        
        G = [(start_state, None)] 
        rng = np.random.default_rng() # seed for randomizing the sample(C)
        for n in range(Nattempts):
            qrand = sample(rng)
            qnear = self.find_nearest(qrand=qrand, Graph=G)
            qnew = self.steer(qrand, qnear)
            if 
            pass

    
    