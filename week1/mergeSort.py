#!/usr/bin/env python 
def mergeSort(alist):
    if len(alist) > 1: 
        mid = len(alist)/2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf)  and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]; 
                i = i + 1
            else:
                alist[k] = righthalf[j];
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
	    i = i + 1
	    k = k + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1

def main():
    infile = open("./IntegerArray.txt")
    alist = infile.readlines()
    alist = [int(x[:-2]) for x in alist]
    b = alist[:10]
    print b 
    mergeSort(b)
    print b 

if __name__ == "__main__":
    main();
