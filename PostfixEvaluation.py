from stackLS import Stack
from InfixToPostfix import infixToPostfix

def EvaPostFixExpression(expression):
    st = Stack()
    operators = '+-/*^'
    tokens = expression.split()
    print("after using split!")
    print(tokens)

    for token in tokens:
        if token.isdigit():
            st.push(int(token))
        elif token in operators:
            b = st.pop()
            a = st.pop()
            if token == '+':
                st.push(a + b)
            elif token == '-':
                st.push(a - b)
            elif token == '*':
                st.push(a * b)
            elif token == '/':
                st.push(a / b)
            elif token == '^':
                st.push(a ** b)
        else:
            raise ValueError(f"Invalid token: {token}")

    return st.pop()


expr1 = "10+100/10+20"
expr2 = "( A + B ) * C"
postfix1 = infixToPostfix(expr1)
print("Postfix:", postfix1)
print("Result:", EvaPostFixExpression(postfix1))

