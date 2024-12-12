class ExtendedList(list):
    def min(self):
        if not self:
            raise ValueError("min() arg is an empty sequence")
        return min(self)

    def max(self):
        if not self:
            raise ValueError("max() arg is an empty sequence")
        return max(self)

if __name__ == "__main__":
    num1 = ExtendedList([10, 20, 30, 5, 40])
    num2 = ExtendedList([-1, -10, 0, 3, 8])
    empty_list = ExtendedList()

    print("List 1:", num1)
    print("Minimum:", num1.min())  
    print("Maximum:", num1.max())  

    print("\nList 2:", num2)
    print("Minimum:", num2.min())  
    print("Maximum:", num2.max())  

    print("\nEmpty List:", empty_list)
    try:
        print("Minimum:", empty_list.min())
    except ValueError as e:
        print("Error:", e)

    try:
        print("Maximum:", empty_list.max())
    except ValueError as e:
        print("Error:", e)