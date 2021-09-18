# Simulator dado

# Simulate the use of a dice, generating a value from 1 to 6

import random
import PySimpleGUI as sg


class SimulatorDado:

    def __init__(self):
        self.value_min = 1
        self.value_max = 6
        self.message = 'Would you like to generate a new value for the dado? '
        # Layout
        self.layout = [
            [sg.Text('Play a Dado')],
            [sg.Button('Yes'), sg.Button('Not')]
        ]

    def start(self):

        # Create a windows
        self.window = sg.Window('Simulator a Dado', layout=self.layout)

        # Read values this windows
        self.event, self.values = self.window.Read()

        # Make somethings with values
        try:
            if self.event == 'Yes' or self.event == 'y':
                self.generate_value_dado()
            elif self.event == 'Not' or self.event == 'n':
                print('Thank you for your participation.')
            else:
                print('Please, write yes or not')
        except:
            print('There was an error receiving your reply!')

    def generate_value_dado(self):
        print(random.randint(self.value_min, self.value_max))


simulator = SimulatorDado()
simulator.start()
