import copy, random

states = [[1, 0.0], [2, 0.0], [3, 0.0], [4, 0.0], [5, 0.0], [6, 0.0], [7, 0.0], [8, 0.0], [9, 0.0]]
options = []

for i in range(1, 10):
    options.append(i)

class MachinePlayer():

    global states

    def __init__(self):
        self.tree = {}
        self.states = states
        self.counter = 0
        self.start = '0'
        self.path = '0'
        self.create_tree()
        self.grow_tree(self.start, self.states)

    def create_tree(self):
        self.tree[self.start] = self.states[:]

    def grow_tree(self, start, states):
        tree = self.tree

        for i in range(0, len(states)):
            new_states = states[:]
            key = start + str(new_states.pop(i)[0])
            if len(new_states) > 0:
                tree[key] = copy.deepcopy(new_states)
                
            self.grow_tree(key, new_states)

        self.tree = tree

    def choose_option(self, options):
        states = self.tree[self.path]
        state_options = list(map(lambda x: x[0], states))
        states = [i for i in states if i[0] in options]
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

    def machine_win(self):
        for i in range(0, len(self.path)-1):
            index = int(i)
            choice = int(self.path[index + 1])
            index_2 = list(map(lambda x: x[0], self.tree[self.path[0:(index + 1)]])).index(choice)
            branch = (self.tree[self.path[0:(index + 1)]])
            self.tree[self.path[0:(index + 1)]][index_2][1] = 1.0 + self.tree[self.path[0:(index + 1)]][index_2][1]
            total = sum(list(map(lambda x: x[1], self.tree[self.path[0:(index + 1)]])))

            for v in branch:
                v[1] = v[1] / total

        self.path = '0'
            #map(lambda x: [x[1] = x[1] / total], self.tree[self.path[0:(index + 1)]])
