##class Pencil:
##    def __init__(self, eraser):
##        self.eraser = eraser
##    def eraser(self):
##        print(self.eraser)
##
##class WriteTool:
##    def __init__(self,color,shape,brand,medium):
##        self.color = color
##        self.shape = shape
##        self.brand = brand
##        self.medium = medium
##    def write(self):
##        print(self.eraser)
##    def __str__(self):
##        return str(self.medium)
##def main():
##    pencilA = Pencil(False)
##    tool = WriteTool("blue", "cylinder", "bic", pencilA)
##    WriteTool.write(pencilA)
##main()
##
##
##


##class Calendar:
##    def __init__(self, date, day,todo):
##        self.mon = int(date[0:1])
##        self.date = int(date[2:3])
##        self.yr = int(date[4:7])
##        self.dow = day
##        self.todo = todo
##        
##    def start_new_day(self,date,day):
##
##        newd = self.d + 1
##        if newd > 31 and self.mon %2 == 1:
##            newd -= 30
##            nmon = self.mon+ 1
##        elif (newd > 30) and (self.mon == 12):
##            newd -= 29
##            nmon = self.mon + 11
##            nyr = self.yr + 1
##            #December 31th + 1 day = January 1st + 1yr
##        elif (newd > 30) and (self.mon %2 == 0):
##            newd -=29
##            nmon = self.mon + 1
##            #February 31st + 1 day = March 1st
##        if self.dow == 1:
##            nday = "Tuesday"
##        elif self.dow == 2:
##            nday = "Wednesday"
##        elif self.dow == 3:
##            nday = "Thursday"
##        elif self.dow == 4:
##            nday = "Friday"
##        elif self.dow == 5:
##            nday = "Saturday"
##        elif sefl.dow == 6:
##            nday = "Sunday"
##        else:
##            nday = "Monday"
##        print("Today's date is: ", nday, nmon, "/", newd, "/", nyr)
##        
##    def __repr__(self):
##        print("Today's date is:" + str(self.dow) + str(self.mon) + "/" + str(self.date) +"/" + str(self.yr))
##        print("Today's Accomplishment")
##        print("==================")
##        print("Things left to do")
##        print("==================")
##        print(repr(self.todo))
##        
##        
##class ToDoList:
##    def __init__(self, name, progress):
##        self.name = name
##        self.progress = progress
##        
##    def create_to_do_list_item(self):
##        ls = []
##        self.name =input("Enter the task: ")
##        ls.append(self.name)
##    def check_to_do_list_item(self, ls):
##        ls2 = []
##        for item in ls:
##            print("Did you do", item, "? (y/n)", input())
##            if input() == "y":
##                ls2.append(item)
##        print("Updated To-Do List: ")
##        print("Today's Accomplishment")
##        print("==================")
##        for item in ls:
##            print(item)
##        print("Things left to do")
##        print("==================")
##        
##    def __repr__(self):
##        return repr(create_to_do_list_item(self))
##        
##def main():
##    date = input("Please enter today's date (mmddyyyy): ")
##    day = input("please enter the day of the week: ")
##    calendar = Calendar(date,day)
##    while True:
##        print("\nMain Menu:")
##        print("1. Create New Calendar")
##        print("2. Add To-Do List Item")
##        print("3. Check Off To-Do List")
##        print("4. Show Today's Calendar")
##        print("5. Start The Next Day\n")
##        answer = input("What would you like to do? ")
##        if answer == '1':
##            calendar = Calendar()
##        elif answer == '2':
##            calendar.ToDoList.create_to_do_list_item()
##        elif answer == '3':
##            calendar.ToDoList.check_to_do_list()
##        elif answer == '4':
##            print(repr(calendar))
##        elif answer == '5':
##            calendar.start_new_day()
##main()
##    
##

class Calendar:
    def __init__(self, date, day):
        ls = date.split("/")
        self.day = ls[1]
        self.month = ls[0]
        self.year = ls[2]
        self.day_of_the_week = day
        self.to_do_list = ToDoList()
        
    def start_new_day(self):
        self.day_of_the_week = (self.day_of_the_week+1)%7
        day = self.day + 1
        self.day = int(day %30)
        self.month += int(day //30)
        self.year += int(self. month //12)
        self.month = int(self.month%12)
        
    def __reprr__(self):
        if self.day_of_the_week == 1:
            day = "Monday"
        elif self.day_of_the_week == 2:
            day = "Tuesday"
        elif self.day_of_the_week == 3:
            day = "Wednesday"
        elif self.day_of_the_week == 4:
            day = "Thursday"
        elif self.day_of_the_week == 5:
            day = "Friday"
        elif self.day_of_the_week == 6:
            day = "Saturday"
        elif self.day_of_the_week == 7:
            day = "Sunday"
        output = "Today's date is: " +str(day) + str(self.month) +"/" + str(self.day) + "/" + str(self.year)
        return output + repr(self.to_do_list)
        

class ToDoList:
    def __init_(self):
        self.tasks = []
        self.finished = []
    def create_to_do_list_item(self):
        tasks = input("Please enter a new task: ")
        self.tasks.append(tasks)
    def check_to_do_list(self):
        i = 0
        while i < len(self.tasks):
            progress = input("Did you complete " +self.tasks[i] + " ? (y/n): ")
            if progress == "y":
                self.finished.append(self.tasks.pop(i))
    def __repr__(self):
        output = "Today's Accomplishments/n============\n"
        for item in self.finished:
            output += item + "\n"
        output +=  "Thing's Left To Do\n============\n"
        for item in self.tasks:
            output += item + "\n"
        return output
        
def main():
    date = input("Please enter today's date (mmddyyyy): ")
    day = input("please enter the day of the week: ")
    calendar = Calendar(date,day)
    while True:
        print("\nMain Menu:")
        print("1. Create New Calendar")
        print("2. Add To-Do List Item")
        print("3. Check Off To-Do List")
        print("4. Show Today's Calendar")
        print("5. Start The Next Day\n")
        answer = input("What would you like to do? ")
        if answer == '1':
            calendar = Calendar()
        elif answer == '2':
            calendar.to_do_list.create_to_do_list_item()
        elif answer == '3':
            calendar.to_do_list.check_to_do_list()
        elif answer == '4':
            print(repr(calendar))
        elif answer == '5':
            calendar.start_new_day()
main()















