import random
def main():
     a = [[1, 2, 3], [4, 5, 66 ]]
     i = 0
     count_0 = 0;
     count_1 = 0;
     count_2 = 0;
     while i < 100000:
         k = int(random.random()*len(a[1]))
         if k == 0:
             count_0 = count_0 + 1 
	 if k == 1:
             count_1 = count_1 + 1 
         if k == 2:
             count_2 = count_2 + 1 
         i = i + 1

     print count_0, count_1, count_2

if __name__ == "__main__":
    main()
