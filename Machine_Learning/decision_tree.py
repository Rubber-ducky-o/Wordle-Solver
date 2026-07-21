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

class DSTree:

    def __init__(self,depth = 1):
        self.root = None
        self.depth = depth

    def class_prob_vector(self, y):
        len_of_y = len(y)
        zero_count = 0
        one_count = 0
        for val in y:
            if val ==0:
                zero_count+=1
            else:
                one_count+=1

        prob_zero = zero_count / len_of_y
        prob_one = one_count / len_of_y

        arr = np.array([prob_zero,prob_one])

    def leaf_condition(self,node):
        if self.max_depth == node.depth:
            return True
        else:
            for val in (node.probs):
                if val == 1:
                    return True
        return False

    def gini_score(self,X,y,i,threshold):

        left_y = []
        right_y = []

        for r in range(len(X)):
            if X[r][i] > threshold:
                right_y.append(y[r])
            else:
                left_y.append(y[r])

        length_y = len(y)
        nL = len(left_y)
        nR = len(right_y)

        def gini_side(side):
            feat = len(side)
            if feat ==0:
                return 0.0
            zero_count = 0
            one_count =0
            for label in side:
                if label == 0:
                    zero_count+=1
                else:
                    one_count +=1
            p0 = zero_count / feat
            p1 = zero_count / feat

            return 1.0 - (p0 **2 + p1 **2)

        G_L = gini_side(left_y)
        G_R = gini_side(right_y)

        return (nL / length_y) * G_L + (nR / length_y) * G_R


