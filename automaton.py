class Config:

    def __init__(
            self,
            start_state: int,
            finish_states: list[int],
            transitions: dict[int, dict[str, int]]
    ):
        """
        :param start_state: Starting state of automaton
        :param finish_states: List of finish states
        :param transitions: Dict of transitions
        """

        self.start_state = start_state
        self.finish_states = finish_states
        self.transitions = transitions


class FiniteAutomaton:
    def __init__(self, config: Config):
        """
        :param config: Config for finite automaton
        """

        self.config = config

    def _next_state(self, state: int, char: str) -> int:
        """
        :param state: Current state
        :param char: Transitions symbol
        :return: Next state according to current state and transition
        """
        if char in self.config.transitions[state].keys():
            return self.config.transitions[state][char]
        return -1

    def find_chains(self, expr: str):
        """

        :param expr: String expression of regular language
        :return: List of all chains of regular language with their starting indexes
        """
        chains = []
        for i in range(len(expr)):
            current_state = self.config.start_state
            for j in range(i, len(expr)):
                current_state = self._next_state(current_state, expr[j])
                if current_state == -1:
                    break
                if current_state in self.config.finish_states:
                    chains.append((i, expr[i: j + 1]))
                    break
        return chains
