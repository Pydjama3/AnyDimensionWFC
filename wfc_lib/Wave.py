from cmath import inf

from wfc_lib import *
from random import choice


class Wave:
    def __init__(self, w, h, rules: RuleCollection, init_state=None):
        self.wave = {}
        if init_state is None:
            init_state = []

        for pos, element in init_state:
            self.wave[pos] = {element: True}

        self.width = w
        self.height = h

        self.rules = rules

        for x in range(w):
            for y in range(h):
                if self.wave.get((x, y)) is None:
                    self.wave[(x, y)] = {member: True for member in rules.members}

        self.iteration_count = 0

        self.propagate()

    def observe(self):
        min_candidates_len = inf
        min_candidates = []
        for candidate in self.wave:
            current_length = len(self.wave[candidate])
            if current_length <= 1:
                continue
            if current_length < min_candidates_len:
                min_candidates_len = current_length
                min_candidates = [candidate]
            if current_length == min_candidates_len:
                min_candidates.append(candidate)

        if len(min_candidates) == 0:
            return

        rand_candidate = choice(min_candidates)

        # nonzeros = [key for key in self.wave.keys() if len(self.wave[key].keys())>1]
        #
        # if len(nonzeros) == 0:
        #     return
        #
        # minimum = min(nonzeros, key=lambda nonzero: len(self.wave[nonzero].keys()))

        self.wave[rand_candidate] = {choice(list(self.wave[rand_candidate].keys())): True}

        return rand_candidate  # minimum

    def propagate(self):
        for x in range(self.width):
            for y in range(self.height):
                remove = None
                for member in self.wave[(x, y)]:
                    if not self.wave[(x, y)][member]:
                        continue

                    details = self.rules.get(member).get_details(x, y)
                    for _x, _y in details:
                        i = max(0, min(_x, self.width - 1))
                        j = max(0, min(_y, self.height - 1))

                        if i != _x or j != _y:
                            continue

                        expected = set(details[(_x, _y)])
                        current = set(self.wave[(_x, _y)].keys())

                        if len(expected & current) == 0:
                            remove = member
                            break

                if remove is not None:
                    self.wave[(x, y)].pop(remove)

    def run_iteration(self):
        observed = self.observe()

        if not observed:
            return

        self.propagate()

        self.iteration_count += 1

    def auto_run(self):
        while True: # TODO: specify condition
            if self.observe() is None:
                break
            self.propagate()

