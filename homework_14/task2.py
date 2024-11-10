def midpoint(x1, y1, x2, y2):
    return ((x1 + x2) / 2 , (y1 + y2) / 2)


if __name__=='__main__':
    print(midpoint(5,10,7,14),type(midpoint(5,10,7,14)))
    print(midpoint(-8,10,16,-11),type(midpoint(0,0,19,150)))
    print(midpoint(-78,1,159,0),type(midpoint(85,2,5,15)))
    
    