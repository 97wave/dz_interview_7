pairs = {'{' : '}',
        '[' : ']',
        '(' : ')',
        '}' : '{',
        ']' : '[',
        ')' : '('
        }

class Stack:

    def __init__(self):
        self.stack = []
        self.stack_size = 0

    def size(self, items=0):
        self.stack_size += items
        return self.stack_size

    def is_empty(self):
        return not bool(self.size())

    def push(self, element):
        if type(element) in (int, float):
            self.stack.append(element)
        else:
            for item in element:
                self.stack.append(item)  
        self.size(len(element))

    def pop(self):
        if self.size() > 0:
            self.size(-1)
            return self.stack.pop()

    def peek(self):
        if  self.size() > 0:
            return self.stack[self.size() - 1]


def is_balanse(stack, tmp):
    if  stack.size() % 2 != 0 or stack.peek() in ['{', '(', '[']:
        return 'Несбалансированно'

    else:
        while not stack.is_empty():
            if tmp.peek() == pairs[stack.peek()]:
                stack.pop()
                tmp.pop()
            else:
                tmp.push(stack.pop())
                
        if stack.is_empty() == tmp.is_empty() == True:
            return "Сбалансированно"
        else:
            return "Несбалансированно" 


strings = {
1 : '(((([{}]))))',
2 : '[([])((([[[]]])))]{()}',
3 : '{{[()]}}',
4 : '}{}',
5 : '{{[(])]}}',
6 : '[[{())}]'
}

stack_object = Stack()
stack_tmp = Stack()

input_ = strings[int(input())]
stack_object.push(input_)
print(input_)

print(is_balanse(stack_object, stack_tmp))