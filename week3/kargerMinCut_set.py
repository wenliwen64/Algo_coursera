#!/usr/bin/env python
import random
import copy
#replace tail with head in adjacent list
def contraction(alist, head, tail):
    vertices = [x[0] for x in alist]
    ind_head = vertices.index(head)
    ind_tail = vertices.index(tail)
    #loop over the related rows
    for x in set(alist[ind_tail]):
        ind_x = vertices.index(x)
        for y in alist[ind_x]:
            if y == tail:
                ind_y = alist[ind_x].index(y)   
                alist[ind_x][ind_y] = head
    #print len(alist)
    alist[ind_head] = [head] + [y for y in alist[ind_head][1:] if y!=head] + [x for x in alist[ind_tail] if x!=head]
    alist.pop(ind_tail)

def kargerMinCut(ad_list): 
    if len(ad_list) > 2:
        edgelist = []
        vertices = [x[0] for x in ad_list]

        for line in ad_list:
            for x in line[1:]:
                edgelist.append([line[0], x])

        #print "edgelist"
        #print edgelist
        pick_pair = edgelist[int(random.random()*len(edgelist))] #? check
        head = pick_pair[0]
        tail = pick_pair[1]
        
        #replace tail with head
        #print "head %d" %head
        #print "tail %d" %tail
        contraction(ad_list, head, tail)
        #merge tail to head

        #ind_head = vertices.index(pick_pair[0])
        #ind_tail = vertices.index(pick_pair[1])

        #ad_list[ind_head].remove(pick_pair[1])
        #ad_list[ind_tail].remove(pick_pair[0])
        #ad_list[ind_head].append(ad_list[ind_tail][1:])
        #ad_list.pop(ind_tail)
        #print ad_list
        return  kargerMinCut(ad_list) 
    else:
        #print ad_list
        return [len(ad_list[0])-1]#, len(ad_list[1])-1]
     
def getAdList(infile):
    newlist = []
    alist = infile.readlines()
    for line in alist:
        newline = line.split('\t')
        newline = [int(x) for x in newline[:-1]]
        newlist.append(newline)
    return newlist  

def main():
    infile = open("./kargerMinCut.txt")
    alist = infile.readlines()
    newlist = []
    edgelist = []
    for line in alist:
        newline = line.split('\t')
        newline = [int(x) for x in newline[:-1]]
        newlist.append(newline)
        for x in newline[1:]:
            edgelist.append([newline[0], x])
    #print edgelist[1] 
    #print newlist[199]
    #print len(edgelist)/2
    test_alist = [[1, 2, 3, 4], [2, 1, 3, 4], [3, 1, 2, 4], [4, 1, 2, 3]]
    #kk = kargerMinCut(newlist)
    kk = []
    iterations = 200
    for i in range(iterations):
        if i%10 == 0:
            print "%d out of %d" %(i, iterations)
        #tmplist = copy.deepcopy(test_alist)
        #tmplist = copy.deepcopy(newlist)
        tmplist = [x[:] for x in newlist]
        #print tmplist
        #print (tmplist, test_alist) 
        kk.append(kargerMinCut(tmplist))
  
    print kk 
    print min(kk)
    #kargerMinCut(newlist, len(newlist), len(edgelist)/2)
            
        

if __name__ == "__main__":
    main();
