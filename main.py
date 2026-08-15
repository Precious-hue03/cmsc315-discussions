class Person:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        pass

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
        pass


class Student(Person):
    school_name = "Generic University"

    def __init__(self, name: str, age: int, student_id):
        super().__init__(name, age)
        self.student_id = student_id

        self.courses = []
        pass

    def enroll_course(self, course_name: str):
        self.courses.append(course_name)
        pass

    def display_info(self):
        courses_string = ", " .join(self.courses)

        print(f"Name: {self.name}, Age: {self.age},"
              f" ID: {self.student_id}, School: {self.school_name},"
              f" Courses: [{courses_string}]" )
        pass

# --- Demonstration code ---
if __name__ == "__main__":
    p = Person("Daniel", 28)
    p.display_info()
    pass

    s = Student("Aaliyah", 21, "S9876")
    s.enroll_course("Biology")
    s.enroll_course("Chemistry")
    s.display_info()
    pass

    s2 = Student("Elijah", 65, "S2222")
    s2.display_info()

    Student.school_name = "Tech Institute"
    s.display_info()
    s2.display_info()
    pass