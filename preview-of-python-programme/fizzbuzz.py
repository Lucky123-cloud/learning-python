def fizzBuzz():
    num = abs(int(input("Enter a number: ")))

    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
    elif num % 3 == 0:
        print("fixzzbuzz")
    elif num % 5 == 0:
        print("buzz")
    else:
        print(num)


fizzBuzz()


    