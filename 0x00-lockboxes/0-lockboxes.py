#!/usr/bin/python3
"""
0-lockboxes
"""


def canUnlockAll(boxes):
    """
    Return true if all the boxes can be opened.
    """
    boxes_amount = len(boxes)
    if boxes_amount == 0:
        return True
    boxes_state = [False]*boxes_amount
    boxes_state[0] = True
    keys = boxes[0]
    keys_used = []
    keys_needed = range(0, boxes_amount)
    while(len(keys) > 0):
        if keys[0] not in keys_used and keys[0] in keys_needed:
            boxes_state[keys[0]] = True
            keys_used.append(keys[0])
            fillKeys(keys, boxes[keys[0]])
        keys.pop(0)

    return sum(boxes_state) == boxes_amount


def fillKeys(keys, boxKeys):
    """
    Append boxKeys to keys
    """
    for key in boxKeys:
        if key not in keys:
            keys.append(key)
