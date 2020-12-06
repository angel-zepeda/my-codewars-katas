example_number = '1242121243'

def create_phone_number(n):
    a, b, c = n[:3], n[3:6], n[6:10]
    phone_number = '({a}) {b}-{c}'.format(a=''.join(str(x) for x in a), b = ''.join(str(x) for x in b), c = ''.join(str(x) for x in c))
    return phone_number

print(example_number)
