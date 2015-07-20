#!/usr/bin/env python
def swap(alist, l, r):
     tmp = alist[l]
     alist[l] = alist[r] 
     alist[r] = tmp
     return [tmp, alist[r], alist[l]]

def main():
    alist = range(10)
    k = swap(alist, 3, 4)
    print alist
    print k

if __name__ == "__main__":
    main()
