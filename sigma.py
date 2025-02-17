# 시간복잡도: 상수 시간 예제.
# O(n)

def sigma(n) -> int:
    sum = 0
    for i in range(n+1): # n+1 잘 기억해두자. 
        sum = sum+i
    return sum

# n이 온 만큼 n만큼 작동함. 

n = int(input())
print(sigma(n))