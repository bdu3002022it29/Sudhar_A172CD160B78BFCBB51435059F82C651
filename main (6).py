class Student:

  def __init__(self, name, roll_number, cgpa): 
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students (student_list):

# Sort the list of students in descending orders of cgpa

  sorted_students = sorted(student_list, key=lambda Student: Student.cgpa, reverse=True)

#syntax - lambda arg:exp
  return sorted_students


# example
Students = [
  Student("Abi","AB1",7.8),
  Student("Ram","AB2",8.9),
  Student("Mani","AB3",9.1),
  Student("Abar","AB4",9.9),
]


sorted_students = sort_students(Students)
# print
for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA:{}}".format(student.name,student.roll_number,student.cgpa))