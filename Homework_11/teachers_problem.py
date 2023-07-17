# Написати фунцію шо задовільняє наступні тести. (github)

def new_format(string):
    return '{:,}'.format(int(string)).replace(',','.')

assert (new_format("1000000") == "1.000.000")
assert (new_format("100") == "100")
assert (new_format("1000") == "1.000")
assert (new_format("100000") == "100.000")
assert (new_format("10000") == "10.000")
assert (new_format("0") == "0")