#!/usr/bin/env python3


import sys


def getData(f):
    """Function to read results and student numbers from a given file"""
    results = []
    for line in f:
        number, mark = line.strip().split()
        results.append( [number, int(mark)] )
    return results

def thoseInRange(data, lower, upper):
    """Function to determine which students have marks in the given ranges"""
    students = []
    for [number, mark] in data:
        if lower <= mark <= upper:
            if number not in students:
                students.append(number)
    if len(students) == 0: students = ["None"]
    return students


def showRanges(data):
    """function to display the sorted result of students and ranges onto the console"""
    lower = boundaries[0]
    for upper in boundaries[1:]:
        candidates = thoseInRange(data,lower,upper)
        candidates.sort()
        print("Between %s and %s"%(lower,upper))
        for student in candidates:
            print("  "+student)
        lower=upper+1

#def initClasify():
#    fname = open("marks.dat")
#    boundaries = [0,49,59,69,74,100]
#    data = getData(fname)

if __name__ == '__main__':

    fname = open(sys.argv[1])
    boundaries = list(map(int, sys.argv[2:]))

    data = getData(fname)
    showRanges(data)




