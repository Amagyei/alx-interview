#!/usr/bin/python3
""" checks if all the boxes passed into the function can be unlocked by the keys derived from previous boxes 
"""

def canUnlockAll(boxes):
    keys = {0}
    opened_boxes = [0]
    while opened_boxes:
        current_box = opened_boxes.pop()  
        for new_key in boxes[current_box]:
            if new_key not in keys and new_key < len(boxes):
                keys.add(new_key)
                opened_boxes.append(new_key)
    for index in range(len(boxes)):
        if index not in keys:
            return False
    return True
