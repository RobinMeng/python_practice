## super class

class User:
    """用户类"""

    def __init__(self, user_name, email):
        """初始化"""
        self.user_name = user_name
        self.email = email

    def print_user_info(self):
        """函数"""
        print(f"用户姓名:{self.user_name}\n用户邮箱:{self.email}")


class Student(User):
    def __init__(self, score, *args):
        self.score = score
        super().__init__(*args)
        pass

    def print_student_info(self):
        print(f"student info \nname:{self.user_name}\nemail:{self.email}\nscore:{self.score}")


xiaoming = Student('59', 'xiaoming', 'xiaoming@gmail.com')

xiaoming.print_student_info()
