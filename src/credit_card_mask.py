card_number = '4556364607935616'

def hide_digits(cc):
    if len(cc) > 4
        return ''.join(digit.replace(digit, '#') for digit in cc[:len(cc) - 4]) + cc[len(cc)-4:len(cc)]
    else:
        return cc

print(hide_digits(card_number))

