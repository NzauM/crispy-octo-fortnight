from models import create_engine, sessionmaker, Base, Teacher
from faker import Faker
import random

engine = create_engine('sqlite:///schools.db')
Base.metadata.create_all(engine)

sessioncreator = sessionmaker(bind=engine)
mysession = sessioncreator()

fakedata = Faker()

if __name__ == '__main__':

    print("Seeding Teachers")
    mysession.query(Teacher).delete()
    # mysession.query(Teacher).filter_by(id==2).first().delete()
    mysession.commit()

    # retrieve the teachers
    # create each teacher as an instance
    # add that instance to the session and commit session

    # What is the teachers name: 
    # What is their Id number: 


    for i in range(10):
        # create a teacher instance, add it to session and commit session
        teacher = Teacher(name=fakedata.name(), id_no=random.randrange(100000, 10000000))
        mysession.add(teacher)
    mysession.commit()

    print("All teachers Seeded, They should now be in your Database")

