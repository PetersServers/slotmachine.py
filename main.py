"""
<confirmation>
    Do not modify this header, but only the checkbox mark.
    I confirm that I solved the exercises on my own, and I am able to present my solution:
    Yes [x]    No []
</confirmation>
"""


from assignment import slot_machine, printer

def pull_lever(commitment):
    profit, symbols = slot_machine.lever(commitment)
    if profit > 0:
        printer.print_machine(symbols, 'U WON ' + str(profit) + '$')
    else:
        printer.print_machine(symbols, 'U LOST ' + str(commitment) + '$')
    return profit

class QuitAddiction(Exception):
    pass

def insert_coin(money):
    commitment = int(input("Insert coin (5, 10, 20): "))
    if commitment == 0:
        raise QuitAddiction("User quit the game")
   if commitment > money:
        print("You do not have the money")
        return money
    elif commitment > money:
        print("You do not have the money")
        return money
    elif commitment not in [5, 10, 20]:
        print("Wrong Coin")
        return money
    else:
        profit = pull_lever(commitment)
        return money + profit - commitment



def main(user_name, money):
    print('Welcome', user_name, 'you have', money, 'coins')
    while money >= 5:
        money += insert_coin(money)
        print('You have now', money, '$')
    print('You are out of money!')


if __name__ == "__main__":
    main('Heisenberg', 100)
