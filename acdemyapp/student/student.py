import csv
class Student:
    def __init__(self,name,course,deposit):
        self.name=name
        self.course=course
        self.deposit=deposit
        self.remaining=20000-deposit
        print("Congratulations,you have been registered successfully..!")

    def store_data(self):
        with open('./student.csv', 'a+', newline='') as file:
            fieldnames = ['name','course','deposit','remaining']
            writer = csv.DictWriter(file,fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'name': f'{self.name}', 'course': f'{self.course}', 'deposit': f'{self.deposit}', 'remaining': f'{self.remaining}'})


