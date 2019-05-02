class School(object):

    def __init__(self):
        self.all = {}

    def add_student(self, name, grade):
        self.all[name] = grade

    def roster(self) -> list:
        lst = sorted([key for key in self.all.keys()])
        lst.sort(key=lambda x: self.all[x])
        return lst

    def grade(self, grade_number) -> list:
        return sorted([name for name in self.all if self.all[name] == grade_number])
