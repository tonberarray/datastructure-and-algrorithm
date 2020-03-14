# 中缀表达式转后缀表达式

# 中缀表达式转后缀表达式的规则：

# 1.遇到操作数，直接输出； 
# 2.栈为空时，遇到运算符，入栈； 
# 3.遇到左括号，将其入栈； 
# 4.遇到右括号，执行出栈操作，并将出栈的元素输出，直到弹出栈的是左括号，左括号不输出； 
# 5.遇到其他运算符’+”-”*”/’时，弹出所有优先级大于或等于该运算符的栈顶元素，然后将该运算符入栈； 
# 6.最终将栈中的元素依次出栈，输出。 
# 经过上面的步骤，得到的输出既是转换得到的后缀表达式。 


# 代码实现：

# 复制代码
expression = "3+(6*7-2)+2*3"

def middle2behind(expresssion):  
    result = []             # 结果列表
    stack = []              # 栈
    for item in expression: 
        if item.isnumeric():    # isdigint() # 如果当前字符为数字那么直接放入结果列表
            result.append(item) 
        else:                     # 如果当前字符为一切其他操作符
            if len(stack) == 0:   # 如果栈空，直接入栈
                stack.append(item)
            elif item == '(':   # 如果当前字符为*/（，直接入栈
                stack.append(item)
            elif item == ')':     # 如果右括号则全部弹出（碰到左括号停止）
                t = stack.pop()
                while t != '(':   
                    result.append(t)
                    t = stack.pop()
            # 如果当前字符为加减且栈顶为乘除，则开始弹出
            elif item in '+-' and stack[len(stack)-1] in '*/':
                if stack.count('(') == 0:        # 如果没有左括号，弹出所有     
                    while stack:
                        result.append(stack.pop())
                else:                               # 如果有左括号，弹到左括号为止  
                    t = stack.pop()  
                    while t != '(':
                        result.append(t)
                        t = stack.pop()
                    stack.append('(')
                stack.append(item)  # 弹出操作完成后将‘+-’入栈
            else:
                stack.append(item)# 其余情况直接入栈（如当前字符为+，栈顶为+-）

    # 表达式遍历完了，但是栈中还有操作符不满足弹出条件，把栈中的东西全部弹出
    while stack:
        result.append(stack.pop())
    # 返回字符串
    return ",".join(result)


print(middle2behind(expression))