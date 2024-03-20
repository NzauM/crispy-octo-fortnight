from functionalities import list_teachers, add_teacher
def main():
    while True:
        print("1. To see all teachers")
        print("2. To add a teacher")
        print("3. To exit the application")
        userschoice = input("What do you want to do?")
        if userschoice == "1":
            # list all teachers
            list_teachers()
            input("Press Enter to Continue")
        elif userschoice == "2":
            add_teacher()
            input("Press Enter to Continue")
        elif userschoice == "3":
            print("Exiting App, Byee")
            return 0
        else:
            print("Invalid Choice")
        

        # return 0


if __name__ == '__main__':
    main()

