
def int_to_roman(number):
    if not 0 < number < 4000:
        raise ValueError("Argument must be between 1 and 3999")
    ints_nums = {
        1000: 'M', 900: 'CM',  500: 'D', 400: 'CD', 100: 'C',  90: 'XC', 50: 'L',  40: 'XL',
        10: 'X',  9: 'IX',   5: 'V', 4: 'IV', 1: 'I'
    }
    result = []
    for i in ints_nums.keys():
        count = int(number / i)
        result.append(ints_nums.get(i) * count)
        number -= i * count
    return ''.join(result)
