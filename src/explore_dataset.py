import pandas as pd

# Load the SMS Spam Collection dataset
df = pd.read_csv(
    "data/SMSSpamCollection",
    sep="\t",
    header=None,
    names=["label", "message"]
)

# Show first 5 messages
print("First 5 messages:")
print(df.head())

# Show dataset size
print("\nDataset shape:")
print(df.shape)

# Count Spam and Ham messages
print("\nLabel counts:")
print(df["label"].value_counts())

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())