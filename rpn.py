#!/usr/bin/env python333

# rpn calculators are easier to use because they have a stack
# eg 1 1 + is equal to 1 + 1, 1 1 + 2 * is equal to (1+1) * 2

def calculate(arg): 
    pass

def main():
    while True:
        calculate(input('rpn calc> '))

if __name__ == '__main__':
    main()
