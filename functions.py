import main
import mysql.connector
connection = mysql.connector.connect(user='root',password='Mithaimate@28',host='localhost',database='project')
mycursor = connection.cursor()


def show_the_seats():
    mycursor.execute("SELECT MAX(Row_no) FROM seats;")
    max_row = mycursor.fetchall()
    mycursor.execute("SELECT MAX(Coloumn_no) FROM seats;")
    max_col = mycursor.fetchall()
    max_row = max_row[0][0]+1
    max_col = max_col[0][0]+1

    for i in range(max_row):
        for j in range(max_col):
            mycursor.execute("SELECT booked_status FROM seats WHERE Row_no = {} AND Coloumn_no = {};".format(i,j))
            seat_status = mycursor.fetchall()

            print(seat_status[0][0], end='  ')
        print()

    main.button_case()


def buy_ticket():
    row_no = int(input("Enter the row no: "))
    col_no = int(input("Enter the coloumn no: "))
    mycursor.execute("SELECT Price FROM seats WHERE Row_no = {} AND Coloumn_no = {};".format(row_no,col_no))
    price = mycursor.fetchall()
    print("Price for this seat is : ",price[0][0])
    booking = input("Do you want to book the ticket ? ")
    if booking.lower() == 'yes':
        name = input("Enter the name: ")
        gender = input("Enter the gender: ")
        age = int(input("Enter the age : "))
        phone_no = int(input("Enter the phone no: "))
        mycursor.execute("INSERT INTO user_info (Name,Gender,Age,Phone_no) VALUES ('{}','{}',{},{});".format(name,gender,age,phone_no))

        connection.commit()
        user_id = mycursor.lastrowid

        mycursor.execute("UPDATE seats SET booked_status = 'B', user_id = {} WHERE Row_no = {} AND Coloumn_no = {};".format(user_id,row_no,col_no))
        connection.commit()
        print("Congratulations your ticket has been booked !!")
        main.button_case()
    else:
        main.button_case()


def statistics():

    mycursor.execute("SELECT COUNT(booked_status) FROM seats WHERE booked_status ='B';")
    booked_count = mycursor.fetchall()
    print("Total Number of purchased tickets : ",booked_count[0][0])

    mycursor.execute("SELECT COUNT(*) FROM seats;")
    total_count = mycursor.fetchall()
    percentage_booked = ((booked_count[0][0]/total_count[0][0])*100)
    print("Percentage of tickets booked is : ",percentage_booked,"%")

    mycursor.execute("SELECT price FROM seats ORDER BY price DESC LIMIT 1;")
    current_income = mycursor.fetchall()
    print("Current income is : ",current_income[0][0])

    mycursor.execute("SELECT SUM(price) FROM seats WHERE booked_status='B';")
    total_income = mycursor.fetchall()
    print("Total income is : ",total_income[0][0])

    main.button_case()

def user_info():
    row_no = int(input("Enter the row no: "))
    col_no = int(input("Enter the coloumn no: "))
    mycursor.execute("SELECT user_id,booked_status,Price FROM seats WHERE row_no = {} AND coloumn_no = {};".format(row_no,col_no))
    seat_obj = mycursor.fetchall()
    is_booked = seat_obj[0][1]
    if is_booked == 'B':
        mycursor.execute("SELECT * FROM user_info WHERE id = {};".format(seat_obj[0][0]))
        all_info = mycursor.fetchall()
        print("Name : ",all_info[0][1])
        print("Gender : ",all_info[0][2])
        print("Age : ",all_info[0][3])
        print("Ticket Price : ",seat_obj[0][2])
        print("Phone No : ",all_info[0][4])

        main.button_case()

    else:
        print("This seat has not been booked yet. ")

        main.button_case()

def exit_menu():
    mycursor.execute("DELETE FROM seats;")
    connection.commit()
    mycursor.execute("DELETE FROM user_info;")
    connection.commit()
