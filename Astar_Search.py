tree = {'S': [['A', 1], ['B', 5], ['C', 8]],
        'A': [['S', 1], ['D', 3], ['E', 7], ['G', 9]],
        'B': [['S', 5], ['G', 4]],
        'C': [['S', 8], ['G', 5]],
        'D': [['A', 3]],
        'E': [['A', 7]]}

# tree2 = {'S': [['A', 1], ['B', 2]],
#          'A': [['S', 1]],
#          'B': [['S', 2], ['C', 3], ['D', 4]],
#          'C': [['B', 2], ['E', 5], ['F', 6]],
#          'D': [['B', 4], ['G', 7]],
#          'E': [['C', 5]],
#          'F': [['C', 6]]
#          }

heuristic = {'S': 8, 'A': 8, 'B': 4, 'C': 3, 'D': 5000, 'E': 5000, 'G': 0}  # cng 'G'
# heuristic2 = {'S': 0, 'A': 5000, 'B': 2, 'C': 3, 'D': 4, 'E': 5000, 'F': 5000, 'G': 0}

cost = {'S': 0}  # cng 'S'


def AStarSearch():
    global tree, heuristic
    closed = []  # closed nodes
    opened = [['S', 8]]  # opened nodes

    '''find the visited nodes'''
    par = {'S': 'S', 'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E', 'F': 'F'}  # cng node

    while True:
        fn = [i[1] for i in opened]  # fn = f(n) = g(n) + h(n)
        chosen_index = fn.index(min(fn))
        node = opened[chosen_index][0]  # current node
        closed.append(opened[chosen_index])

        del opened[chosen_index]
        if closed[-1][0] == 'G':  # cng 'G'
            break

        for item in tree[node]:
            if item[0] in [closed_item[0] for closed_item in closed]:
                continue

            cost.update({item[0]: cost[node] + item[1]})  # add nodes to cost dictionary
            fn_node = cost[node] + heuristic[item[0]] + item[1]  # calculate f(n) of current node
            temp = [item[0], fn_node]
            opened.append(temp)

            par[item[
                0]] = node  # a -> b, par[b] = a                          # store f(n) of current node in array opened

    '''find optimal sequence'''

    optimal_sequence = []
    goal = 'G'  # cng 'G'
    while par[goal] != goal:
        optimal_sequence.append(goal)
        goal = par[goal]

    optimal_sequence.append(goal)
    optimal_sequence.reverse()
    print(optimal_sequence)

    return closed, optimal_sequence


if __name__ == '__main__':
    visited_nodes, optimal_nodes = AStarSearch()
    print('visited nodes: ' + str(visited_nodes))
    print('optimal nodes sequence: ' + str(optimal_nodes))


