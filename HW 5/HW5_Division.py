
from random import randrange


def main():

    print('INTEGER DIVISIONS')
    # infinite loop
    while True:
        # generate two random numbers in range 0, 5
        num1 = randrange(0, 5)
        num2 = randrange(0, 5)
        # get user input
        result = input('{}/{}='.format(num1*num2, num1))
        
        # check if result is valid integer
        try:
            # check if result is correct answer
            if int(result) == num2:
                print('CORRECT!')
            else:
                print('INCORRECT!')
        except ValueError:
            print('Please enter Integers Only!')
            
            
main()            
