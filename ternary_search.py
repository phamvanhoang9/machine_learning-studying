"""
Finding Mimo:

You have been given an Unimodal function:

f(x) = 2x^2 - 12x + 7

with N intervals. For each interval you will be given two integer values l and r , where l < r
and you need to find the minimum value of f(x)
where x will be in the range [l, r] (both inclusive).

Input:
The first line will consists of one integer N denoting the number of intervals.
In next N lines, each line contains 2 space separated integers, l and r denoting the range of interval.

Output:
Print N lines, where i_th line denotes the minimum value of f(x)
, where x will be in range [li, ri].

Constraints:

1 <= N <= 10^5
-10^6 <= l <= r <= 10^6
"""

# from typing import List

# def calc(x: int) -> int:
#     return 2*x**2 - 12*x + 7

# def interval_calc(l: int, r: int) -> List[int]:
#     out = []
#     while l <= r:
#         x = l
#         result = calc(x)
#         out.append(result)
#         l += 1

#     out.sort()

#     return out

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

N = int(input())
intervals = [list(map(int, input().split())) for _ in range(N)] # [[l, r], [l, r], ...]

results = find_min_val(N, intervals)
for result in results:
    print(result)


# if __name__ == "__main__":
#     print(min(interval_calc(2, 5)))


# def ternary_search(arr: List[int], )