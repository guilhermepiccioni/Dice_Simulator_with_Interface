# Simulator dado

# Simulate the use of a dice, generating a value from 1 to 6

import random


class SimulatorDado:

    def __init__(self):
        self.value_min = 1
        self.value_max = 6
        self.message = 'Would you like to generate a new value for the dado? '

    def start(self):
        answer = input(self.message)
        try:
            if answer == 'Yes' or answer == 'y':
                self.generate_value_dado()
            elif answer == 'Not' or answer == 'n':
                print('Thank you for your participation.')
            else:
                print('Please, write yes or not')
        except:
            print('There was an error receiving your reply!')

    def generate_value_dado(self):
        print(random.randint(self.value_min, self.value_max))


simulator = SimulatorDado()
simulator.start()
