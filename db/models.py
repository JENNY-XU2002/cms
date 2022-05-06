class Participator:  # 教师，学生，管理员有很多共同部分，为这三个类创建共同父类
    def __init__(self, name: str, number: str, age: int, school: str):  # 初始化方法传入姓名，学号，年龄，学校
        self.name = name
        self.number = number
        self.age = age
        self.school = school

    def set_info(self, name, number: str, age: int, school: str) -> None:  # 创建方法用于修改个人信息
        self.name = name
        self.number = number
        self.age = age
        self.school = school

    def get_info(self) -> dict:  # 创建方法返回个人信息
        return {'name': self.name, 'number': self.number, 'age': self.age, 'school': self.school}


class Student(Participator):  # 创建学生类，继承Participator
    count = 0  # 创建一个类属性count用于记录学生实例数量

    def __init__(self, name, number, age, school):
        Student.count += 1  # 每创建一个实例就将类属性count+1
        super().__init__(name, number, age, school)  # 直接继承父类的方法


class Teacher(Participator):  # 创建教师类
    count = 0  # 创建一个类属性count用于记录教师实例数量

    def __init__(self, name, number, age, school):
        Teacher.count += 1  # 每创建一个实例就将类属性count+1
        super().__init__(name, number, age, school)  # 直接继承父类的方法


class Administrator(Participator):  # 创建管理员类
    count = 0  # 创建一个类属性count用于记录管理员实例数量

    def __init__(self, name, number, age, school):
        super().__init__(name, number, age, school)


class School:
    def __init__(self):
        pass


class Course:
    def __init__(self):
        pass
