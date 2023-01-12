"""
<confirmation>
    Do not modify this header, but only the checkbox mark.
    I confirm that I solved the exercises on my own, and I am able to present my solution:
    Yes [ ]    No [x]
</confirmation>
"""
from slot_machine import SlotMachine
from printer import Printer

def main():
    machine = SlotMachine()
    printer = Printer()
    while True:
        bet = int(input('Enter your bet: '))
        symbols, text = machine.play(bet)
        printer.print_machine(symbols, text)
        if machine.wins >= 2 and machine.losses >= 5:
            print('You lost all your money')
            break

if __name__ == '__main__':
    main()

