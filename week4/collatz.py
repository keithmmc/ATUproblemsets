def collatz(n):
    while n != 1:
        print(n, end = " ")
        if n & 1:
            n = 3 * n +1 
            
