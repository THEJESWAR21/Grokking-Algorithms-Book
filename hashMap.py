book = {}

book["apple"] = 0.67
book["milk"] = 1.49
book["avocado"] = 1.49

print(book["milk"]) # Returns ERROR if key not found
print(book.get("milk")) # Returns NONE if key not found
