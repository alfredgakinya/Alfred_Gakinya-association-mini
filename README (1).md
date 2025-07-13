
# Association Rule Mining from Simulated Transaction Data

This project demonstrates how to simulate basic transactional data and use the Apriori algorithm to uncover shopping patterns through association rule mining.

## Contents

- Simulate at least 10 transactions from a pool of 8+ items
- Convert to one-hot encoded format using `TransactionEncoder`
- Use `mlxtend`'s Apriori to find frequent itemsets (support ≥ 0.3)
- Generate rules using confidence (threshold ≥ 0.7)
- Brief explanation of one rule in simple terms

## Requirements

- Python
- pandas
- mlxtend

## How to Run

Run the Jupyter Notebook `Association_Rule_Mining_Transactions.ipynb` to execute each step.

## Example Insight

A rule like `{Milk} → {Bread}` with 75% confidence means: "If someone buys Milk, there's a 75% chance they'll buy Bread too."
