##class Person:
##    def __init__ (self, person, hobbies):
##        self.person = [];
##        self.hobbies = hobbies;
##    def add_person(self):
##        name = input("Please enter the name: ");
##        age = int(input("Please enter the age: "));
##        ls = [name, age]
##        self.person.append(ls)
### the positions will coincide with the name and age of the same person
##    def add_hobby(self):
##        name = input("Who is receiving a new hobby? ")
##        newhobby = input("what is this person's new hobby? ")
##        for person in self.person:
##            if name == person[0]:
##                person.append(newhobby)
####    def delete_hobby(self):
##        
##    def birthday(self):
##        name = input("Who is having a birthday? ")
##        for person in self.person:
##            if name == person[0]:
##                print("Happy birthday,", name)
##    def __repr__(self):
##        output = "\n"
##        for item in self.person:
##            output += "Name: " + item[0] + "\n"
##            output += "Age: " + item[1] + "\n"
##            output += "Hobbies: " + "\n"
##            for hobby in item:
##                output += hobby + "\n"
##        
##        
##def main():
##    start = True
##    while start:
##        print("Select one of the following options: ");
##        print("==========================");
##        print("1. Create a new Person")
##        print("2. Add to an exisiting person's hobbies")
##        print("3. Delete an existing person's hobby")
##        print("4. Someone has a birthday")
##        print("5. See a list of people")
##        print("6. Exit")
##        answer = input();
##        if answer == "1":
##            Person.add_person();
##        elif answer == "2":
##            newHobby = Person.add_hobby()
####        elif answer == "3":
##        elif answer == "4":
##            birthday = Person.birthday
##        elif answer == "5":
##            print(repr(Person))
##        else:
##            start = False
##    print("Goodbye!")
##main()
##


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.hobbies = []
    def addhobby(self,hobby):
        if hobby not in self.hobbies:
            self.hobbies.append(hobby)
    def deletehobby(self,hobby):
        self.hobbies.remove(hobby)
    def birthday(self):
        return "Happy birthday " + self.name
    def __repr__(self):
        return "Name: " + str(self.name) + "\n" + "Age: " + str(self.age) +"\n" + "Hobbies: \n" + str(self.hobbies)
def main():
    people = [];
    start = True;
    while start:
        print("Select one of the following options: ");
        print("==========================");
        print("1. Create a new Person")
        print("2. Add to an exisiting person's hobbies")
        print("3. Delete an existing person's hobby")
        print("4. Someone has a birthday")
        print("5. See a list of people")
        print("6. Exit")
        answer = input()
        if answer == "1":
            name = input("What is the person's name? ")
            age = int(input("What is the person's age? "))
            people.append(Person(name, age))
        elif answer == "2":
            name = input("Who is getting a new hobby? ")
            hobby = input("What is the person's new hobby? ")
            for per in people:
                if per.name == name:
                      per.addhobby(hobby)
        elif answer == "3":
            name = input("Who is losing their hobby? ")
            hobby = input("What is that person's hobby? ")
            for per in people:
                if per.name == name:
                      per.deletehobby(hobby)
        elif answer == "4":
            name = input("Whose birthday is it? ")
            for per in people:
                    if per.name == name:
                      print(per.birthday())
        elif answer == "5":
            for per in people:
                print(repr(per))
        else:
            start = False
    print("Goodbye!")
main()
