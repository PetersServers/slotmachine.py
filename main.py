"""
<confirmation>
    Do not modify this header, but only the checkbox mark.
    I confirm that I solved the exercises on my own, and I am able to present my solution:
    Yes [ ]    No []
</confirmation>
"""

# Uncomment for working in PyCharm
# import slot_machine, printer

# Uncomment for testing in Artemis
from assignment import slot_machine, printer

def pull_lever(commitment):
    profit, symbols = slot_machine.lever(commitment)
    if profit > 0:
        printer.print_machine(symbols, 'U WON ' + str(profit) + '$')
    else:
        printer.print_machine(symbols, 'U LOST ' + str(commitment) + '$')
    return profit


def insert_coin(money):
    print('How much you want to insert (5, 10, 20)')
    commitment = int(input('0 to quit: '))
    """
    TODO
    """


def main(user_name, money):
    print('Welcome', user_name, 'you have', money, 'coins')
    while money >= 5:
        money += insert_coin(money)
        print('You have now', money, '$')
    print('You are out of money!')


if __name__ == "__main__":
    main('Heisenberg', 100)