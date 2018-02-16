#!/usr/bin/env python333

# rpn calculators are easier to use because they have a stack
# eg 1 1 + is equal to 1 + 1, 1 1 + 2 * is equal to (1+1) * 2

def calculate(arg): 
    stack = list()

    # range-based for loop: setting value for each token
    for token in arg.split(): 
        try:
            value = int(token)
            stack.append(value)

        # if anything in the try block fails, program jumps to except block
        except ValueError:
            arg1 = stack.pop()
            arg2 = stack.pop()
            return arg1 + arg2
        
def main():
    while True:
        print(calculate(input('rpn calc> ')))

if __name__ == '__main__':
    main()
