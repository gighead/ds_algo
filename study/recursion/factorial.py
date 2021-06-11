#Step1 : Recursive case - the flow
#  n! = n * (n-1) * (n-2) * ....*2 *1 => n! = n * ( n-1)!

#step 2 : Base case - Stopping criteria!

#step3 : Unintentional case - Constraint



def factorial(n):
    assert n >=0 and int(n) == n, 'The number must be positive int only'
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(10))