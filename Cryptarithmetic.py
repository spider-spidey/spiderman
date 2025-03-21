from itertools import permutations

def is_valid(s, m, e, n, d, o, r, y):
    send = s * 1000 + e * 100 + n * 10 + d
    more = m * 1000 + o * 100 + r * 10 + e
    money = m * 10000 + o * 1000 + n * 100 + e * 10 + y
    return send + more == money

def solve_cryptarithmetic():
    letters = 'SENDMORY'
    for perm in permutations(range(10), 8):
        s, e, n, d, m, o, r, y = perm
        if s != 0 and m != 0 and is_valid(s, m, e, n, d, o, r, y):
            print(f"{s}{e}{n}{d} + {m}{o}{r}{e} = {m}{o}{n}{e}{y}")

solve_cryptarithmetic()
