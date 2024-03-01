
def f(x):
    return 2*x**2 - 12*x + 7

def ternary_search(l, r):
    epsilon = 1e-9

    while r - l > epsilon:
        m1 = l + (r - l) / 3
        m2 = r - (r - l) / 3

        if f(m1) < f(m2):
            r = m2
        else:
            l = m1

    return f(l)

def find_min_val(N, intervals):
    results = []
    for i in range(N):
        l, r = intervals[i]
        min_val = ternary_search(l, r)
        results.append(min_val)

    return results

if __name__ == '__main__':
    print("Enter N intervals:")
    N = int(input())
    print("Let's give the intervals:")
    intervals = [list(map(int, input().split())) for _ in range(N)]

    results = find_min_val(N, intervals)
    print("Min value for each interval is:")
    for result in results:
        print(f"{result:.2f}")
