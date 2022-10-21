from datetime import datetime
from itertools import combinations

###########################
# for alpha
########################


def find_alpha(V, fam_sets):
    # iterate through different length minimum sets
    for i in range(len(V)):
        # iterate over potential minimum set
        for potential_min in list(combinations(V, i)):
            if valid(potential_min, fam_sets):
                return i, potential_min


def valid(potential_min, fam_sets):
    # check's if intersection with each of the sets is none-empty
    for s in fam_sets:
        if not intersect_none_empty(potential_min, s):
            return False
    return True


def intersect_none_empty(a, b):
    x = set(b)
    for i in a:
        if i in x:
            return True
    return False

###############
# For Beta
###############


def find_beta(V, fam_sets):
    upper_bound = find_alpha(V, fam_sets)[0]
    # keep increasing i to find max
    for i in range(2, upper_bound):
        if not find_valid_disjoint(V, fam_sets, i):
            return i - 1
    return upper_bound


def find_valid_disjoint(V, fam_sets, i):
    # iterate over all combinations of sets in fam_sets
    # attempt to find pairwise disjoint set

    sets = list(combinations(fam_sets, i))
    for potential_max in sets:
        if sum([len(a) for a in potential_max]) > len(V):
            continue
        if pairwise_disjoint(potential_max):
            return True
    return False


def pairwise_disjoint(set_of_sets):
    # check's if set of sets are pairwise disjoint
    a = set()
    for s in set_of_sets:
        for val in s:
            if val in a:
                return False
            a.add(val)
    return True

#######
# Example
##########


A = [i for i in range(1, 13)]
fam = list(combinations(A, 5))

start_time = datetime.now()

print(f'Alpha is: {find_alpha(A, fam)[0]}')
second_time = datetime.now()
print(f'Time taken for alpha: {second_time - start_time}')


print(f'Beta is: {find_beta(A, fam)}')
final_time = datetime.now()
print(f'Time taken for beta: {final_time - second_time}')
