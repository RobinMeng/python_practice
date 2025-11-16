class User:
    """用户类"""

    def __init__(self, user_name, email):
        """初始化"""
        self.user_name = user_name
        self.email = email

    def print_user_info(self):
        """函数"""
        print(f"用户姓名:{self.user_name}\n用户邮箱:{self.email}")


mike = User('mick', 'mick@google.com')
print(mike.user_name)
print(mike.email)
mike.print_user_info()
