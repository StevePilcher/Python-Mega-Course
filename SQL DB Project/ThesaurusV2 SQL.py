import mysql.connector

con = mysql.connector.connect(
    user="ardit700_student",
    password="ardit700_student",
    host="108.167.140.122",
    database="ardit700_pm1database"
)

cursor = con.cursor()
# Ask for input
word = input("Enter a search word: ")
# Query comes back as a tuple
query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' " % word)
results = cursor.fetchall()

# Check to see if there are any results returned
if results:
    for result in results:
        # Tuple are pairs, the word and description, print index 1
        print(result[1])
else:
    print('There are no results')
