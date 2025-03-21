import streamlit as st

# Initialize session state to store the library
if 'library' not in st.session_state:
    st.session_state.library = []

# Function to add a book
def add_book():
    st.subheader("Add a Book")
    title = st.text_input("Title")
    author = st.text_input("Author")
    year = st.number_input("Publication Year", min_value=0, max_value=2100, step=1)
    genre = st.text_input("Genre")
    read_status = st.radio("Have you read this book?", ("Yes", "No"))
    
    if st.button("Add Book"):
        if title and author and genre:  # Basic validation
            book = {
                "title": title,
                "author": author,
                "year": year,
                "genre": genre,
                "read": True if read_status == "Yes" else False
            }
            st.session_state.library.append(book)
            st.success("Book added successfully!")
        else:
            st.error("Please fill in all fields.")

# Function to remove a book
def remove_book():
    st.subheader("Remove a Book")
    if st.session_state.library:
        titles = [book["title"] for book in st.session_state.library]
        title_to_remove = st.selectbox("Select a book to remove", titles)
        
        if st.button("Remove Book"):
            st.session_state.library = [book for book in st.session_state.library if book["title"] != title_to_remove]
            st.success("Book removed successfully!")
    else:
        st.warning("No books in the library to remove.")

# Function to search for a book
def search_book():
    st.subheader("Search for a Book")
    search_by = st.radio("Search by:", ("Title", "Author"))
    query = st.text_input(f"Enter the {search_by.lower()}")
    
    if st.button("Search"):
        if query:
            if search_by == "Title":
                results = [book for book in st.session_state.library if query.lower() in book["title"].lower()]
            else:
                results = [book for book in st.session_state.library if query.lower() in book["author"].lower()]
            
            if results:
                st.write("Matching Books:")
                for book in results:
                    status = "Read" if book["read"] else "Unread"
                    st.write(f"- **{book['title']}** by {book['author']} ({book['year']}) - {book['genre']} - {status}")
            else:
                st.warning("No matching books found.")
        else:
            st.warning("Please enter a search term.")

# Function to display all books
def display_all_books():
    st.subheader("Your Library")
    if st.session_state.library:
        for i, book in enumerate(st.session_state.library, 1):
            status = "Read" if book["read"] else "Unread"
            st.write(f"{i}. **{book['title']}** by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        st.warning("No books in the library.")

# Function to display statistics
def display_statistics():
    st.subheader("Library Statistics")
    total_books = len(st.session_state.library)
    read_books = sum(book["read"] for book in st.session_state.library)
    percentage_read = (read_books / total_books * 100) if total_books > 0 else 0
    
    st.write(f"Total books: **{total_books}**")
    st.write(f"Percentage read: **{percentage_read:.1f}%**")

# Main function to run the Streamlit app
def main():
    st.title("Personal Library Manager")
    
    # Sidebar menu
    menu = st.sidebar.selectbox(
        "Menu",
        ["Add a Book", "Remove a Book", "Search for a Book", "Display All Books", "Display Statistics"]
    )
    
    if menu == "Add a Book":
        add_book()
    elif menu == "Remove a Book":
        remove_book()
    elif menu == "Search for a Book":
        search_book()
    elif menu == "Display All Books":
        display_all_books()
    elif menu == "Display Statistics":
        display_statistics()

# Run the app
if __name__ == "__main__":
    main()