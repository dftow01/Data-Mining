# 🚚 Transportation Problem and Northwest Corner Method

## 📌 Overview

The **Transportation Problem** is a special type of **Linear Programming** problem where the objective is to determine the **most cost-efficient way** to transport goods from multiple **sources** to multiple **destinations**, while satisfying supply and demand constraints.

---

## 🧮 Problem Setup

### Components:
- **Sources (Supply)**: Each origin point has a fixed supply.
- **Destinations (Demand)**: Each destination point has a fixed demand.
- **Cost Matrix**: Represents the cost of transporting goods from each source to each destination.

### Objective:
> **Minimize the total transportation cost** while meeting all supply and demand.

---

## 🛠️ Northwest Corner Method (NWCM)

The **Northwest Corner Method** is a heuristic technique to find an **initial feasible solution** for the transportation problem. It starts at the **top-left (northwest) corner** of the cost matrix.

### ⚠️ Note:
This method **does not guarantee the optimal solution**, but provides a valid starting point for further optimization (e.g., MODI or Stepping Stone Method).

---

## 📐 Step-by-Step Guide

### Given:
|        | D1 | D2 | D3 | Supply |
|--------|----|----|----|--------|
| **S1** | 2  | 3  | 1  | 30     |
| **S2** | 5  | 4  | 2  | 40     |
| **S3** | 1  | 6  | 4  | 20     |
| **Demand** | 20 | 30 | 40 |        |

---

### Step 1: Start at Top-Left (S1-D1)
- Supply = 30, Demand = 20 → Allocate **min(30, 20) = 20**
- Update: S1 = 10, D1 = 0 → Move to next column (D2)

### Step 2: S1-D2
- Supply = 10, Demand = 30 → Allocate **10**
- Update: S1 = 0, D2 = 20 → Move to next row (S2)

### Step 3: S2-D2
- Supply = 40, Demand = 20 → Allocate **20**
- Update: S2 = 20, D2 = 0 → Move to next column (D3)

### Step 4: S2-D3
- Supply = 20, Demand = 40 → Allocate **20**
- Update: S2 = 0, D3 = 20 → Move to next row (S3)

### Step 5: S3-D3
- Supply = 20, Demand = 20 → Allocate **20**
- Done. All supply and demand met.

### Important Rule
- In NWCM, you must fully exhaust the supply of one supplier (row) before moving to the next.
- This ensures that:
  - You go from left to right within a row until the supply is used up.
  - Only then do you move down to the next supplier.

---

## ✅ Final Allocation Table

|        | D1 | D2 | D3 | Supply |
|--------|----|----|----|--------|
| **S1** | 20 | 10 |    | 0      |
| **S2** |    | 20 | 20 | 0      |
| **S3** |    |    | 20 | 0      |
| **Demand** | 0  | 0  | 0  |        |

---

## 💰 Total Transportation Cost

Using the original cost matrix:

- S1-D1: 20 × 2 = 40  
- S1-D2: 10 × 3 = 30  
- S2-D2: 20 × 4 = 80  
- S2-D3: 20 × 2 = 40  
- S3-D3: 20 × 4 = 80  

### 🔽 **Total Cost = 270**

---

## 🔄 When to Use Northwest Corner Method?

| Feature      | Description                                         |
|--------------|-----------------------------------------------------|
| Simplicity   | Very easy to apply manually or programmatically     |
| Use case     | First step in solving transportation problem        |
| Limitation   | May yield high-cost solutions (non-optimal)         |
| Next step    | Use MODI or Stepping Stone to optimize              |

---

## 🌐 Applications

- Logistics and Supply Chain Management
- Manufacturing Distribution
- Airline Scheduling
- Vaccine/Medical Supply Distribution

---

## 📚 Further Learning

- Vogel’s Approximation Method (VAM)
- MODI (Modified Distribution) Method
- Stepping Stone Method
- Python: `scipy.optimize.linprog` for solving optimally

---

*Created by: DF TOW*  
*Last updated: 8 June 2025*
