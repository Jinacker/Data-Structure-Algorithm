# 스택 만들기

class Stack: #스택 생성.
    def __init__(self):
        self.items = list()
        
    def push(self, data):
        self.items.append(data)
        
    def pop(self): 
        return self.items.pop()

    def size(self):
        return len(self.items)
    
    def peek(self):
        return self.items[-1]

s1 = Stack()
s1.push(-9)
s1.push(11)
s1.push(123)

print(s1.pop()) # 이거는 아예 마지막 값이 사출됨.
print(s1.peek()) #마지막으로 들어간게 출력.
print(s1.peek())

print(s1.size())

