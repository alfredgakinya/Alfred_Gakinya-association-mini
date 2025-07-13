import random
import pandas as pd

# Item pool (at least 8 unique items)
item_pool = ['Bread', 'Milk', 'Eggs', 'Cheese', 'Butter', 'Juice', 'Apples', 'Bananas']

# Generate 10 fake transactions with 2-5 random items each
transactions = []
for i in range(10):
    num_items = random.randint(2, 5)
    transaction = random.sample(item_pool, num_items)
    transactions.append(transaction)

# Display transactions
for idx, trans in enumerate(transactions, start=1):
    print(f"Transaction {idx}: {trans}")
from mlxtend.preprocessing import TransactionEncoder

te = TransactionEncoder()
te_data = te.fit(transactions).transform(transactions)
df = pd.DataFrame(te_data, columns=te.columns_)

print("\nOne-Hot Encoded DataFrame:")
print(df)

from mlxtend.frequent_patterns import apriori, association_rules

# Get frequent itemsets
frequent_itemsets = apriori(df, min_support=0.2, use_colnames=True)

# Generate association rules
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.5)

# Display rules
print("\nAssociation Rules:")
print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])
