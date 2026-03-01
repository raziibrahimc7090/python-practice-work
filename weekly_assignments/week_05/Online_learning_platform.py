from abc import ABC, abstractmethod


class Course(ABC):
    def __init__(self, course_name, duration):
        self.course_name = course_name
        self.duration = duration

    @abstractmethod
    def course_details(self):
        pass


class ProgrammingCourse(Course):
    def course_details(self):
        print(f"Programming Course: {self.course_name}, Duration: {self.duration}")


class DesignCourse(Course):
    def course_details(self):
        print(f"Design Course: {self.course_name}, Duration: {self.duration}")


class MarketingCourse(Course):
    def course_details(self):
        print(f"Marketing Course: {self.course_name}, Duration: {self.duration}")


c1 = ProgrammingCourse("Python Basics", "4 weeks")
c2 = DesignCourse("UI/UX Design", "3 weeks")
c3 = MarketingCourse("Digital Marketing", "5 weeks")

c1.course_details()
c2.course_details()
c3.course_details()