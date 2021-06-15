"""Zoe Berling Algorithms Lab 2 Sort Running Times"""
import random
from time import time


def mergeSort(L):
    """
    Divide in half
    Keep track of the smallest element in each sorted half
    Insert the smallest of the two elements into the auxiliary array
    Repeat until done"""
    sort_L = []
    if len(L) < 2:
        return L[:]
    else:
        mid = len(L)//2
        A = mergeSort(L[:mid])
        B = mergeSort(L[mid:])
        i, j = 0, 0
        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                sort_L.append(A[i])
                i += 1
            else:
                sort_L.append(B[j])
                j += 1
        while i < len(A):
            sort_L.append(A[i])
            i += 1
        while j < len(B):
            sort_L.append(B[j])
            j += 1
        return(sort_L)

def insertionSort(L):
    """
    Iterate through the list checking pairs.
    While the first number in the pair is larger than the second, move the second number to the index of the first number
    Repeat with all pairs in the list.
    """
    sort_L = [x for x in L]

    for i in range(1,len(sort_L)):
        key = sort_L[i]
        j = i-1
        while j >= 0 and sort_L[j] > key:
            sort_L[j+1] = sort_L[j]
            j = j-1
        sort_L[j+1] = key

    return sort_L

def bubbleSort(L):
    """Run through all elements from front to back
    at each index, compare index to next value
    if the index is larger, swap values"""
    sort_L = [x for x in L]

    for n in range(len(sort_L)):
        for i in range(len(L)-1):
            key = sort_L[i]
            if sort_L[i] > sort_L[i+1]:
                    sort_L[i] = sort_L[i+1]
                    sort_L[i+1] = key

    return sort_L

n = 10
A = [i for i in range(n)]
random.shuffle(A)

M = mergeSort(A)

I = insertionSort(A)

B = bubbleSort(A)

print(M ,'\n', I, '\n', B) # check sort

n = [x for x in range(100, 5100, 100)]

print(f'N  \t  Merge \t  Insert \t Bubble')
for i in range(len(n)):
    A = [x for x in range(n[i])]
    random.shuffle(A)

    t1 = time()
    M = mergeSort(A)
    t2 = time()
    mtime = round((t2-t1)*1000,1)

    t1 = time()
    I = insertionSort(A)
    t2 = time()
    itime = round((t2 - t1) * 1000, 1)

    t1 = time()
    B = bubbleSort(A)
    t2 = time()
    btime = round((t2 - t1) * 1000, 1)

    print(n[i], '\t', mtime, '\t', itime, '\t', btime, '\t')

