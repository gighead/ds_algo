#1.  Recursive case
# pick any number , its always the sum of twp preciding numbers in the sequence
# f(n) = f(n-1) + f(n-2)
#2. Base condition
# Unintentional condition


def fibo(n):
    assert n >= 0 and int(n) == n , "n must either be a +int or a whole number"
    if n in [0,1]:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

print(fibo(7))