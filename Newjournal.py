import mysql.connector

db = mysql.connector.connect(#connects to MySQL Server for data to be stored
    host = "localhost",
    user = "root",
    password = "defg5678"
)


mycursor = db.cursor()

#Creates a Database and the corresponding tables
def createJournal(name):
    try: 
        mycursor.execute(f"CREATE DATABASE {name}") 
        mycursor.execute(f"USE {name}")
        createTables()
        return True
    except:
        return False

#Creates the Tables inside the database 
def createTables():

    sql = """
    CREATE TABLE IF NOT EXISTS entries (
        description VARCHAR(500),
        errors VARCHAR(200),
        buddy VARCHAR(100),
        Todo VarChar(300),
        addtional VARCHAR(100),
        date datetime,

        primary key(date)
    )
    """
    mycursor.execute(sql)

#Inserts User entries into the database
def InsertData(choice1, choice2, choice3, choice4, choice5, choice6, name):
    mycursor.execute(f"USE {name}")
    sql = "INSERT INTO entries (description, errors, buddy, Todo, addtional, date) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (choice1, choice2, choice3, choice4, choice5, choice6)
    try:
        mycursor.execute(sql, values)
        db.commit()
    except:
        ("There's an error")