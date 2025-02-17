# 공간복잡도 예제

memo = dict() # 리스트 써도됨
def fibo(n) -> int:
    if n in memo:
        return memo[n]
    elif n<=1:
        return n
    else:
        memo[n] = fibo(n-2) + fibo(n-1)
        return memo[n]

print(fibo(5))
print(memo)
