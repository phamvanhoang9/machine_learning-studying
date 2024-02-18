"""
You are given container full of water. Container can have limited amount of water. You also have N bottles to fill. You need to find the maximum numbers of bottles you can fill.

Input:
First line contains one integer, T, number of test cases.
Second line of each test case contains two integer, N and X, number of bottles and capacity of the container.
Third line of each test case contains N space separated integers, capacities of bottles.

Output:
For each test case print the maximum number of bottles you can fill.
"""

def max_bottles_filled(test_case):
    results = []

    for case in test_case:
        N, X = case[0], case[1]
        bottle_capacities = case[2]

        assert len(bottle_capacities) == N, "Number of bottle capacity must equal to N"

        bottle_capacities.sort()
        total_bottles_filled = 0
        
        for capacity in bottle_capacities:
            if X >= capacity:
                total_bottles_filled += 1
                X -= capacity

        results.append(total_bottles_filled)

    return results

T = int(input())
test_case = []

for _ in range(T):
    N, X = map(int, input().split())
    capacities = list(map(int, input().split()))
    test_case.append((N, X, capacities))

results = max_bottles_filled(test_case)

for result in results:
    print(result)
