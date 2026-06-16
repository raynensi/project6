# def add_entry():
#     entry = input("Enter your journal entry:")
#     with open("cmn.txt", "a") as c:
#         c.write(entry+"\n")
#         print("Entry added successfully")

# def view_entries():
#     try:
#         with open("cmn.txt", "r") as c:
#             content=c.read()
#             if content.strip()=="":
#                 print("No entry found")
#             else:
#                 print("----All entries----")
#                 print(content)
#     except filenotfounderror:
#         print("no entries found")
    
# def search_entry():
#     keyword = input("Enter a keyword or date to search: ")
#     try:
#         with open("cmn.txt", "r") as c:
#             content = c.read()
#             if keyword.lower() in content.lower():
#                 print("Matching Entries:")
#             else:
#                 print(f"No entries were found for the keyword: {keyword}.")
#     except FileNotFoundError:
#         print("\nError: The journal file does not exist. Please add a new entry first.")

# def delete_entries():
#     try:
#         if not os.path.exists():
#             print("No journal entries to delete.")
#             return

#         confirm = input("Are you sure you want to delete all entries? (yes/no): ")
#         if confirm.lower() == 'yes':
#             with open("cmn.txt", "w") as c:
#                 c.write("")
#             print("All journal entries have been deleted.")
#         else:
#             print("Delete cancelled.")
#     except FileNotFoundError:
#         print("No journal entries to delete.")

# def menu():
#     while True:
#         print("\nWelcome to Personal Journal Manager!")
#         print("Please select an option:")
#         print("1. Add a New Entry")
#         print("2. View All Entries")
#         print("3. Search for an Entry")
#         print("4. Delete All Entries")
#         print("5. Exit")

#         choice = input("\nUser Input: ")

#         if choice == "1":
#             add_entry()
#         elif choice == "2":
#             view_entries()
#         elif choice == "3":
#             search_entry()
#         elif choice == "4":
#             delete_entries()
#         elif choice == "5":
#             print("Thank you for using Personal Journal Manager. Goodbye!")
#             break
#         else:
#             print("\nInvalid option. Please select a valid option from the menu.")
