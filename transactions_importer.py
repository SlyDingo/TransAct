import csv

with open('test.csv', 'r') as file:
    reader = csv.reader(file)
    for i, row in enumerate(reader):
        if i == 0:
            # Skip the header row
            continue
        
        print(row)

# Structure to hold transaction data
class Transaction:
    def __init__(self, name:str, description:str, amount:str) -> None:
        self.ID = name
        self.description = description
        self.amount = amount

    def __repr__(self) -> str:
        """Return a string representation of the transaction."""
        return f"Transaction(ID={self.ID}, description={self.description}, amount={self.amount})"