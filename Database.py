# _____________________________________________________
# | Name : Janmeijay Vinod Mapari (Jay) [jvm33]        |
# | Coursework: CM12004, SQL Databases with Python     |
# | Student_ID: 239406965                              |
# | Date Submitted: 15/12/2023                         |
# | Additional Authors: None (indiviual project)       |
# |____________________________________________________|
# This is a code for a database for an airline
# ****************************************************************************************************************************

# importing relevant libraries for the project
import math
import random
import sqlite3
from prettytable import PrettyTable

# standard code for the project
conn = sqlite3.connect("Freshair.db")
c = conn.cursor()

# Making a table named Flights
c.execute("DROP TABLE IF EXISTS Flights")
# Creating a table names Flights, which has all the flight information
c.execute('''CREATE TABLE Flights (
                Flight_ID                 TEXT PRIMARY KEY,
                time                      TIME,
                date                      DATE,
                Leaving                   TEXT,
                Layover                   TEXT,
                Destination               TEXT,
                Aircraft_ID               TEXT,
                Pilot_Name                TEXT, 
                FOREIGN KEY (Aircraft_ID) REFERENCES Aircrafts (Aircraft_ID)
            )''')

# Inserting some data in Flights
c.execute('''INSERT INTO Flights (Flight_ID, time , date , Leaving , Layover , Destination, Pilot_Name, Aircraft_ID)
          VALUES 
          ('1',"23:30","12/12","London","Paris","Warsaw","Tom",'BO787D'),
          ('2',"19:30","9/12","Berlin","London","Dublin","Maxx",'B07474'),
          ('3',"23:45","15/09","Manchester", "Rome", "Istanbul", "James",'BO7478'),
          ('4',"13:20","12/10","Turin","Helsinki","Murmansk","Stuart","BO767")''')

# Creating a table of Aircrafts for Aircrafts and the type off Aircraft
c.execute("DROP TABLE IF EXISTS Aircrafts")
c.execute('''CREATE TABLE Aircrafts (
                Aircraft_ID                 TEXT PRIMARY KEY,
                Aircraft_Type               TEXT
            )''')
# make the garage i.e. table of all the aircrafts we own and their IDs
c.execute('''INSERT INTO Aircrafts (Aircraft_ID,Aircraft_Type) VALUES
          ('BO787D','Boeing 787 Dreamliner'),
          ('BO7474','Boeing 747-400 '),
          ('BO7478','Boeing 747-8'),
          ('BO767','Boeing 767'),
          ('AIR330','Airbus A330'),
          ('AIR319','Airbus A319')''')

# Creating a table of Pilots with Pilot details
c.execute("DROP TABLE IF EXISTS Pilots")
c.execute('''CREATE TABLE Pilots (
                   Pilot_ID                INT PRIMARY KEY,
                   Pilot_Name              TEXT
                )''')

# data of pilots we have
c.execute('''INSERT INTO Pilots (Pilot_ID,Pilot_Name) VALUES 
          ('P1','Tom'),
          ('P2','Maxx'),
          ('P3','James'),
          ('P4','Stuart'),
          ('P5','Boris'),
          ('P6','Ethan'),
          ('P7','David')''')

# Creating a table for pairing flights with Pilots 
c.execute('''CREATE TABLE IF NOT EXISTS Pilot_Flight (
                    Flight_ID               INT,
                    Pilot_ID                INT,
                    FOREIGN KEY (Flight_ID) REFERENCES Flights (Flight_ID),
                    FOREIGN KEY (Pilot_ID)  REFERENCES Pilots (Pilot_ID)
                )''')

# Inserting data into the table
c.execute('''INSERT INTO Pilot_Flight (Flight_ID,Pilot_ID) VALUES ("1","P1"),("2","P2"),("3","P3"),("4","P4")''')


# *****************************************************************************************************
# SEARCHING DETAILS FROM THE DATABASE
# *****************************************************************************************************

