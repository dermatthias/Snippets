# infix to postfix algorithm
def in2post(s):
    stack = []
    operator = {'+': 0,
                '-': 0,
                '*': 1,
                '/': 1}
    postfix = ''

    for i in s:
        # if a operator
        if i in operator:
            # check for precedence
            if not stack:
                stack.append(i)
            else:
                # if same or lower precedence, pop() to string, repeat
                while stack and operator[i] <= operator[stack[-1]]:
                        postfix += stack.pop()
                else:
                    # and add the recent operator to the stack
                    stack.append(i)                
            
        # if an operand
        else:
            postfix += i

    # pop the stack until empty
    while stack:
        postfix += stack.pop()

    return postfix

if __name__ == "__main__":
    import sys
    s = sys.stdin.readline()[:-1]
    print in2post(s)
