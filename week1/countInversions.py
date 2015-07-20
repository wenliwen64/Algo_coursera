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

def countSplitInversions(lefthalf, righthalf):
    i = 0
    j = 0
    k = 0
    while i < len(lefthalf):
        if lefthalf[i] > righthalf[j]:
            k = k + len(righthalf) - j;
            i = i + 1;
        else:
            j = j + 1;
    return k  
    
def countInversions(alist):
    if len(alist) > 1: 
        mid = len(alist)/2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        a = countInversions(lefthalf)
        #print lefthalf 
        #print a  
        b = countInversions(righthalf)
        #print righthalf
        #print b
        i = 0
	j = 0
	k = 0
        ci = 0
	while i < len(lefthalf)  and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]; 
                i = i + 1
                ci = ci + j  
            else:
                alist[k] = righthalf[j];
                j = j + 1
            k = k + 1

        #if i < len(lefthalf) - 1:
        #    ci = ci + len(righthalf)*(len(lefthalf) - i - 1) 

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
	    i = i + 1
	    k = k + 1
            ci = ci + j

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1

	return a + b + ci 
    else:
        return 0

def main():
    infile = open("./IntegerArray.txt")
    alist = infile.readlines()
    alist = [int(x[:-2]) for x in alist]
    b = alist[:5]
    test = [1, 2, 3, 4, 5]
    test2 = [6, 5, 4, 3, 2, 1]
    print b 
    no = countInversions(alist)
    print no
    #print "=========="
    #print no
    #print "=========="
    #print countInversions(test2) 

if __name__ == "__main__":
    main();
