"""
Quotes Management System is my personal program from which i want to manage my Quotes,
which i used to write in my @coding.tutor posts on Instagram, basically it takes all 
quotes and check and return whether it's present in the exisisting quotes or not. This
will make my work easy cause i don't have to waste my time in matching quoutes again & 
again.
"""

class QuotesManagementSystem:
    # @staticmethod
    # def createList():
    #     global myQuotes, myAuthors
    #     f = open("quotes list.txt", "r")
    #     allQuotes = f.read()
    #     myQuotes = allQuotes.split(".\n")
    #     f.close()
    #     f = open("authors list.txt", "r")
    #     allAuthors = f.read()
    #     myAuthors = allAuthors.split(".\n")
    #     f.close()

    @staticmethod
    def addQuotes():
        newQuote = input("\n\t\t\tEnter your Quote here: ")
        newAuthor = input("\t\t\t\tAuthor: ")

        f = open("quotes list.txt", "a")
        f.write(newQuote)
        f.write(".\n")
        f.close()
        f = open("authors list.txt", "a")
        f.write(newAuthor)
        f.write(".\n")
        f.close()

    @staticmethod
    def display():
        global myQuotes, myAuthors
        f = open("quotes list.txt", "r")
        allQuotes = f.read()
        myQuotes = allQuotes.split(".\n")
        f.close()
        f = open("authors list.txt", "r")
        allAuthors = f.read()
        myAuthors = allAuthors.split(".\n")
        f.close()
        for index, value in enumerate(myQuotes):
            if index+2 > len(myQuotes):
                break;
            else:
                print(f"\t-------------------------------{index+1}-----------------------------", end="")
                print("\n\t\t", end="")
                quote = value.split(" ")
                for iindex, vaalue in enumerate(quote):
                    if iindex%8==0:
                        print("\n", end="")
                        print("\t\t", end="")
                    print(f"{vaalue} ", end="")
                print(f"\n\n\t\t\t\t\t\t\t----{myAuthors[index]}\n\n", end="")
        print("\t--------------------------------------------------------------", end="")

    @staticmethod
    def checkMyQuote():
        newQuote = input("\n\t\t\tEnter your quote below for search\n\n\t\t\t")
        f = open("quotes list.txt", "r")
        allQuotes = f.read()
        myQuotes = allQuotes.split(".\n")
        f.close()
        
        status = "Sorry, Quote Doesn't exists!"
        for value in myQuotes:
            if newQuote.lower() == value.lower():
                status = "Quote exists!"
                break
        print(f"\n\n\t\t\t{status}")

    @staticmethod
    def main():
        # Creating a file to store all my quotes.
        try:
            open("quotes list.txt", "+x")
            open("authors list.txt", "+x")
        except:
            pass
        
        source = QuotesManagementSystem()
        while True:
            print("\n\n\t\t\tQUOTES MANAGEMENT SYSTEM\n\n\t\t\t\t1. Add\n\t\t\t\t2. Display\n\t\t\t\t3. Check\n")
            option = input("\t\t\tChoose one from Above: ")
            if option == "1":
                source.addQuotes() # For adding new quotes to the list
            elif option == "2":
                source.display() # Display all the Quotes in a very sequencial manner
            elif option == "3":
                source.checkMyQuote() # Check your Quote and Display the result
            elif option == "exit":
                print("\n\n\t\t--------Thank you for using our Application!--------\n\t\t\t\t\t\t\tSee You Again ;)\n\n")
                break
            else:
                print("\n\t\t--------Wrong Input, Please Input Again!--------")

QuotesManagementSystem.main()
