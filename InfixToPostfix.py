from stackLS import Stack

def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    if op == '^':
        return 3
    return 0

operators = '+-^/*'

def infixToPostfix(expression):
    st_k = Stack()
    output = []
    operators = '+-/*^'

    i = 0
    while i < len(expression):
        ch = expression[i]

        # build the full number and add to the output
        if ch.isdigit():
            num = ch
            while i + 1 < len(expression) and expression[i+1].isdigit():
                i += 1
                num += expression[i]
            print(num)  
            output.append(num)

        elif ch.isalpha():  # variable like a, b, c
            output.append(ch)

        elif ch == '(':
            st_k.push(ch)

        elif ch == ')':
            while not st_k.isEmpty() and st_k.peek() != '(':
                output.append(st_k.pop())
            st_k.pop()

        elif ch in operators:
            while (not st_k.isEmpty() and
                   precedence(st_k.peek()) >= precedence(ch)):
                output.append(st_k.pop())
            st_k.push(ch)

        i += 1

    while not st_k.isEmpty():
        output.append(st_k.pop())
    print(output)

    return " ".join(output)   # space-separated tokens
 

expr1 = "a+b/c+d"
expr2 = "( A + B ) * C"
expr3 = "A + B * C ^ D - E"

print("Infix:", expr1)
print("Postfix:", infixToPostfix(expr1))

print("Infix:", expr2)
print("Postfix:", infixToPostfix(expr2))

print("Infix:", expr3)
print("Postfix:", infixToPostfix(expr3))
