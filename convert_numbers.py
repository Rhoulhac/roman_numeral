def make_numeral(num):
    """
    Convert an Arabic number to a Roman numeral
    :param num: Arabic number
    :return: Roman numeral
    """

    if num == 0:
        raise Exception('There is no Roman numeral for zero')
    elif num < 0:
        raise Exception('There are no negative Roman numerals')

    # Mapping for a number and it's power of 10 equivalent
    symbol_options = {
        1: {0: 'I', 1: 'X', 2: 'C', 3: 'M'},
        2: {0: 'II', 1: 'XX', 2: 'CC'},
        3: {0: 'III', 1: 'XXX', 2: 'CCC'},
        4: {0: 'IV', 1: 'XL', 2: 'CD'},
        5: {0: 'V', 1: 'L', 2: 'D'},
        6: {0: 'VI', 1: 'LX', 2: 'DC'},
        7: {0: 'VII', 1: 'LXX', 2: 'DCC'},
        8: {0: 'VIII', 1: 'LXXX', 2: 'DCCC'},
        9: {0: 'IX', 1: 'XC', 2: 'CM'},
    }

    num = str(num)
    power_of_ten = len(num) - 1
    numeral = ''
    for digit in num:
        digit = int(digit)
        if digit != 0:
            numeral += symbol_options[digit][power_of_ten]
        power_of_ten -= 1

    return numeral
