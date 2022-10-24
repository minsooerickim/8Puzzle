"""Driver code that calls the the appropriate algorithm based on user input."""
# import methods to create/utilize priority queue
from heapq import heappop, heappush
# import helper functions
from helper import pretty_print, goal_state, generate_next_states, pretty_print, find_goal_coordinates
# import typing to type parameters and declare return types
from typing import List
# used to record the elapsed time of the algorithms
from time import time

# TODO: DON'T COPY PASTE THE SAMPLE PROBLEM SETS TO THE REPORT
problem_set_depth_0 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]
problem_set_depth_2 = [
    [1, 2, 3],
    [4, 5, 6],
    [0, 7, 8]
]
problem_set_depth_4 = [
    [1, 2, 3],
    [5, 0, 6],
    [4, 7, 8]
]
problem_set_depth_8 = [
    [1, 3, 6],
    [5, 0, 2],
    [4, 7, 8]
]
problem_set_depth_12 = [
    [1, 3, 6],
    [5, 0, 7],
    [4, 8, 2]
]
problem_set_depth_16 = [
    [1, 6, 7],
    [5, 0, 3],
    [4, 8, 2]
]
problem_set_depth_20 = [
    [7, 1, 2],
    [4, 8, 5],
    [6, 3, 0]
]
problem_set_depth_24 = [
    [0, 7, 2],
    [4, 6, 1],
    [3, 5, 8]
]

def calculate_h_ucs(state: List[List[int]]) -> int:
    """
    Calculate h(n) for Uniform Cost Search.

    :param state: list of lists of integer values representing a state of the puzzle.
    :returns: 0
    """
    # Uniform Cost Search has a hard-coded h(n) value of 0
    return 0

def calculate_h_amt(state: List[List[int]]) -> int:
    """
    Calculate h(n) for A* with Misplaced Tiles.

    :param state: list of lists of integer values representing a state of the puzzle.
    :returns: the total number of misplaced tiles for the puzzle.
    """
    # count of the number of misplaced tiles
    count = 0
    # loop through every position of the given state and compare its value to the value at the same position in the goal state
    for i in range(3):
        for j in range(3):
            if (i, j) != find_goal_coordinates(state[i][j]) and state[i][j] != 0:
                count += 1
    return count

def calculate_h_amd(state:List[List[int]]) -> int:
    """
    Calculate h(n) for A* with Manhattan Distance.

    :param state: list of lists of integer values representing a state of the puzzle.
    :returns: the total manhattan distance.
    """
    # initialize all coordinate values to -1
    x1 = y1 = x2 = y2 = -1
    # variable to store the total sum of all manhattan distances for the given puzzle
    manhattan_dist_total = 0;
    
    # loop through every value in given puzzle and calculate manhattan distance by comparing to the goal state
    for x2 in range(3):
        for y2 in range(3):
            x1, y1 = find_goal_coordinates(state[x2][y2])
            manhattan_dist_total += abs(x1-x2)+abs(y1-y2)
            
    return manhattan_dist_total

# maps the name of the function to the queuing function to use
algorithm_to_queueing_fn = {
    'uniform_cost_search': calculate_h_ucs,
    'a_star_misplaced_tile': calculate_h_amt,
    'a_star_manhattan_distance': calculate_h_amd,
}

def general_search(state: List[List[int]], queueing_fn: str) -> None:
    """
    General search algorithm logic used with varying queueing function based on the algorithm chosen by user

    :param state: list of lists of integer values representing a state of the puzzle.
    """
    # depth of the puzzle
    depth = 0

    # print the depth and state of the initial puzzle
    print(f"\n-- depth {depth} --")
    pretty_print(state)

    # priority queue consisting of nodes that should be visited next based on minmum f(n) = g(n) + h(n)
        # pq stores a tuple (cost, depth, state) where cost is calculated by g(n) + h(n)
            # g(n) = the depth of node
            # h(n) = the heuristic value of node (varies based on the the search algorithm used)
    pq = []

    # list of states that have been visited
    visited_states = []

    # push the initial state to the priority queue
    heappush(pq, (algorithm_to_queueing_fn[queueing_fn](state) + 0, depth, state))

    # loop while queue isn't empty
    while pq:
        # get the node with the minimum cost (g(n) + h(n))
        min_cost, depth, min_state = heappop(pq)

        # check if the state has already been visited
        if min_state in visited_states:
            continue

        # add the state to visited_states to mark it as visited
        visited_states.append(min_state)
        
        # check if min_state is the goal state
        if min_state == goal_state:
            # stop searching when the goal state is found
            print(f"\n-- depth {depth} --")
            pretty_print(min_state)
            print(f'\n\ndepth of the solution: {depth}\n')
            return

        # generate a list of possible next states of the popped node's state
        list_of_next_states = generate_next_states(min_state)

        # loop through all the possible next states and add them to the priority queue if it hasn't been visited already
        for next_state in list_of_next_states:
            if next_state not in visited_states:
                heappush(pq, (algorithm_to_queueing_fn[queueing_fn](next_state) + (depth + 1), depth + 1, next_state))

        # print the state to trace the solution
        print(f"\n-- depth {depth} --")
        pretty_print(min_state)

    # puzzle is unsolvable if it reaches this point
    print('Puzzle not solvable!')
    return

if __name__ == "__main__":
    # store the algorithm to use from user
    search_method = input("1: Uniform Cost Search \n2: A* with the Misplaced Tile heuristic \n3: A* with the Manhattan Distance heuristic \n")
    
    # get the custom puzzle from user
    custom_puzzle = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append(int(input(f'\nEnter value for row {i} column {j}: ')))
        custom_puzzle.append(row)
    
    # time to measure the elapsed time of the algorithm to be run
    start_time = time()

    # call the general search function with the user-selected algorithm and user-selected puzzle
    if int(search_method) == 1:
        general_search(custom_puzzle, 'uniform_cost_search')
    elif int(search_method) == 2:
        general_search(custom_puzzle, 'a_star_misplaced_tile')
    elif int(search_method) == 3:
        general_search(custom_puzzle, 'a_star_manhattan_distance')
    else:
        print('enter valid search option')
    
    # stop the time once the algorithm finishes running
    end_time = time()

    # take the difference between start_time and end_time to find the total elapsed time
    print(f"Elapsed time: {end_time - start_time}\n")
    