from preprocess import preprocess_text


message = "WIN a FREE prize!!! Visit www.example.com NOW!!!"

cleaned_message = preprocess_text(message)

print("Original:")
print(message)

print("\nAfter preprocessing:")
print(cleaned_message)