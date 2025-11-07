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

    for token in expression:   # iterate character by character
        if token.isalnum():    # operand (single letter/number)
            output.append(token)
        elif token == '(':
            st_k.push(token)
        elif token == ')':
            while not st_k.isEmpty() and st_k.peek() != '(':
                output.append(st_k.pop())
            st_k.pop()  # remove '('
        elif token in operators:  # operator
            while (not st_k.isEmpty() and 
                   precedence(st_k.peek()) >= precedence(token)):
                output.append(st_k.pop())
            st_k.push(token)

    # Pop remaining operators
    while not st_k.isEmpty():
        output.append(st_k.pop())

    return "".join(output)   # no spaces in final postfix

expr1 = "a+b/c+d"
expr2 = "( A + B ) * C"
expr3 = "A + B * C ^ D - E"

print("Infix:", expr1)
print("Postfix:", infixToPostfix(expr1))

print("Infix:", expr2)
print("Postfix:", infixToPostfix(expr2))

print("Infix:", expr3)
print("Postfix:", infixToPostfix(expr3))
