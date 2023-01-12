def print_machine(symbols, text):
    _print_top()
    _print_slots(symbols)
    _print_base()
    _print_text(text)


def _print_top():
    print("+------------+")
    print("|            |")
    print("|            |")
    print("+------------+")
def _print_slots(symbols):
    for symbol in symbols:
        print(f"[{symbol}]", end=" ")
    print()
def _print_text(text):
    print("+------------+")
    print("|  " + text + "  |")
    print("+------------+")

