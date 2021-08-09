import random
"""Zoe Berling Algorithms Lab 4 Closest Pair DAC"""
"""For this lab, you will be solving the following problem: Given a group of points, find the closest
pair. However, to make this lab significantly easier to code, you only need to solve the problem
of finding the distance between the closest pair of points. Additionally, you will work only with
1-D points (i.e., with only one coordinate, like points on a number line) instead of 2-D or 3-D
points.
"""

"""recursive divide-and-conquer algorithm"""

"""1. The distance between the closest pair of points in the first half of the list
2. The distance between the closest pair of points in the second half of the list
3. The distance between the closest pair of points where one point of the pair is in the first
half of the list and the other point of the pair is in the second half of the list
"""
"""Divide: Split the list into two equal pieces.
 Conquer: Recursively find the closest pair distance in each sublist (obtains distances
1 and 2 from above).
 Combine: Compute the remaining distance (3 from above), and combine them by
taking the minimum of the three."""

def recCPairDist(points):
    """Performs the recursion: This function takes in a sorted list of points and performs the divide/conquer/combine steps
outlined earlier and returns minimum distance between the closest pair of points."""
    # base case
    if len(points) <= 1:  # continue with last item in list
        return points[0]
    # divide in half
    first = points[:len(points) // 2]
    second = points[(len(points) // 2):]
    best = abs(max(first) - min(second))

    # recursively find difference between closest pair of points
    firstdiff = recCPairDist(first)
    seconddiff = recCPairDist(second)

    # return the minimum distance between first list, second list, and between the lists
    print(points)
    print(f'f{firstdiff}, s{seconddiff}, b{best}')
    return min(firstdiff, seconddiff, best)


def cPairDist(points):
    """It takes in a list of 1-D points (i.e., integers) and returns the distance between the closest pair
    of points."""
    points.sort() # sort the list
    if len(points) <= 1:  # catch edge cases where the length of the list is 1 or 0
        return 0
    if len(points) == 2:
        return abs(points[0]-points[1]) # catch edge case where length of the list is 2 (recursion sometimes returns min of list)
    else:
        return(recCPairDist(points))


list1 = [.07, 4, 12, 14, 2, 10, 16, 6]

list2 = [7, 4, 12, 14, 2, 10, 16, 5]

list3 = [14, 8, 2, 6, 3, 10, 12]

list4 = [9]

list5 = []

list6 = random.sample(range(10,500), 2)

print(f'one {cPairDist(list1)}')

# print(f'two {cPairDist(list2)}')

# print(f'three {cPairDist(list3)}')

# print(f'four {cPairDist(list4)}')

# print(f'five {cPairDist(list5)}')

# print(sorted(list6))
# print(f'six {cPairDist(list6)}')

# print(recCPairDist(list1))