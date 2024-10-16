n = int(input("Enter the height of the Christmas tree from 1 to 50: "))


count=1

print('Merry Christmas and a Happy New year!')

print(' ' * (n-1) + '*')

for level in range(1,n):
    branch_width = 2 * level + 1
    spaces = n - level - 1
    print(' ' * spaces + '/' * (branch_width//2) + '|' + '\\' * (branch_width//2) )
    count += 1



print(' ' *(count-1) + '|' )
