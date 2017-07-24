import copy

states = [[1, 0.0], [2, 0.0], [3, 0.0], [4, 0.0], [5, 0.0], [6, 0.0], [7, 0.0], [8, 0.0], [9, 0.0]]

simple_states = [[1, 1], [2,1], [3, 1]]

tree = {}

def create_tree(states):
    tree['0'] = states[:]

def grow_tree(tree, start, states):
    for i in range(0, len(states)):
        new_states = states[:]
        key = start + str(new_states.pop(i)[0])
        print(new_states)
        if len(new_states) > 0:
            tree[key] = new_states
        grow(tree, key, new_states)
