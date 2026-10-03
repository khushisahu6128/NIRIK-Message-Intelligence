import pandas as pd
from preprocess import preprocess_text


# Load dataset
df = pd.read_csv(
    "data/SMSSpamCollection",
    sep="\t",
    header=None,
    names=["label", "message"]
)

# Apply preprocessing to every message
df["clean_message"] = df["message"].apply(preprocess_text)

# Show original and cleaned messages
print(df[["message", "clean_message"]].head(10))