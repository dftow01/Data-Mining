# Understands the logic behind Apriori and FP-growth

## What is Frequent Itemset?
- Frequent itemsets are groups of items that appear together in a dataset with a frequency greater than or equal to a specified minimum support threshold.
- Finding frequent itemsets is the first step in association rule mining, as they represent potential relationships between items

## What are Associate Rules
- Association rules are derived from frequent itemsets, and they express relationships between items. 
- They have the form "antecedent -> consequent", where the antecedent is a group of items and the consequent is another group of items. 

## What is Support Count 
- A frequent item set is a set of items that occur together frequently in a dataset. The frequency of an item set is measured by the support count, which is the number of transactions or records in the dataset that contain the item set. For example, if a dataset contains 100 transactions and the item set {milk, bread} appears in 20 of those transactions, the support count for {milk, bread} is 20.

## The evaluation metrics used in the algorithms
1. Support
   - This metric measures how frequently an item appears in the dataset relative to the total number of transactions. A higher support indicates a more significant presence of the itemset in the dataset. Support tells us how often a particular item or combination of items appears in all the transactions
2. Confidence
   - The likelihood that the consequent will occur given that the antecedent occurs
   - Confidence assesses the likelihood that an item Y is purchased when item X is purchased. It provides insight into the strength of the association between two items. Confidence tells us how often items go together. (“If bread is bought, butter is bought 75% of the time.”)
3. Lift
  -  Lift evaluates how much more likely two items are to be purchased together compared to being purchased independently. A lift greater than 1 suggests a strong positive association. Lift shows how strong the connection is between items. (“Bread and butter are much more likely to be bought together than by chance.”)

## How they worked together 
1. Find Frequent Itemsets:
The algorithm first identifies itemsets that appear frequently in the data, meeting a minimum support threshold. 
2. Generate Association Rules:
It then uses these frequent itemsets to generate association rules of the form "antecedent -> consequent". 
3. Evaluate Rules:
Finally, the algorithm evaluates the strength of these rules using metrics like support, confidence, and lift to determine which rules are most interesting and useful.

## The main objective of Apriori and FP-growth
- Use the algorithms to mine the frequent itemsets from the dataset
- Then, generate an association rule from the dataset based on the confidence level, which is the ratio of the number of
 transaction that contains the itemset and the number of transactions that contain the antecedents (left-hand side of the rule)
