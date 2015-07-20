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


def partition(alist, l, r):
    #print "l, r = "
    #print l, r
    dist = int((r - l)/2)
   
    candidates = [alist[l], alist[l+dist], alist[r]]
    mergeSort(candidates)
    pivot = candidates[1] 

    print pivot
    if alist[l] == pivot:
	alist[l] = pivot
        print l
    elif alist[l+dist] == pivot:
        alist[l+dist] = alist[l]
        alist[l] = pivot
        print l+dist
    else:
        alist[r] = alist[l]
        alist[l] = pivot 
        print r

    i = l + 1
    j = i
    while j < r+1:
        if alist[j] < pivot:
            tmp = alist[j] 
            alist[j] = alist[i] 
            alist[i] = tmp
            i = i + 1
            j = j + 1
        else:
            j = j + 1

    #print "i, j = "
    #print  i, j
    tmp = pivot  
    alist[l] = alist[i-1]
    alist[i-1] = tmp
    #print "alist = "
    #print alist
    return [l, i-2, i, r]

def quickSort(alist, l, r, count):
    n = r-l+1
    #print "n = "
    #print n
    if n <= 1:
        return 
    else:
        pos_pair = partition(alist, l, r)
        #print "r-l"
        #print r-l
        count[0] = count[0] + r - l
        #count = count + r - l
        #print alist 
        #print "pos_pair = "
        #print  pos_pair
        
        #print "count = "
        #print count[0] 
        #print count 
        quickSort(alist, pos_pair[0], pos_pair[1], count)
        quickSort(alist, pos_pair[2], pos_pair[3], count)


def main():
    alist = [int(a[:-2]) for a in open("./QuickSort.txt")]
    #temp = [2, 4, 3, 100, 5, 7, 9, 6] 
    #temp = alist[:5]
    temp = [1, 4, 6, 5, 2, 3]
    count = [0]
    #count = 0
    #k = partition(temp, 3, 7)
    print temp
    #quickSort(temp, 0, len(temp)-1, count)
    quickSort(alist, 0, len(alist)-1, count)
    #print k 
    print temp, count[0]
    print count
 
if __name__ == "__main__":
    main()
