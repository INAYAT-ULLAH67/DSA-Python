expression = '20+100/500'
nums = []
i = 0
while i < len(expression):
    ch = expression[i]
    
    if ch.isdigit():
        num = ch
        while i + 1 < len(expression) and expression[i+1].isdigit():
            i += 1
            num += expression[i]
        print(num)
        nums.append(num)
    i += 1   #  need this to move forward!