# function to search flights by departure airport i.e. airport 'from'
def search_by_id(search_flight_id):
    c.execute("SELECT * FROM Flights WHERE Flight_ID = ?", (search_flight_id,))

    # the part below is common to every function in this part
    rows = c.fetchall() # assigning the rows to a variable named rows
    if rows: # if rows is not empty then the code below runs
        # standard PrettyTable code below
        a = PrettyTable() # the variable is a table now
        # the column headings
        a.field_names = ["Flight_ID","Scheduled time","date","Leaving","Layover","Destination","Pilot Name", "Aircraft_ID"]
        # for a row in rows
        for row in rows: 
            a.add_row(row) # add the row to the table 
        print(a) # print the table with the required rows

# function to search flights by departure airport i.e. airport 'from'
def search_by_departure(search_departure):
    c.execute("SELECT * FROM Flights WHERE Leaving = ?", (search_departure,))

    # the part below is common to every function in this part
    rows = c.fetchall() # assigning the rows to a variable named rows
    if rows: # if rows is not empty then the code below runs
        # standard PrettyTable code below
        a = PrettyTable() # the variable is a table now
        # the column headings
        a.field_names = ["Flight_ID","Scheduled time","date","Leaving",
                         "Layover","Destination", "Pilot Name", "Aircraft_ID"]
        # for a row in rows
        for row in rows: 
            a.add_row(row) # add the row to the table 
        print(a) # print the table with the required rows

def search_by_destination(search_destination):
    c.execute("SELECT * FROM Flights WHERE Destination = ?", (search_destination,))

    # the part below is common to every function in this part
    rows = c.fetchall() # assigning the rows to a variable named rows
    if rows: # if rows is not empty then the code below runs
        # standard PrettyTable code below
        a = PrettyTable() # the variable is a table now
        # the column headings
        a.field_names = ["Flight_ID","Scheduled time","date","Leaving",
                         "Layover","Destination", "Pilot Name" , "Aircraft_ID"]
        # for a row in rows
        for row in rows: 
            a.add_row(row) # add the row to the table 
        print(a) # print the table with the required rows

def search_by_date(search_scheduled_date):
    c.execute("SELECT * FROM Flights WHERE date = ?", (search_scheduled_date,))

    # the part below is common to every function in this part
    rows = c.fetchall() # assigning the rows to a variable named rows
    if rows: # if rows is not empty then the code below runs
        # standard PrettyTable code below
        a = PrettyTable() # the variable is a table now
        # the column headings
        a.field_names = ["Flight_ID","Scheduled time","date","Leaving",
                         "Layover","Destination", "Pilot Name", "Aircraft_ID"]
        # for a row in rows
        for row in rows: 
            a.add_row(row) # add the row to the table 

def search_by_time(search_scheduled_time):
    c.execute("SELECT * FROM Flights WHERE time = ?", (search_scheduled_time,))

    # the part below is common to every function in this part
    rows = c.fetchall() # assigning the rows to a variable named rows
    if rows: # if rows is not empty then the code below runs
        # standard PrettyTable code below
        a = PrettyTable() # the variable is a table now
        # the column headings
        a.field_names = ["Flight_ID","Scheduled time","date","Leaving",
                         "Layover","Destination", "Pilot Name" , "Aircraft_ID"]
        # for a row in rows
        for row in rows: 
            a.add_row(row) # add the row to the table 
        print(a) # print the table with the required rows

def search_by_layover(search_layover_airport):
    c.execute("SELECT * FROM Flights WHERE Layover = ?", (search_layover_airport,))

    # the part below is common to every function in this part
    rows = c.fetchall() # assigning the rows to a variable named rows
    if rows: # if rows is not empty then the code below runs
        # standard PrettyTable code below
        a = PrettyTable() # the variable is a table now
        # the column headings
        a.field_names = ["Flight_ID","Scheduled time","date","Leaving",
                         "Layover","Destination", "Pilot Name" , "Aircraft_ID"]
        # for a row in rows
        for row in rows: 
            a.add_row(row) # add the row to the table 
        print(a) # print the table with the required rows

# *****************************************************************************************************
# DELETING DETAILS FROM THE DATABASE
# *****************************************************************************************************

# deleting by the flight_id required
def delete_by_flight_id(flight_id):
    c.execute("DELETE FROM Flights WHERE Flight_ID = ?", (flight_id,))
    conn.commit()

# deleting by the departure airport mentioned
def delete_by_departure(delete_departure):
    c.execute("DELETE FROM Flights WHERE Leaving = ?",(delete_departure,))
    conn.commit()

