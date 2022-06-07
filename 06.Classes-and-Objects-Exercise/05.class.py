class Class:
    __students_count = 22

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name, grade):
        if len(self.students) <= Class.__students_count:
            self.students.append(name)
            self.grades.append(grade)
        return

    def get_average_grade(self):
        return sum(self.grades) / len(self.students)

    def __repr__(self):
        avg_sum = self.get_average_grade()
        return f"The students in {self.name}: {', '.join(self.students)}. Average grade: {avg_sum:.2f}"


a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)