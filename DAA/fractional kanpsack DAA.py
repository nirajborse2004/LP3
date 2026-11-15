#Assingment No. 3: Fractional Knapsack Problem
def fractional_knapsack(weights, values, capacity):
    items = []
    for i in range(len(weights)):
        ratio = values[i] / weights[i]
        items.append((ratio, weights[i], values[i]))
        
    # Sort by highest value/weight ratio
    items.sort(reverse=True)
    
    total_value = 0.0
    remaining_capacity = capacity
    
    print("\nSelected items and fractions:")
    for ratio, weight, value in items:
        if remaining_capacity == 0:
            break
            
        if weight <= remaining_capacity:
            remaining_capacity -= weight
            total_value += value
            print(f"Take full item: weight={weights}, profit={profit}")
        else:
            fraction = remaining_capacity / weight
            total_value += value * fraction
            print(f"Take {fraction*100:.2f}% of item: weight used={remaining_capacity}, value added={value*fraction:.2f}")
            remaining_capacity = 0
    return total_value

# Example usage
weights = []
values = []

n = int(input("Enter number of items: "))

for i in range(n):
    w = int(input("Enter weight: "))
    weights.append(w)

for i in range(n):
    v = int(input("Enter value: "))
    values.append(v)

capacity = int(input("Enter capacity: "))

max_val = fractional_knapsack(weights, values, capacity)

print("Maximum value in knapsack:", max_val)