# deleting by the layover airport mentioined
def delete_by_layover(delete_layover):
    c.execute("DELETE FROM Flights WHERE Layover = ?",(delete_layover,))
    conn.commit()

# deleting by the destination airport 
def delete_by_destination(delete_destination):
    c.execute("DELETE FROM Flights WHERE Destination = ?",(delete_destination,))
    conn.commit()

# deleting by the flying date
def delete_by_date(delete_date):
    c.execute("DELETE FROM Flights WHERE date = ?",(delete_date,))
    conn.commit()

# deleting by the flying time
def delete_by_time(delete_time):
    c.execute("DELETE FROM Flights WHERE time =  ?",(delete_time,))
    conn.commit()

# deleting by the pilot's name
def delete_by_pilot(delete_pilot_name):
    c.execute("DELETE FROM Flights WHERE Pilot_Name = ?",(delete_pilot_name,))
    conn.commit()

# *****************************************************************************************************
# UPDATING THE FLIGHT DETAILS
# *****************************************************************************************************

# updating the database with the help of flight_id
def update_flight(flight_id):
  # We can either update the Journey (airports), Pilot, or Schedule
    print("What do you want to update?")
    print("1. Journey")
    print("2. Schedule")
    print("3. Pilot")
# this is the reason for updating
    updating_id = input("Enter the reason for updating (1 to 3): ")

  # each choice is taken to its respective function
    if updating_id == "1":
        update_journey(flight_id)
    elif updating_id == "2":
        update_schedule(flight_id)
    elif updating_id == "3":
        update_pilot(flight_id)
    else:
        print("Invalid choice. Please enter 1 or 2.")

# to update the journey you can only change the airports, 
def update_journey(flight_id):
    new_leaving = input("Enter the new Leaving airport: ")
    new_layover = input("Enter the new Layover: ")
    new_destination = input("Enter the new Destination: ")

    c.execute('''UPDATE Flights
                 SET Leaving = ?, Layover = ?, Destination = ?
                 WHERE Flight_ID = ?''', (new_leaving, new_layover, new_destination, flight_id))
    conn.commit()

# to update the pilot you can only change the pilot's name 
def update_pilot(flight_id):
    pilot_name = input("Enter Pilot Name: ")
    c.execute('''UPDATE Flights SET Pilot_Name = ? , Flight_ID = ?''' , (pilot_name,flight_id))
    conn.commit()

# to update the schedule you can change the date and time of the flight
def update_schedule(flight_id):
    new_time = input("Enter the new scheduled time: ")
    new_date = input("Enter the new scheduled date: ")

    c.execute('''UPDATE Flights
                 SET time = ?, date = ?
                 WHERE Flight_ID = ?''', (new_time, new_date, flight_id))
    conn.commit()

# *****************************************************************************************************
# ADDING FLIGHTS
# *****************************************************************************************************
# A function to add flights to the table
def add_flight(flight_id, scheduled_time, scheduled_date, leaving, layover, destination, pilot_name, aircraft_id):
    # SQL command to insert values into the table
    c.execute('''INSERT INTO Flights (Flight_ID, time, date, Leaving, Layover, Destination, Pilot_Name, Aircraft_ID)
                      VALUES (?, ?, ?, ?, ?, ?,?, ?)''', (flight_id, scheduled_time, scheduled_date, leaving, layover, destination, pilot_name, aircraft_id))
    conn.commit()
    print(f"Flight with ID {flight_id} added successfully.")
    # successfully added message
    if sqlite3.IntegrityError:
        # if there is an integrity eror i.e. primary key is repeated then we display the message below
        print(f"Error: Flight with ID {flight_id} already exists in the database.")

# *****************************************************************************************************
# VIEWING THE DETAILS PARAMETER BY PARAMETER 
# *****************************************************************************************************

# to view all flights 
def view_flights():
    c.execute("SELECT * FROM Flights")
    rows = c.fetchall()

    if rows: # if rows is not null then
        a = PrettyTable() # standard PrettyTable syntax
        a.field_names =["Flight_ID","time","date","Leaving","Layover","Destination","Pilot_Name","Aircraft_ID"] # Column Headings
        a.add_rows(rows) # adding the rows to the PrettyTable
        print(a) # Printing the PrettyTable


