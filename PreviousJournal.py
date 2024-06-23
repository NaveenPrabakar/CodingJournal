import mysql.connector

db = mysql.connector.connect( #connects to MySQL Server for data to be accessed
    host = "localhost",
    user = "root",
    password = "xxxxxxxx"
)

mycursor = db.cursor()

def checkname(Journal):
    try:
        mycursor.execute(f"USE {Journal}")
        return True
    except:
        return False

def extract(date, name):
    try:
        # Use the specified database
        mycursor.execute(f"USE {name}")

        # Define the SQL query with parameterization
        sql = "SELECT * FROM entries WHERE date = %s"
        mycursor.execute(sql, (date,))  

        # Fetch all results
        results = mycursor.fetchall()

        if results:
            # Process and print the results
            query(results)
            print(f"This is the following entry for: {date}")
        else:
            print(f"No entries found for date: {date}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")


def query(results):
    for row in results:
        description = row[0]
        errors = row[1]
        buddy = row[2]
        todo = row[3]
        print(f"Description: {description}\n Errors: {errors}\n Buddy: {buddy}\n Todo: {todo}\n")


