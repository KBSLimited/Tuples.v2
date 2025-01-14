def add_book(library, title, author):
    new_book = (title, author)

    if new_book in library:
        print(f"Book '{title}' by {author} already exists in the library.")
    else:
        library.append(new_book)
        print(f"Book '{title}' by {author} has been added to the library.")

# Example usage:
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

# Adding new books
add_book(library, "1984", "George Orwell")  # Already exists
add_book(library, "To Kill a Mockingbird", "Harper Lee")  # New book
add_book(library, "The Great Gatsby", "F. Scott Fitzgerald")  # New book

# Displaying updated library
print("\nUpdated Library:")
for index, (title, author) in enumerate(library, 1):
    print(f"Book {index}: {title} by {author}")