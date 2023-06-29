from colorama import Fore, Style

class Colorizer:
    def __init__(self, color):
        self.color = color

    def __enter__(self):
        if self.color == 'red':
            print (Fore.RED)
        elif self.color == 'green':
            print(Fore.GREEN)
        elif self.color == 'blue':
            print(Fore.BLUE)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(Style.RESET_ALL)

with Colorizer('red'):
    print('printed in red')
print('printed in default color')
