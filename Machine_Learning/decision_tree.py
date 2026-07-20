import numpy as np
import matplotlib.pyplot as plt

class Node:
    def __init__(self,depth):
        self.depth = depth
        self.split_feature = None
        self.threshold = None
        self.left_child = None
        self.right_child = None
        self.probs = None

    def __repr__(self):
        return f'DT Node: \n -| Depth: {self.depth}' \
                        f'\n -| Split feature: {self.split_feature}' \
                        f'\n -| Threshold: {self.threshold}' \
                        f'\n -| Probs: {self.probs}'


def main():
    return


