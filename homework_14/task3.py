def fibonaci (n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1
        
if __name__=='__main__':            
    print(tuple(fibonaci(5)))        
    print(tuple(fibonaci(10)))   
    print(tuple(fibonaci(15))) 
    print(tuple(fibonaci(7)))  