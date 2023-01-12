class Printer:
    def _print_top(self):
        print('+------------+')

    def _print_base(self):
        print('+------------+')

    def _print_slots(self, symbols):
        print('| [{}] [{}] [{}] |'.format(*symbols))

    def _print_text(self, text):
        print('| ' + text + ' |')

    def print_machine(self, symbols, text):
        self._print_top()
        self._print_slots(symbols)
        self._print_text(text)
        self._print_base()
