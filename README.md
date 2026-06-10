*README.md* for Personal Journal Manager

### *Personal Journal Manager*
A simple Python command-line app to create, view, search, and delete journal entries. All entries are saved locally in a text file.

#### *Features*
1. *Add a New Entry* – Write an entry with an automatic date & time stamp.
2. *View All Entries* – Display all saved entries.
3. *Search for an Entry* – Search by keyword or date, case-insensitive.
4. *Delete All Entries* – Clear the entire journal after confirmation.
5. *Exit* – Close the program safely.

#### *Requirements*
- Python 3.x
- No external libraries needed. Uses only built-in modules: `os`, `datetime`.

#### *Installation & Run*
1. Save the code as `journal_manager.py`
2. Open terminal/command prompt in that folder
3. Run:
python journal_manager.py


#### *File Storage*
All entries are stored in `journal.txt` in the same folder as the script. 
Format: `[YYYY-MM-DD HH:MM:SS]` followed by your entry text.

#### *Usage Example*
Welcome to Personal Journal Manager!
Please select an option:
1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit

User Input: 1

Enter your journal entry:
Had a great day today!

Entry added successfully!


#### *Error Handling*
- If `journal.txt` doesn’t exist, the program prompts you to add an entry first.
- Empty files show “No journal entries found.”
- Invalid menu choices show “Invalid option. Please select a valid option from the menu.”
- Delete asks for confirmation `yes/no` to prevent accidental loss.

#### *Notes*
- Entries are separated by a blank line for readability.
- Search is case-insensitive and matches partial words.
- Data is stored locally only. No internet connection required.

---

