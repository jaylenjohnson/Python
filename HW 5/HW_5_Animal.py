class Animal:
    
    def __init__(self, kind):
        # a name of an animal
        self.name = kind
        # generate a list of hints for given animal
        if   kind == 'elephant':
            self.hints = ['I have exceptional memory', 
                          'I am the largest land-living mammal in the world', 
                          'I have a trunk and big ears']
        elif kind == 'tiger':
            self.hints = ['I am the biggest cat', 
                          'I come in black and white or orange and black', 
                          'I am not a lion']
        elif kind == 'bat':
            self.hints = ['I use echo-location', 
                          'I can fly', 
                          'I see well in dark']
        
    def guess_who_am_i(self):
        print('I will give you 3 hints, guess what animal I am\n')
        # give at most 3 hints
        for i in range(3):
            # print a hint
            print(self.hints[i])
            # get the answer from user
            answer = input('Who am I?:')
            # check if answer is correct
            if answer == self.name:
                # answer is correct
                print('You got it! I am {}\n'.format(self.name))
                # exit loop (no need to print other hints)
                break
            else:
                # answer is not correct
                print('Nope, try again!\n')
                
        else:
            # no correct answer after 3 hints
            print("I'm out of hints! The answer is: {}\n".format(self.name))
            
            
def main():

    e = Animal("elephant")
    t = Animal("tiger")
    b = Animal("bat")

    e.guess_who_am_i()
    t.guess_who_am_i()
    b.guess_who_am_i()        
    
    
main()    