# a function to view all the flights flying to a destination
def view_flights_by_destination(view_destination):
    # selects the required rows matching with the parameter we mentioned
    c.execute("SELECT * FROM Flights WHERE Destination = ?", (view_destination,)) 
    # rows variable is assigned here to all the rows of the table which satisfy the above condition
    rows = c.fetchall()

    if rows: # if rows is not null then
        a = PrettyTable() # standard PrettyTable syntax
        a.field_names =["Flight_ID","time","date","Leaving","Layover","Destination","Pilot_Name","Aircraft_ID"] # Column Headings
        a.add_rows(rows) # adding the rows to the PrettyTable
        print(a) # Printing the PrettyTable

# a function to view the flight of a particular flight_id
def view_flights_by_id(view_flight_id):
    # To select the required rows of the table matching with our input id
    c.execute("SELECT * FROM Flights WHERE Flight_ID = ?", (view_flight_id,))
    # rows variable is assigned here to all the rows of the table which satisfy the above condition
    rows = c.fetchall()

    if rows: # if rows is not null then
        a = PrettyTable() # standard PrettyTable syntax
        a.field_names = ["Flight_ID","time","date","Leaving","Layover","Destination","Pilot_Name","Aircraft_ID"] # Column Headings
        a.add_rows(rows) # adding the rows to the PrettyTable
        print(a) # Printing the PrettyTable


# a function to view all the flights having a layover at a particular airport
def view_flights_by_layover(view_layover):
    # selecting the required rows of the table which have the same layover airport as we asked for
    c.execute("SELECT * FROM Flights WHERE Layover = ?", (view_layover,))
    # rows variable is assigned here to all the rows of the table which satisfy the above condition
    rows = c.fetchall()

    if rows: # if rows is not null then
        a = PrettyTable() # standard PrettyTable syntax
        a.field_names = ["Flight_ID","time","date","Leaving","Layover","Destination","Pilot_Name","Aircraft_ID"] # Column Headings
        a.add_rows(rows) # adding the rows to the PrettyTable
        print(a) # Printing the PrettyTable


# a function to view all the flights who have a departure from the same airport
def view_flights_by_departure(view_leaving):
    # selecting the flights from the table which have the departure airport which we asked for in the input
    c.execute("SELECT * FROM Flights WHERE Leaving = ?", (view_leaving,))
    # rows variable is assigned here to all the rows of the table which satisfy the above condition
    rows = c.fetchall()

    if rows: # if rows is not null then
        a = PrettyTable() # standard PrettyTable syntax
        a.field_names = ["Flight_ID","time","date","Leaving","Layover","Destination","Pilot_Name","Aircraft_ID"] # Column Headings
        a.add_rows(rows) # adding the rows to the PrettyTable
        print(a) # Printing the PrettyTable


# a function to view all the flights flying at a partiuclar date
def view_flights_by_date(view_date):
    # selects all the flights from the table flying at the input date
    c.execute("SELECT * FROM Flights WHERE date = ?", (view_date,))
    # rows variable is assigned here to all the rows of the table which satisfy the above condition
    rows = c.fetchall()

    if rows: # if rows is not null then
        a = PrettyTable() # standard PrettyTable syntax
        a.field_names = ["Flight_ID","time","date","Leaving","Layover","Destination","Pilot_Name","Aircraft_ID"] # Column Headings
        a.add_rows(rows) # adding the rows to the PrettyTable
        print(a) # Printing the PrettyTable


# a function to display all hte flights flying at a particular time
def view_flights_by_time(view_time):
    # selects all the flights from the table hwihc are flying at the given time
    c.execute("SELECT * FROM Flights WHERE time = ?", (view_time,))
    # rows variable is assigned here to all the rows of the table which satisfy the above condition
    rows = c.fetchall()

    if rows: # if rows is not null then
        a = PrettyTable() # standard PrettyTable syntax
        a.field_names = ["Flight_ID","time","date","Leaving","Layover","Destination","Pilot_Name","Aircraft_ID"] # Column Headings
        a.add_rows(rows) # adding the rows to the PrettyTable
        print(a) # Printing the PrettyTable

