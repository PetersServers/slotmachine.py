
def print_machine(symbols, text):
    '''
    Todo
    '''


def _print_top():
    print("+------------+")
    print("|            |")
    print("|            |")
    print("+------------+")
def _print_slots(symbols):
    for symbol in symbols:
        print(f"[{symbol}]", end=" ")
    print()
