import psycopg2

#Connecting Database to Application
def Data_Base_Connection():
    return psycopg2.connect (
        host="INSERT HERE",
        dbname="INSERT HERE",
        user="INSERT HERE",
        password="INSERT HERE"
    )

#Retrieve/Read all student data 
def getAllStudents():
    connect = Data_Base_Connection()                                #establish a connection
    cursorToConnection = connect.cursor()                           #Create a cursor object to interact with database 

    cursorToConnection.execute("SELECT * FROM students")            #Query to retrieve all the student data 
    students = cursorToConnection.fetchall()                        #Gets the result from the query
    for student in students:
        print(student)                                              #prints all the students 
    cursorToConnection.close()                                      #Closes the cursor object
    connect.close()                                                 #Terminates the connection 
   
#Create new student details to the database
def addStudent(first_name, last_name, email, enrollment_date):
    connect = Data_Base_Connection()                                #establish a connection
    cursorToConnection = connect.cursor()                           #Create a cursor object to interact with database 

    cursorToConnection.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",    
                (first_name, last_name, email, enrollment_date))    #Inserts the student details into the database 

    connect.commit()                                                #Commits/saves the changes to the database 
    cursorToConnection.close()                                      #Closes the cursor object
    connect.close()                                                 #Terminates the connection 

#Update existing emails 
def updateStudentEmail(student_id, new_email):
    connect = Data_Base_Connection()                                #establish a connection
    cursorToConnection = connect.cursor()                           #Create a cursor object to interact with database 

    cursorToConnection.execute("UPDATE students SET email = %s WHERE student_id = %s",
                (new_email, student_id))                            #Updates the existing details 
    
    connect.commit()                                                #Commits/saves the changes to the database
    cursorToConnection.close()                                      #Closes the cursor object
    connect.close()                                                 #Terminates the connection

#Delete exisiting student data 
def deleteStudent(student_id):
    connect = Data_Base_Connection()                                #establish a connection
    cursorToConnection = connect.cursor()                           #Create a cursor object to interact with database

    cursorToConnection.execute("DELETE FROM students WHERE student_id = %s", (student_id,))     #Deletes the specified student using the student_id as an identifier 

    connect.commit()                                                #Commits/saves the changes to the database
    cursorToConnection.close()                                      #Closes the cursor object
    connect.close()                                                 #Terminates the connection

# #Main function for testing 
# def main():
#     print("Starting the application...")

#     try:
#         #print("Retrieving all students...")
#         #getAllStudents()
        
#         #print("Adding a new student...")
#         #addStudent('Hamzah', 'hamad', 'hamzah@example.com', '2023-10-19')
        
#         #print("Updating student email...")
#         #updateStudentEmail(21, 'hamzahofficial@example.com')
        
#         print("Deleting a student...")
#         deleteStudent(19)
        

#     except Exception as e:
#         print(f"An error occurred: {e}")

#     print("Application finished.")

# # Ensure to call the main function.
# if __name__ == "__main__":
#     main()
