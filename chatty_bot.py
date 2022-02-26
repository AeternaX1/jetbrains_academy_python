def greet(bot_name, birth_year):
    print('\nHello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('\nPlease, remind me of your name.')
    name = input()
    print('\nWhat a great name you have, ' + name + '!')


def guess_age():
    print('\nLet me guess your age.')
    print('Enter the remainders of dividing your age by 3, 5 and 7.')
    print('Eg: If you are 24:')
    print('Number 1 will equal the result of 24 divided by 3, which has no remainder, so enter 0')
    print('Number 2 will equal the result of 24 divided by 5, which has a remainder of 4, so we will enter this') 
    print('Number 3 will equal the result of 24 divided by 7, which has a remainder of 3, so we will enter this')

    print("\nEnter first number: ")
    rem3 = int(input())
    print("\nEnter second number: ")
    rem5 = int(input())
    print("\nEnter third number: ")
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("\nYour age is " + str(age) + "; that's a good time to start programming!")


def count():
    print('\nNow I will prove to you that I can count to any number you want.')

    print("Enter number: ")
    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("\nLet's test your programming knowledge.")
    # write your code here
    print("\n1. To repeat a statement multiple times.")
    print("2. To decompose a program into several small subroutines.")
    print("3. To determine the execution time of a program.")
    print("4. To interrupt the execution of a program.")

    print("Enter number: ")
    user_choice = int(input())

    if user_choice == 2:
        print("\nCorrect")
        print('Congratulations, have a nice day!')
    else:
        print("Please, try again.")


def end():
    print('Completed!')


greet('Aid', '2020')
remind_name()
guess_age()
count()
test()
end()
