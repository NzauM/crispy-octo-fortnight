from seeds import mysession
from models import Teacher
def list_teachers():
    print("Hereeeee")
    # print a list of all teachers
    myteachers = mysession.query(Teacher).all()
    for teacher in myteachers:
        print(teacher.name)
    pass

def add_teacher():
    # takes in teacher name and id_no and adds them to the database
    teacher_name = input("Enter Teachers name:")
    tr_id_no = input("Enter Teacher's Id Number:")
    teacher = Teacher(name=teacher_name, id_no=tr_id_no)
    mysession.add(teacher)
    mysession.commit()
    print(f"New Teacher {teacher_name} Created Successfully")
