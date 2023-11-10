from automaton import FiniteAutomaton, Config
import config as cfg

if __name__ == "__main__":
    expr = input()
    config = Config(cfg.start, cfg.finish, cfg.transitions)
    automaton = FiniteAutomaton(config)
    chains = automaton.find_chains(expr)
    if len(chains) == 0:
        print("No chains found")
    else:
        for index, chain in chains:
            print(index + 1, chain)
