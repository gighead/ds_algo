#Sum of digits
# 10 = 1
# 120 = 122 % 10 => 12,2 => 12/10 => 1,2,2


def sumofDigits(n):
    assert n >= 0 and int(n) == n, 'n must be positive and a whole number'
    if n == 0:
        return 0
    else:
        return int(n%10) + sumofDigits(int(n//10))


print(sumofDigits(1111111111111111111))