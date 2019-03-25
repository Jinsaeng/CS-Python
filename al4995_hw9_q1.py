class Student:
    def __init__(self, name, NYU_id, net_id):
        self.name = name
        self.nyu = NYU_id
        self.net = net_id
        self.grade_list = []

    def add_grade(self, catalog_name, grade):
        new_grade = (catalog_name, grade)
        self.grade_list.append(new_grade)
    def average(self):
        grade = 0
        count = 0
        for num in self.grade_list:
            if (len(num[1]) > 0 and num[1] != "\n"):
                grade += int(num[1])
                count += 1
        avg = int(grade/count)
        return avg
    def get_email(self):
        return self.net + "@nyu.edu"
##    def __repr__(self):
##        return str(self.get_email())
    
def load_students(student_data_filename):
    file = open(students_data_filename , "r");
    for line in file:
        if len(line) != 0:
            string = line.split(",")
            return string
    file.close
def generate_performance_report(student, out_filename):
    student_list = student.nyu + "," + str(student.average())
    return student_list
def generate_course_mailing_list(student, catalog_name,out_filename2):
    for course in student.grade_list:
        if course[0] == catalog_name and len(course[1]) > 0 and course[1] != "\n":
            email_list = student.get_email()
            return email_list
            

def main():
    students_data_filename = "studentgrades.csv"
    out_filename = "studentavg.txt"
    out_filename2 = "CS-UY 1114.txt"
    out3 = open("MA-UY 1024.txt", "w")
    out4 = open("EG-UY 1001.txt", "w")
    out5 = open("EG-UY 1003.txt", "w")
    out6 = open("CS-UY 1122.txt", "w")
    out7 = open("CS-UY 1134.txt", "w")
    out8 = open("MA-UY 1124.txt", "w")
    out_3 = "MA-UY 1024.txt", "w"
    out_4 = ("EG-UY 1001.txt", "w")
    out_5 = ("EG-UY 1003.txt", "w")
    out_6 = ("CS-UY 1122.txt", "w")
    out_7 = ("CS-UY 1134.txt", "w")
    out_8 = ("MA-UY 1124.txt", "w")
    file2  = open(out_filename, "w")
    file3 = open(out_filename2, "w")
    file = open(students_data_filename, "r");
    inside = file.readline()
    print("NYU ID, Average", file=file2)
    for line in file:
        if len(line) != 0:
            parts = line.split(",")
            NYU_id = parts[0]
            name = parts[1]
            net_id = parts[2]
            student = Student(name, NYU_id, net_id)
            student.add_grade("CS-UY 1114",parts[3])
            student.add_grade("MA-UY 1024",parts[4])
            student.add_grade("EG-UY 1001",parts[5])
            student.add_grade("EG-UY 1003",parts[6])
            student.add_grade("CS-UY 1122",parts[7])
            student.add_grade("CS-UY 1134",parts[8])
            student.add_grade("MA-UY 1124", parts[9])
            print(generate_performance_report(student, out_filename), file = file2)

            print(generate_course_mailing_list(student, "CS-UY 1114", out_filename2), file= file3)
            print(generate_course_mailing_list(student, "MA-UY 1024", out_3), file= out3)
            print(generate_course_mailing_list(student, "EG-UY 1001", out_4), file= out4)
            print(generate_course_mailing_list(student, "EG-UY 1003", out_5), file= out5)
            print(generate_course_mailing_list(student, "CS-UY 1122", out_6), file= out6)
            print(generate_course_mailing_list(student, "CS-UY 1134", out_7), file= out7)
            print(generate_course_mailing_list(student, "MA-UY 1124", out_8), file= out8)
            
            
            
##    load_students(students_data_filename)
##            print(repr(student.average))
##            print(repr(student.get_email))
main()

    
