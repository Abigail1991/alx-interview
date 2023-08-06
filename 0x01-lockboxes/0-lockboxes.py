#!/usr/bin/python3
"""Lockboxes module.

This module contains a function related to the lockboxes.
"""


def canUnlockAll(boxes):
    """Determine if all the boxes can be opened.

    Args:
        boxes (list): A list of lists. A key with the same number as a box opens that box.

    Returns:
        bool: True if all boxes can be opened, else False.
    """
    n = len(boxes)  # Total number of boxes
    visited = [False] * n  # Keep track of visited boxes
    visited[0] = True  # The first box is unlocked initially
    stack = [0]  # Start with the first box in the stack
    
    while stack:
        current_box = stack.pop()
        
        # Iterate through keys in the current box
        for key in boxes[current_box]:
            if key >= 0 and key < n and not visited[key]:
                visited[key] = True
                stack.append(key)
    
    # Check if all boxes have been visited
    return all(visited)
