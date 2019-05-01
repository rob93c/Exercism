from re import findall

school_class = ["Alice", "Bob", "Charlie", "David",
                "Eve", "Fred", "Ginny", "Harriet",
                "Ileana", "Joseph", "Kincaid", "Larry"]


class Garden(object):

    def __init__(self, diagram, students=school_class):
        self.diagram = [findall("..", row) for row in diagram.split()]
        self.students = sorted(students)

    def plants(self, student):
        index = self.students.index(student)
        plants = self.diagram[0][index] + self.diagram[1][index]
        return plants.replace("G", "Grass ")\
            .replace("C", "Clover ")\
            .replace("R", "Radishes ")\
            .replace("V", "Violets ").strip().split()
