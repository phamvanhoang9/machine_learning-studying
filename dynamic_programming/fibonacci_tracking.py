# Find the end fibonacci number

known = {0: 0, 1: 1}

def fibonacci_memo(n):

    if n in known:
        return known[n]
    
    res = fibonacci_memo(n-1) + fibonacci_memo(n-2)
    known[n] = res

    return res

if __name__ == "__main__":
    print(fibonacci_memo(100))