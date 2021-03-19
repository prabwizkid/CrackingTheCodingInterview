# Given an expression string, write a python program
# to find whether a given string has balanced parentheses or not.


open_list = ["[", "{", "(", "<"]
close_list = ["]", "}", ")", ">"]

# Function to check parentheses
def checkParentheses(myStr):
    stack = []
    for i in myStr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                    (open_list[pos] == stack[len(stack) - 1])):
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False


string = "{[]{()}}"
print(checkParentheses(string))

string = "[{}{})(]"
print(checkParentheses(string))

