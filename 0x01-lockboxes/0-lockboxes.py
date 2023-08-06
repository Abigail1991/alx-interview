#!/usr/bin/python3
"""Lockboxes module.

This module contains a function related to the lockboxes.
"""


def canUnlockAll(boxes):
    """Determines if all the boxes can be opened.

    Args:
        boxes (lst): the list of boxes containing a list of keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    box_count = len(boxes)

    if box_count > 0:
        keys = boxes[0]
        boxes[0] = [-1]
        while keys:
            new_keys = []
            for key in keys:
                if key < box_count:
                    if boxes[key] != [-1]:
                        new_keys += boxes[key]
                        boxes[key] = [-1]
            keys = new_keys

        return boxes.count([-1]) == box_count

    return False
