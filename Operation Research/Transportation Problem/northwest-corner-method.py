"""
Transportation Problem - Northwest Corner Method
Author: [DF Tow]
Date: 2025-06-01
License: MIT (see LICENSE file)
"""
def northwest_corner_method(supply, demand, cost_matrix):
    supply_copy = supply.copy()
    demand_copy = demand.copy()

    allocation = [[0 for _ in range(len(demand))] for _ in range(len(supply))]

    i, j = 0, 0
    total_cost = 0
    steps = []

    while i < len(supply) and j < len(demand):
        allocation_amount = min(supply_copy[i], demand_copy[j])
        allocation[i][j] = allocation_amount

        cost = allocation_amount * cost_matrix[i][j]
        total_cost += cost

        steps.append(f"Step {len(steps)+1}: Allocate {allocation_amount} units from {sources[i]} to {destinations[j]} at cost RM{cost_matrix[i][j]}/unit = RM{cost}")
        supply_copy[i] -= allocation_amount
        demand_copy[j] -= allocation_amount

        if supply_copy[i] == 0 and demand_copy[j] == 0:
            i += 1
            j += 1
        elif supply_copy[i] == 0:
            i += 1
        else:
            j += 1

    return allocation, total_cost, steps

allocation, total_cost, steps = northwest_corner_method(supply, demand, cost_matrix)
for step in steps:
    print(step)

print("\n\nAllocation Table:")
allocation_df = pd.DataFrame(allocation, index=sources, columns=destinations)
print(allocation_df)

print("\nVerification:")
for i, source in enumerate(sources):
    allocated = sum(allocation[i])
    print(f"{source}: Allocated {allocated}/{supply[i]} units")

for j, destination in enumerate(destinations):
    allocated = sum(allocation[i][j] for i in range(len(sources)))
    print(f"{destination}: Received {allocated}/{demand[j]} units")

print(f"\nFinal Results:")
print(f"Total Transportation Cost: RM {total_cost}")

print("\nCost Breakdown:")
for i in range(len(sources)):
    for j in range(len(destinations)):
        if allocation[i][j] > 0:
            cost = allocation[i][j] * cost_matrix[i][j]
            print(f"{sources[i]} → {destinations[j]}: {allocation[i][j]} units × RM{cost_matrix[i][j]} = RM{cost}")
