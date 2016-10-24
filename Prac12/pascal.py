def pascal(n):
    if n <= 0:
        return 0
    else:
        return n + pascal(n-1)

print(pascal(6))