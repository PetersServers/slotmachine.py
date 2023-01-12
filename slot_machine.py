def lever(commitment):
    '''
    Todo
    '''
    
import random

SYMBOLS = ('A', 'B', 'C', 'D', 'E')

def _get_symbol():
    return random.choice(SYMBOLS)
    
def _get_different_symbols():
    symbol1 = _get_symbol()
    symbol2 = _get_symbol()
    symbol3 = _get_symbol()
    while symbol1 == symbol2 == symbol3:
        symbol1 = _get_symbol()
        symbol2 = _get_symbol()
        symbol3 = _get_symbol()
    return (symbol1, symbol2, symbol3)
