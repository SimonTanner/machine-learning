import copy, random

states = [[1, 0.0], [2, 0.0], [3, 0.0], [4, 0.0], [5, 0.0], [6, 0.0], [7, 0.0], [8, 0.0], [9, 0.0]]

simple_states = [[1, 1], [2,1], [3, 1]]

class MachinePlayer():

    global states

    def __init__(self):
        self.tree = {}
        self.states = states
        self.counter = 0
        self.start = '0'
        self.path = '0'

    def create_tree(self):
        self.tree[self.start] = self.states[:]

    def grow_tree(self, start, states):
        tree = self.tree

        for i in range(0, len(states)):
            new_states = states[:]
            key = start + str(new_states.pop(i)[0])
            if len(new_states) > 0:
                tree[key] = new_states
            #print(new_states)
            self.grow_tree(key, new_states)

        self.tree = tree

    def choose_option(self, options):
        states = self.tree[self.path]
        max_chance = max(states, key=lambda x: x[1])[1]
        choices = []
        for i in states:
            if i[1] == max_chance:
                try:
                    options.index(i[0])
                    choices.append(i[0])
                except (ValueError, IndexError):
                    continue

        choice = random.choice(choices)
        self.path = self.path + str(choice)

        return choice
