for book in data["books"]:
    print("ID:", book["id"])
    print("Title:", book["title"])
    print("Author:", book["author"])
    print("Copies:", book["details"]["copies"])
    print("Available:", book["details"]["available"])
    print("\n")
    
for book in data["books"]:
    print(book["title"])
    
for book in data["books"]:
    title = book["title"]
    available = book["details"]["available"]
    print(f"Title: {title} | Available: {available}")
    
totalcopies = 0

for book in data["books"]:
    totalcopies += book["details"]["copies"]

print("Total Copies:", totalcopies)