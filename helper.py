# import deepcopy to make copy of states
from copy import deepcopy
# import typing to type parameters and declare return types
from typing import List, Tuple

def find_blank_pos(state: List[List[int]]) -> Tuple[int, int]:
    """
    Finds the position (row, col) with the value 0.

    :param state: list of lists of integer values representing a state of the puzzle.
    :returns: the row and col of the 0 position.
    """
    # loop through every position in the goal matrix and check if its 0
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def find_goal_coordinates(val: int) -> Tuple[int, int]:
    """
    Find the position (row, col) of a value in the goal state.

    :param val: value to find the position of.
    :returns: the row and col of the position value is in.
    """
    # loop through every position in the goal matrix and compare its value to the given value
    for i in range(3):
        for j in range(3):
            if goal_state[i][j]==val:
                return i, j
                
def generate_next_states(state: List[List[int]]) -> List[List[int]]:
    """
    Generates a list of states possible after making one move on a given state.

    :param state: list of lists of integer values representing a state of the puzzle.
    :returns: the list of possible states.
    """
    def helper(swappable_indices: List[Tuple[int, int]]):
        """
        Given the indices of next possible moves for the value 0, generates the list of next possible states.

        :param swappable_indices: list of (row, col) of the positions 0 can move to.
        """
        for swap_x, swap_y in swappable_indices:
            # create a deepcopy of the state to use for the next state
            copy_state = deepcopy(state)
            
            # perform the swap and save it to the copy we made in the line above
            copy_state[blank_pos_x][blank_pos_y], copy_state[swap_x][swap_y] = copy_state[swap_x][swap_y], copy_state[blank_pos_x][blank_pos_y]
            # append the swapped copy/next possible state to the list of next states
            list_of_next_states.append(copy_state)

    # list to store the possible next states
    list_of_next_states = []

    # call helper function to find the position of 0 in the given state
    blank_pos_x, blank_pos_y = find_blank_pos(state)

    # check the position of 0 and create a list of indices the 0 can move to
    if blank_pos_x == 0 and blank_pos_y == 0:
        pos_indices_to_move = [(0, 1), (1, 0)]
        helper(pos_indices_to_move)
    elif blank_pos_x == 0 and blank_pos_y == 1:
        pos_indices_to_move = [(0, 0), (0, 2), (1, 1)]
        helper(pos_indices_to_move)
    elif blank_pos_x == 0 and blank_pos_y == 2:
        pos_indices_to_move = [(0, 1), (1, 2)]
        helper(pos_indices_to_move)
    elif blank_pos_x == 1 and blank_pos_y == 0:
        pos_indices_to_move = [(0, 0), (1, 1), (2, 0)]
        helper(pos_indices_to_move)
    elif blank_pos_x == 1 and blank_pos_y == 1:
        pos_indices_to_move = [(0, 1), (1, 0), (1, 2), (2, 1)]
        helper(pos_indices_to_move)
    elif blank_pos_x == 1 and blank_pos_y == 2:
        pos_indices_to_move = [(0, 2), (1, 1), (2, 2)]
        helper(pos_indices_to_move)
    elif blank_pos_x == 2 and blank_pos_y == 0:
        pos_indices_to_move = [(1, 0), (2, 1)]
        helper(pos_indices_to_move)
    elif blank_pos_x == 2 and blank_pos_y == 1:
        pos_indices_to_move = [(2, 0), (1, 1), (2, 2)]
        helper(pos_indices_to_move)
    elif blank_pos_x == 2 and blank_pos_y == 2:
        pos_indices_to_move = [(2, 1), (1, 2)]
        helper(pos_indices_to_move)
    
    return list_of_next_states

def pretty_print(state: List[List[int]]) -> None:
    """
    Prints the given state in a 3x3 matrix format.

    :param state: list of lists of integer values representing a state of the puzzle.
    """
    # loop through every position of the given state and print newlines appropriately
    for i in range(3):
        for j in range(3):
            print(state[i][j], end=' ')
        print('\n')

# goal state
goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]