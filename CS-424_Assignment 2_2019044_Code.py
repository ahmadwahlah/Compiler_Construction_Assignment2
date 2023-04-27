#!/usr/bin/env python
# coding: utf-8

# In[ ]:

# In[7]:


# Define the LR(1) parsing table
lr1_table = {
    0: {'id': 's4'},
    1: {'$': 'acc'},
    2: {'-': 'r2', '$': 'r2'},
    3: {'-': 's3', '$': 'r4'},
    4: {'id': 's4'},
    5: {'*': 's2', '-': 'r1', '$': 'r1'},
    6: {'*': 'r3', '-': 'r3', '$': 'r3'}
}

# Define the productions for the grammar
productions = {
    1: ['E', 'T', '-', 'E'],
    2: ['E', 'T'],
    3: ['T', 'F', '*', 'T'],
    4: ['T', 'F'],
    5: ['F', 'id']
}

# Define the LR(1) parser function
def lr1_parser(input_string):
    stack = [0]
    input_list = input_string.split()
    i = 0
    while True:
        state = stack[-1]
        lookahead = input_list[i]
        action = lr1_table[state].get(lookahead)
        if action is None:
            return False
        elif action == 'acc':
            return True
        elif action[0] == 's':
            stack.append(int(action[1:]))
            i += 1
        elif action[0] == 'r':
            prod_num = int(action[1:])
            rhs_len = len(productions[prod_num]) - 1
            for j in range(rhs_len):
                stack.pop()
            state = stack[-1]
            lhs = productions[prod_num][0]
            stack.append(int(lr1_table[state][lhs]))
        else:
            return False

# Test the LR(1) parser with the input string "a b c d"
input_string = "a b c d"
stack = [0]
input_list = input_string.split()
i = 0
print("Stack\t\tInput\t\tOperation")
print("----\t\t-----\t\t---------")
while True:
    state = stack[-1]
    lookahead = input_list[i]
    action = lr1_table[state].get(lookahead)
    if action is None:
        print(stack, "\t\t", input_list[i:], "\t\tError")
        break
    elif action == 'acc':
        print(stack, "\t\t", input_list[i:], "\t\tAccept")
        break
    elif action[0] == 's':
        stack.append(int(action[1:]))
        i += 1
        print(stack, "\t\t", input_list[i:], "\t\tShift", lookahead)
    elif action[0] == 'r':
        prod_num = int(action[1:])
        rhs_len = len(productions[prod_num]) - 1
        for j in range(rhs_len):
            stack.pop()
        state = stack[-1]
        lhs = productions[prod_num][0]
        stack.append(int(lr1_table[state][lhs]))
        print(stack, "\t\t", input_list[i:], "\t\tReduce", productions[prod_num])
    else:
        print(stack, "\t\t", input_list[i:], "\t\tError")
        break








# In[ ]:



