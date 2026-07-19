class User:
    def __init__(self,name,email):
        self.name=name
        self.email=email
    def login(self):
        print(f"{self.name} has logged in!")
    def get_role(self):
        return "User"
class Instructor(User):
    def __init__(self,name,email,courses_created):
        super().__init__(name,email)
        self.courses_created=courses_created
    def create_course(self,course_name):
        print(f"{course_name} is created!")
    def get_role(self):
        return "Instructor"
class Student(User):
    def __init__(self,name,email,courses_enrolled):
        super().__init__(name,email)
        self.courses_enrolled=courses_enrolled
    def enroll(self,course_name):
        print(f"{self.name} is enrolled in {course_name}")
    def get_role(self):
        return "Student"
class PremiumFeature:
    def __init__(self):
        self.subscription="Premium"
    def download_course(self,course_name):
        print(f"{course_name} is downloaded!")
    def get_subscription(self):
        return f"{self.subscription}"
class PremiumStudent(Student, PremiumFeature):
    def __init__(self,name,email,courses_enrolled):
        Student.__init__(self,name,email,courses_enrolled)
        PremiumFeature.__init__(self)
    def get_role(self):
        return "Premium Student"
    def show_dashboard(self):
        print(f"Name: {self.name}")
        print(f"Role: {self.get_role()}")
        print(f"Subscription: {self.subscription}")
def show_user_details(user):
    print(f"Name: {user.name}")
    print(f"Role: {user.get_role()}")
a=Instructor("anushka","abc@gmail.com","Data Science")
b=Student("ankush","abc@gmail.com","Science")
c=PremiumStudent("akansha","abc@gmail.com","Data Science")
a.login()
b.login()
c.login()
a.create_course("Data Science")
b.enroll("Science")
c.enroll("Buisness")
c.download_course("Statistics")
c.show_dashboard()
show_user_details(a)
show_user_details(b)
show_user_details(c)
print(c.get_role())