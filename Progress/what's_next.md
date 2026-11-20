Learn more about SQLite
Finish copying notes to word


Let's prove the table exists
Run:
Shell
sqlite3 career_compass.db
You should get:
Plain Text
sqlite>
Then:
SQL
.tables
 
You should see:
Plain Text
users
Then:
SQL
.schema users
You should see something similar to:
SQL
CREATE TABLE users (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
email TEXT UNIQUE
);
 
Exit with:
SQL
.quit
Next: Put data into the database
Create a file called insert_user.py:
Python
import sqlite3
 
conn = sqlite3.connect("career_compass.db")
cursor = conn.cursor()
 
cursor.execute(
"INSERT INTO users (name, email) VALUES (?, ?)",
("Nate", "nate@example.com")
)
 
conn.commit()
conn.close()
 
print("User added!")
Run:
Shell
python3 insert_user.py
Then check:
Shell
sqlite3 career_compass.db
SQL
SELECT * FROM users;
Expected output:
Plain Text
1|Nate|nate@example.com
 
For CareerCompass Scout
Now that you have the database working, I'd suggest not stopping at a generic users table. A more useful next step is creating tables such as:
SQL
users
careers
skills
assessments
career_matches
saved_careers
That would let CareerCompass Scout store:
User profiles
Assessment results
Skills inventories
Career recommendations
Saved career paths