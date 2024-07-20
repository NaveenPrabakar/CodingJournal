import mysql.connector
import Grammer

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


#Outputs the query results
def query(results):
    for row in results:
        description = row[0]
        errors = row[1]
        buddy = row[2]
        todo = row[3]
        additional = row[4]
        print(f"Description: {description}\n Errors: {errors}\n Buddy: {buddy}\n Todo: {todo}\n additional: {additional}")



def modify(date,name):

    while True:
        extract(date,name)
        
        choice = input("These were the entries found, would you like to edit the [d]escription, [e]rrors, [p]artners, [t]odo, [da]te, [o]thers or [q]uit ")

        if choice == 'q':
            break

        edit = input("Enter the new change")
        temp = [edit]
        temp = Grammer.spell(temp)
        update(choice, temp[0], date)



#updates the entries
def update(choice, edit, date):
    word = ""

    match choice:
        case "d":
            word = "description"
        case "e":
            word = "errors"
        case "p":
            word = "buddy"
        case "t":
            word = "Todo"
        case "o":
            word = "additional"
        case "da":
            word = "date"
    
    if word:
        sql = f"UPDATE entries SET {word} = %s WHERE date = %s"
        try:
            mycursor.execute(sql, (edit, date))
            db.commit()
            print("Update successful.")
        except Exception as e:
            print(f"An error occurred: {e}")




