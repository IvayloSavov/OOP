from abc import abstractmethod


class StudentTaxes:
    def __init__(self, name, semester_fee, average_grade):
        self.name = name
        self.semester_fee = semester_fee
        self.average_grade = average_grade

    @abstractmethod
    def get_discount(self):
        pass


class ExcellentStudent(StudentTaxes):
    def get_discount(self):
        return self.semester_fee * 0.4


class AverageStudent(StudentTaxes):
    def get_discount(self):
        return self.semester_fee * 0.3


student = StudentTaxes("Ivo", 250, 5.00)
print(student.semester_fee)