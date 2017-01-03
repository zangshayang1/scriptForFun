#!/bin/bash/python
#encoding: utf-8

import sys

class Calculator(object):
    def __init__(self, user_input):
        self.user_input = user_input
    
    def _precedence(self, operator):
        if operator == '+' or operator == '-':
            return 1
        elif operator == '*' or operator == '/':
            return 2
        elif operator == '^':
            return 3
        else:
            raise Exception("Wrong operator.")
    
    def _simpleCalc(self, num1, num2, operator):
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            return num1 / num2
        elif operator == '^':
            return num1 ** num2
        else:
            raise Exception("Wrong operator2.")

    def calc(self):
        if len(self.user_input) == 0:
            raise Exception("Wrong Input.")
        print self.user_input
        num_stack = []
        operator_stack = []

        for c in self.user_input:
            if ord('0') <= ord(c) <= ord('9'):
                num_stack.append(int(c))
            else:
                if len(operator_stack) == 0:
                    operator_stack.append(c)
                    continue

                if self._precedence(c) >= self._precedence(operator_stack[-1]):
                    operator_stack.append(c)
                else:
                    prev_operator = operator_stack.pop(-1)
                    last_num = num_stack.pop(-1)
                    seclast_num = num_stack.pop(-1)
                    result = self._simpleCalc(seclast_num, last_num, prev_operator)
                    operator_stack.append(c)
                    num_stack.append(result)

        # after user_input runs out
        while len(operator_stack) > 0:
            operator = operator_stack.pop(-1)
            last_num = num_stack.pop(-1)
            seclast_num = num_stack.pop(-1)
            result = self._simpleCalc(seclast_num, last_num, operator)
            num_stack.append(result)
        # in the end there ought to be only one last number left in stack
        return num_stack[-1]

myCalc = Calculator(sys.argv[1])
print myCalc.calc()
