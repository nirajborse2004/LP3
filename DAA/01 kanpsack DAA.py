def knapsack(weights, values, capacity):
    n = len(weights)

    # Create DP table
    dp = []
    for i in range(n + 1):
        dp.append([0] * (capacity + 1))

    # Fill DP table
    for i in range(n + 1):
        for j in range(capacity + 1):

            if i == 0 or j == 0:
                dp[i][j] = 0

            elif weights[i-1] <= j:
                dp[i][j] = max(
                    dp[i-1][j],
                    dp[i-1][j-weights[i-1]] + values[i-1]
                )

            else:
                dp[i][j] = dp[i-1][j]

    # Find selected items
    selected = []
    j = capacity

    for i in range(n, 0, -1):
        if dp[i][j] != dp[i-1][j]:
            selected.append(i-1)
            j = j - weights[i-1]

    return dp[n][capacity], selected


# Input
weights = list(map(int, input("Enter weights: ").split()))
values = list(map(int, input("Enter values: ").split()))
capacity = int(input("Enter capacity: "))

max_value, selected = knapsack(weights, values, capacity)

print("Maximum value that can be obtained:", max_value)
print("Selected item indices:", selected[::-1])
