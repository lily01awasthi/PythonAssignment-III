from acdemyapp.student.student import Student
import csv
import pandas as p


class Academy:
    course_list = ['python', 'java', 'JavaScript', 'Django', 'php']

    def menu(self):
        print("welcome...!")
        print("""
        1.Inquiry courses/Register 
        2.Display students
        3.Update student info
        4.Release Student 
        you can press any other key to exit.
        """)
        choice = int(input("please enter your choice(1/2/3/4),press any other integers to exit: "))

        if choice == 1:
            a1.view_course()
        elif choice == 2:
            a1.display_students()
        elif choice == 3:
            a1.update_student()
        elif choice == 4:
            a1.Release_student()
        else:
            print("visit again")

    def view_course(self):
        print("we have following courses available at 20000.you can also do payment in installment for these courses.")
        for i in range(len(self.course_list)):
            print(f"{i + 1}.{self.course_list[i]}")
        try:
            choose = int(input("type the course number,if you want to register for that course otherwise you can "
                               "enter any other integer key to exit: "))
            for i in range(len(self.course_list) + 1):
                if choose == i:
                    print(f"you choose course {self.course_list[i - 1]}...!")
                    self.register(self.course_list[i - 1])
                    self.menu()
        except ValueError:
            print("thanks for vising")

    def register(self, course, deposit=20000):
        name = input("enter your name: ")
        print("would you like to deposit partial or full payment for now?:")
        ch = int(input("choose 1 partial(10,000) \n press any for full(20000): "))
        if ch == 1:
            deposit = 10000
        reg = Student(name, course, deposit)
        reg.store_data()

    def display_students(self):
        content = p.read_csv('student.csv')
        print(content)

    def update_student(self):
        self.display_students()
        temp=[]
        row=input("enter the name key you would like to update: ")
        with open('student.csv','r',newline='') as file:
            reader = csv.reader(file)
            titles = next(reader)
            for i in reader:
                temp+=[i]
            for i in temp:
                if i[0]==row:
                    name=input("enter your name: ")
                    course=input("enter your course: ")
                    deposit=int(input("enter your deposit amount: "))
                    i[0]=name
                    i[1]=course
                    i[2]=deposit
        with open("student.csv",'w',newline='') as file:
            writer=csv.writer(file)
            writer.writerow(titles)
            writer.writerows(temp)
            print("you have successfully updated the data.")
        self.menu()

    def Release_student(self):
        self.display_students()
        temp = []
        row = input("enter the name key you would like to delete: ")
        with open('student.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            titles = next(reader)
            for i in reader:
                temp += [i]
            for i in temp:
                if i[0] == row:
                    temp.remove(i)
        with open("student.csv", 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(titles)
            writer.writerows(temp)
            print("u have successfully removed the data.")
        self.menu()


a1 = Academy()
a1.menu()