def view_flights_by_pilot(view_pilot):
    # selects all the flights from the table hwihc are flying at the given time
    c.execute("SELECT * FROM Flights WHERE Pilot_Name = ?", (view_pilot,))
    # rows variable is assigned here to all the rows of the table which satisfy the above condition
    rows = c.fetchall()

    if rows: # if rows is not null then
        a = PrettyTable() # standard PrettyTable syntax
        a.field_names = ["Flight_ID","time","date","Leaving","Layover","Destination","Pilot_Name","Aircraft_ID"] # Column Headings
        a.add_rows(rows) # adding the rows to the PrettyTable
        print(a) # Printing the PrettyTable

# *****************************************************************************************************
# Main Loop
# *****************************************************************************************************

  # main loop
if __name__ == "__main__":
    while True: # will run till I break it
      # introductory main menu
        print("Welcome to the database of flight management")
        print("What would you like to do?")
        print("1. To look at our garage (should do before adding elements)")
        print("2. To look at all the Pilots this firm has (should do as well)")
        print("3. Add data into the database.")
        print("4. Delete data from the database.")
        print("5. View data from the database.")
        print("6. Update data in the database.")
        print("7. To Exit")
        # takes user input and stores it ofr further redirection
        user_input = input("Enter your choice (1 to 7)\n")

        # if user inputs 1 then we show our garage
        if user_input == "1":
            print("This is our plane garage\n")
            print("We have the following planes in our garage: \n Boeing 787 Deamliner \n Boeing 747-400 \n Boeing 747-8 \n Boeing 767 \n Airbus A330 \n Airbus A319 \n")

        # if user inputs 2 then we show our flight staff
        if user_input == "2":
            print("This is our Staff")
            print("We have \n Tom \n Maxx \n James \n Stuart \n Boris \n Ethan \n Daivd \n Joel \n John \n Jonathan")     

        # if user inputs 3 then we add data into the database
        if user_input == "3":
            print("start adding a flight to the database:\n ")
            # we essentially ask for the new data they are adding, checking for primary key repeating in the initial function
            add_flight_id = input("Enter the flight_id of the flight you want to add:")
            add_flight_time = input("Enter the time of the flight you want to add: ")
            add_flight_date = input("Enter the date of flying for the flight you want to add: ")
            add_flight_leaving = input("Enter the departure airport of the flight you want to add: ")
            add_flight_layover = input("Enter layover of the route you are adding: ")
            add_flight_destination = input("Enter the destination of the route you are adding: ")
            add_flight_aircraft_type = input("Enter the aircraft you will be flying by: ")
            add_pilot = input("Enter the pilot for this flight: ")

            # here we check if the pilot's anem entered is valid or not
            def pilot_validity(name):
              c.execute("SELECT Pilot_Name FROM Flights WHERE Pilot_Name = ?", (name,))
              row = c.fetchone()
              return row[0] if row is not None else None

            add_pilot_name = pilot_validity(add_pilot)

            # here we check if the aircraft type entered is valid or nor
            def aircraft_id_of_type(type):
                c.execute("SELECT Aircraft_ID FROM Aircrafts WHERE Aircraft_Type = ?", (type,))
                row = c.fetchone()
                return row[0] if row is not None else None

            add_flight_aircraft_id = aircraft_id_of_type(add_flight_aircraft_type)

          # if both (Pilot_Name and Aircraft_ID) are valid then we add the data into the database)
            if add_flight_aircraft_id and add_pilot_name: 
                add_flight(add_flight_id,add_flight_time,add_flight_date,add_flight_leaving,add_flight_layover,add_flight_destination, add_pilot_name, add_flight_aircraft_id)
                view_flights()
            else:
                print("Invalid aircraft type.")
        # if user inputs 4 then we delete data from the database
        if user_input == "4":
          # we ask for the details of what they want to delete the data on
            print("Enter the parameter on which you want to select the data to delete")
            print("1. on the basis of flight_id")
            print("2. on the basis of time of flight")
            print("3. on the basis of the date of the flight")
            print("4. on the basis of the Leaving airport")
            print("5. on the basis of Layover airport")
            print("6. on the basis of Destination airport")
            print("7. on the basis of pilot's name")
            print("8. to exit")
            delete_input = input("Enter your choice (1 to 7)\n")

          # deleting data by flight_id
            if delete_input == "1":
                delete_by_id_input = input("enter the flight_id you want to delete:\n")
                delete_by_flight_id(delete_by_id_input)
                view_flights()

          # deleting data by time of the flight's departure
            if delete_input == "2":
                delete_by_time_input = input("Enter the time of the flight you want to delete:\n")
                delete_by_time(delete_by_time_input)
                view_flights()

          # deleting data by the date of flight
            if delete_input == "3":
                delete_by_date_input = input("Enter the date of the flight you want to delete:\n")
                delete_by_date(delete_by_date_input)
                view_flights()

          # deleting the data by the departure airport
            if delete_input == "4":
                delete_by_departure_input = input("Enter the departure airport of the flight you want to delete:\n")
                delete_by_departure(delete_by_departure_input)
                view_flights()

          # deleting the data by the layover airport
            if delete_input == "5":
                delete_by_layover_input = input("Enter the layover airport of the flight you would like to delete:\n")
                delete_by_layover(delete_by_layover_input)
                view_flights()

          # deleting the data by the destination
            if delete_input == "6":
                delete_by_destination_input = input("Enter the destination airport of the flight you would like to delete:\n")
                delete_by_destination(delete_by_destination_input)
                view_flights()

        # deleting the data by the pilot's name
            if delete_input == "7":
                delete_by_pilot_name_input = input("Enter name of the pilot whose flights you want to delete: \n")
                delete_by_pilot(delete_by_pilot_name_input)
                view_flights()

            if delete_input == "8":
                print("*****merci*****")
                break
            else: 
                print(f"{delete_input} is an Invalid input, please try again")

        # if user inputs 5 then we view the data in the database
        if user_input == "5":
          # choosing the parameter to view the database on
            print("Enter the parameters on which you want to view the data")
            print("1. to view data on the basis of flight_id")
            print("2. to view data on the basis of departure airport")
            print("3. to view data on the basis of destination airport")
            print("4. to view data on the basis of layover aiport")
            print("5. to view data on the basis of flight date")
            print("6. to view data on the basis of time of flight")
            print("7. to view data on the basis of the Pilot's Name")
            print("8. to exit")
            view_input = input("Enter your choice (1 to 8)")

          # viewing the data on the basis of flight_id
            if view_input == "1":
                view_flights_by_id_input = input("Enter the flight_id of the flight you would like to see:\n")
                view_flights_by_id(view_flights_by_id_input)

          # viewing the data on the basis of departure airport
            if view_input == "2":
                view_flights_by_departure_input = input("Enter the departure airport of the flight you want to view information of:\n")
                view_flights_by_departure(view_flights_by_departure_input)

          # viewing the data on the basis of destination airport
            if view_input == "3":
                view_flights_by_destination_input = input("Enter the destination airport of the flight you would like to see information of:\n")
                view_flights_by_destination(view_flights_by_destination_input)

          # viewing the data on the basis of layover aiport
            if view_input == "4":
                view_flights_by_layover_input = input("Enter the layover airport of the flight you need information of: \n")
                view_flights_by_layover(view_flights_by_layover_input)

          # viewing the data on the basis of flight date
            if view_input == "5":
                view_flights_by_date_input = input("Enter the date of the flight you need information of:\n")
                view_flights_by_date(view_flights_by_date_input)

          # viewing the data on the basis of time of flight's departure
            if view_input == "6":
                view_flights_by_time_input = input("Enter the time of the flight you need information of: \n")
                view_flights_by_time(view_flights_by_time_input)

          # viewing the data on the basis of the Pilot's Name
            if view_input == "7":
                view_flights_by_pilot_input = input("Enter the name of Pilot you want to see flights of \n ")
                view_flights_by_pilot(view_flights_by_pilot_input)

          # exiting the program
            if view_input == "8":
                break

            else: 
                break

      # if user inputs 6 then we update the Flights details
        if user_input == "6":
            input_flight_id = input("Enter flight id of the flight you want to update the details of: \n "  )
            update_flight(input_flight_id)
            view_flights()

      # if the user presses 7 then we exit. 
        if user_input == "7":
            print("Thanks for using this service")
            break