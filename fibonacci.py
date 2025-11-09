def fibonacci(n):
    if n<=1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

x=fibonacci(5)
print(x)
def goodfibonacci(n):
    assert n>-1
    if n==0: return (1,0)
    (a,b)=goodfibonacci(n-1)
    return (a+b,a)
y=goodfibonacci(4)
print(y)