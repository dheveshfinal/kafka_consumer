import pandas as pd

# Create some data
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "City": ["NY", "LA", "Chicago", "Houston"]
}

df = pd.DataFrame(data)

# Save DataFrame to CSV inside /app directory
df.to_csv("sample.csv", index=False)

print("CSV file created successfully!")
