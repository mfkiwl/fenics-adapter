from .solverstate import SolverState

class Checkpoint:

    def __init__(self):
        """
        A checkpoint for the solver state
        """
        self._state = None

    def get_state(self):
        return self._state

    def write(self, new_state):
        """
        write checkpoint from solver state.
        :param u: function value
        :param t: time
        :param n: timestep
        """
        if not self.is_empty():
            self._state.update(new_state)
        else:
            self._state = new_state

    def is_empty(self):
        """
        Returns whether checkpoint is empty. An empty checkpoint has no state saved.
        :return:
        """
        return not self._state
