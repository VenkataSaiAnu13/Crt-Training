                     #CONSTRUCTORS

"""class student:
    name=""
    def __init__(self,name):
        print("object created")
        print(name)


s1=student("anu")"""


"""class student:
    studnet_name="no name"         self.studnet_name=new_name
    def __init__(self,name):
        print("object created")
        print(self,student_name)


s1=student("anu")"""


class student:
    studnet_name="no name"
    def __init__(self,name):
        self.student_name=name
    def update_name(self,new_name):
        pass


s1=student("anu")
s2=student("tanu")
s3=student("manu")
print(s2.student_name)


