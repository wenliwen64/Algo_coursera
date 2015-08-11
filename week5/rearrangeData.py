#!/usr/bin/env python
def main():
    infile = open('dijkstraData.txt', 'r'); 
    ofile = open('new_dijkstraData.txt', 'w');
    alist = infile.readlines();
    for line in alist:
        newline = line.split('\t')
        head = newline[0];
        print head, newline
        for subline in newline[1:-1]:
            newsubline = subline.split(',')
            print newsubline[0], newsubline[1]
            ofile.write(''.join([head, ' ', newsubline[0], ' ', newsubline[1], '\n'])) 
    infile.close()
    ofile.close();
     
if __name__ == "__main__":
    main();
