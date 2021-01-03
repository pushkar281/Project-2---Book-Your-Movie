import functions
import mysql.connector
connection = mysql.connector.connect(user='root',password='Mithaimate@28',host='localhost',database='project')
mycursor = connection.cursor()


def button_case():
    print("\n ********************************")
    print("1.Show the seats\n2.Buy a Ticket\n3.Statistics\n4.Show Booked Tickets User Info\n0.Exit\n")
    choices = int(input("Enter the Number : "))
    switcher = {
        0 : functions.exit_menu,
        1 : functions.show_the_seats,
        2 : functions.buy_ticket,
        3 : functions.statistics,
        4 : functions.user_info
    }
    switch_choice =  switcher.get(choices,"0")
    return switch_choice()

if __name__=="__main__":
    no_of_rows = int(input("Enter the no of rows: "))
    no_of_coloumn = int(input("Enter the no of coloumns: "))
    ######  mysql seats
    for i in range(no_of_rows):
        for j in range(no_of_coloumn):
            ##### Connector logic
            mycursor.execute("INSERT INTO seats (Row_no,Coloumn_no,booked_status,Price) VALUES ({},{},'S',100);".format(i,j))
            connection.commit()

    button_case()

