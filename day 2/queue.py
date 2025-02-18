# 큐
# 먼저 들어온걸 먼저 처리
# FiFO
# 프론트 // @@@@@ // 리어
# 인큐: 삽입 // 디큐: 삭제
# 예시) 공용 프린터 => 작업 순서대로 출력됨.
class Node: 
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


class queue:
    
    def __init__(self): # 생성자 메서드
        self.front =None
        self.rear = None
        self._size = 0
        
    def enqueue(self, data): # 삽입
        self._size = self._size + 1
        node = Node(data)
        if self.rear is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node
    
    def dequeue(self): # 삭제
        if self.front is None:
            raise IndexError('dequeue from empty queue')
        self._size = self._size - 1
        temp = self.front # backup
        self.front = self.front.next # update
        if self.front is None:
            self.rear = None
        return temp.data
    
    def size(self) -> int: #사이즈
        return self._size
    
if __name__ == "__main__":
    q = queue()
    q.enqueue(7)
    q.enqueue(-11)
    q.enqueue(8)
    print(q.size())
    print(q.dequeue())
    print(q.size())    
    
## 파이썬 내장된 큐 클래스

from queue import Queue

q = Queue()
q.put('a') # enqueue
print(q.qsize())
print(q.get()) # dequeue

# 내장함수 있어서 그냥 이거 쓰면됨.