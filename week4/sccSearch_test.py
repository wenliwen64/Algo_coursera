#!/usr/bin/env python
import sys
import resource
t = -1 
s = 0  

def DFS(elist, i, ft, bk_explore, leader):
    global s
    global t
    bk_explore[i] = 1
    leader[i] = s
    for edge in [y for y in elist if y[0] == i]:
        #print edge[1], bk_explore[edge[1]]
        if bk_explore[edge[1]] == 0:
	    DFS(elist, edge[1], ft, bk_explore, leader) 
    t = t + 1
    ft[i] = t
    print i 
    print t 
    
def DFS_loop(elist, kVtx, ft, bk_explore, leader):
    i = kVtx - 1 
    while i > -1:
        if i%10 == 0:
            print "%d out of total events kVtx done"%i 
        #print "bk_exp = "
        #print bk_explore
        #print "leader = "
        #print leader
        if bk_explore[i] == 0:
            global s
            s = i
            DFS(elist, i, ft, bk_explore, leader) 
        i = i - 1

def main():
    #sys.setrecursionlimit(10**6)
    #resource.setrlimit(resource.RLIMIT_STACK, (2**29, 2**30))
    #infile = open("./SCC.txt")
    infile = open("./test.txt")
    alist = infile.readlines()
    graph = []
    for line in alist:
        #print line
        newline = line.split(' ') 
        newline = [int(x) for x in newline[:-1]] 
        graph.append(newline)
    
    # -1
    graph = [[x[0]-1, x[1]-1] for x in graph] 
    rev_graph = [[x[1], x[0]] for x in graph] 
    #print rev_graph
    kVtx = len(set([x[0] for x in graph] + [x[1] for x in graph]))

    ft = [-1 for x in range(kVtx)]
    bk_explore = [0 for x in range(kVtx)]
    leader = [-1 for x in range(kVtx)]
    DFS_loop(rev_graph, kVtx, ft, bk_explore, leader)
    #print ft
    #relabel the graph 
    #print "kVtx=%d"%kVtx
    #print "len = %d"%len(graph)
    for i in range(len(graph)):
        graph[i][0] = ft[graph[i][0]]
        graph[i][1] = ft[graph[i][1]]

    del bk_explore[:]
    bk_explore = [0 for x in range(kVtx)]
    #print graph
    #print bk_explore
    DFS_loop(graph, kVtx, ft, bk_explore, leader)

    kk = []
    for i in range(kVtx):
        kk.append(leader.count(i))

    #print kVtx
    #print rev_graph
    kk.sort(reverse=True)
    print kk[:10]
    #print newlist

if __name__ == "__main__":
    main()
