def main():
    #ex1()
    #ex2()
    ex3()






#Write a Python program that prints all the numbers
# from 0 to 6 except 3 and 6.


# def ex1():
#
#
#     for num in range (7):
#         if(num % 3 == 0 and num != 0):
#             continue
#         else:
#             print(num)
#
#
#




#Write a Python program to count the number of
# even and odd numbers from a series of numbers.


# def ex2():
#
#     numlist = [1 ,2, 3, 4, 5, 6, 7, 8, 9, 10]
#
#     evenonly = [num for num in numlist if num % 2 == 0]
#     print("Number of even numbers: " + str(len(evenonly)))
#     oddonly = [num for num in numlist if num % 2 != 0]
#     print("Number of odd numbers: " + str(len(oddonly)))








#Write a Python program that accepts a sequence of lines
# (blank line to terminate) as input and prints the
# lines as output after User enters a blank line to end.


def ex3():

    while True:
        userblank = input("Enter a line")
        print(userblank, end='.')

        if userblank == "":
            break

































if __name__ == '__main__':
    main()