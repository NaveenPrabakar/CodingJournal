# CodingJournal

The following program is a dairy/journal type system that targets a computer science student. The program takes in user entries regarding: What they programmed today, If they had any erros, things they need to do for tommorow, collaboraters they might have had, and addditional comments. 

These entries are then stored inside of database (MySQL) so when the user launches the program again, the data is saved. With the saved entries, the user may see them after entering the day of the entry. The data is extracted by SQL query statements and optimized to ensure a fast extraction. 

They may also change what they wrote on previous entries. Sql modifications statements are used to ensure this change. The update statements are also optimized to produce a quick input to the database.

Additionally, Grammtical and spelling API's are implemented into the program to ensure the user entries are automatically checked for spelling and grammer errors before it is stored inside the data base. This ensures realiability. 

A Shell script was created to automate the task of running the program, which was helpful was debugging and visual purposes while creating the program. 
