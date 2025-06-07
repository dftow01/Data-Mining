# Transportation Problem - Northwest Corner Method

```
Author: [DF Tow]
Date: 2025-06-01
License: MIT (see LICENSE file)
```

## Code

```python
def northwest_corner_method(supply, demand, cost_matrix):
    # Part 1: Initialize variables and placeholders
    supply_copy = supply.copy()
    demand_copy = demand.copy()
    
    allocation = [[0 for _ in range(len(demand))] for _ in range(len(supply))]
    
    i, j = 0, 0
    total_cost = 0
    steps = []
    
    # Part 2: NWCM algorithm
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

# Part 3: Implementation and Visualization
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
```

## Algorithm Explanation

### Part 1: Initialize Variables and Placeholders

**Purpose:** Set up the necessary data structures and variables for the algorithm.

1. **Create copies of supply and demand arrays:**
   ```python
   supply_copy = supply.copy()
   demand_copy = demand.copy()
   ```
   - We create copies to avoid modifying the original arrays during the algorithm execution
   - These copies will be decremented as allocations are made

2. **Initialize the allocation matrix:**
   ```python
   allocation = [[0 for _ in range(len(demand))] for _ in range(len(supply))]
   ```
   - Creates a 2D matrix filled with zeros
   - Rows represent suppliers (sources)
   - Columns represent customers (destinations)
   - Each cell [i][j] will store the allocation from supplier i to customer j

3. **Initialize tracking variables:**
   - `i, j = 0, 0`: Starting position (northwest corner)
   - `total_cost = 0`: Accumulates the total transportation cost
   - `steps = []`: Records each allocation step for visualization

### Part 2: Northwest Corner Method Algorithm

**Purpose:** Systematically allocate supply to demand starting from the northwest corner.

**Core Logic:**

1. **Main Loop:**
   ```python
   while i < len(supply) and j < len(demand):
   ```
   - Continues until all supplies are allocated or all demands are satisfied
   - Ensures we don't go beyond the matrix boundaries

2. **Determine Allocation Amount:**
   ```python
   allocation_amount = min(supply_copy[i], demand_copy[j])
   ```
   - Takes the minimum between current supplier's remaining supply and current customer's remaining demand
   - This ensures we don't over-allocate or under-satisfy

3. **Make the Allocation:**
   ```python
   allocation[i][j] = allocation_amount
   cost = allocation_amount * cost_matrix[i][j]
   total_cost += cost
   ```
   - Records the allocation in the matrix
   - Calculates the cost for this allocation
   - Adds to the running total cost

4. **Update Supply and Demand:**
   ```python
   supply_copy[i] -= allocation_amount
   demand_copy[j] -= allocation_amount
   ```
   - Reduces the supplier's remaining capacity
   - Reduces the customer's remaining demand

5. **Movement Logic:**
   ```python
   if supply_copy[i] == 0 and demand_copy[j] == 0:
       i += 1  # Move to next supplier
       j += 1  # Move to next customer
   elif supply_copy[i] == 0:
       i += 1  # Move to next supplier (current one exhausted)
   else:
       j += 1  # Move to next customer (current one satisfied)
   ```
   
   **Movement Rules:**
   - **Diagonal move (i++, j++):** When both supply is exhausted AND demand is satisfied simultaneously
   - **Vertical move (i++):** When supply is exhausted but customer still needs more
   - **Horizontal move (j++):** When customer is satisfied but supplier has remaining capacity

**Key Principle:** The Northwest Corner Method follows a "greedy" approach, always trying to allocate the maximum possible amount at each step, starting from the top-left corner and moving systematically.

### Part 3: Implementation and Visualization

**Purpose:** Execute the algorithm and present results in a clear, understandable format.

1. **Execute the Algorithm:**
   ```python
   allocation, total_cost, steps = northwest_corner_method(supply, demand, cost_matrix)
   ```
   - Calls the main function and receives the results

2. **Display Step-by-Step Process:**
   ```python
   for step in steps:
       print(step)
   ```
   - Shows each allocation decision made during the algorithm
   - Helps users understand the progression of the solution

3. **Create Allocation Table:**
   ```python
   allocation_df = pd.DataFrame(allocation, index=sources, columns=destinations)
   print(allocation_df)
   ```
   - Converts the allocation matrix into a readable pandas DataFrame
   - Uses source and destination names as labels for clarity

4. **Verification Section:**
   - **Supply Verification:** Confirms each supplier's total allocation matches their capacity
   - **Demand Verification:** Confirms each customer receives exactly what they demanded
   - Ensures the solution is feasible and complete

5. **Results Summary:**
   - **Total Cost:** Displays the final transportation cost
   - **Cost Breakdown:** Shows individual route costs for transparency
   - Provides detailed cost analysis for each non-zero allocation

**Benefits of this Visualization:**
- **Transparency:** Users can see exactly how the algorithm works
- **Verification:** Easy to check if constraints are satisfied
- **Analysis:** Detailed cost breakdown helps identify expensive routes
- **Learning:** Step-by-step process aids in understanding the methodology

## Algorithm Characteristics

**Advantages:**
- Simple and easy to understand
- Always finds a basic feasible solution
- Computationally efficient
- Good starting point for optimization methods

**Limitations:**
- May not produce the optimal (minimum cost) solution
- Doesn't consider cost efficiency in allocation decisions
- Often requires further optimization using methods like MODI or Stepping Stone

**Use Cases:**
- Initial solution for transportation problems
- Quick feasibility check
- Educational purposes to understand transportation problem basics
- Baseline solution for comparison with optimized methods
