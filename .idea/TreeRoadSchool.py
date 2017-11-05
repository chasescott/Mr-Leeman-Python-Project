import sys
import pickle
from tkinter import *
from tkinter import messagebox
from Student import Student

#VARIABLES
PIK = "pickle.dat"
students = []
totalCount = Student.counterId
maleStudents = ''
femaleStudents = ''

#CLASS CODE
class TreeRoadSchool:

#CONSTRUCTOR
    def __init__(self, name):
        self.schoolName = "Tree Road School"
        self.loadAllStudents()

#METHODS
    def loginCode(self, userInput, userPW):
        username = "Mr Leeman"
        password = "123456"
        if userInput == username:
            if userPW == password:
                print("Welcome!  Please proceed to use the system.")
                return True
            else:
                print("Password not recognised")
                return False
        else:
            print("That username is not recognised")
            return False


    def logoutFromSystem(self):
        print("You've now been logged out")
        sys.exit


    def addStudent(self, firstName, surname, address, telNumber, DOB, gender, tutorGroup, uniqueEmail):
        with open(PIK, 'ab') as output:
            newStudent = Student(firstName, surname, address, telNumber, DOB, gender, tutorGroup, uniqueEmail)
            pickle.dump(newStudent, output, pickle.HIGHEST_PROTOCOL)
        newStudentAsString = ("Student: {0} {1} has been added under unique ID {2}".format(newStudent.firstName, newStudent.surname, str(newStudent.uniqueId)))
        print(newStudentAsString)


    def addStudentWithPopUp(self, firstName, surname, address, telNumber, DOB, gender, tutorGroup, uniqueEmail):
        with open(PIK, 'ab') as output:
            newStudent = Student(firstName, surname, address, telNumber, DOB, gender, tutorGroup, uniqueEmail)
            pickle.dump(newStudent, output, pickle.HIGHEST_PROTOCOL)
        newStudentAsString = ("Student: {0} {1} has been added under unique ID {2}".format(newStudent.firstName, newStudent.surname, str(newStudent.uniqueId)))
        print(newStudentAsString)
        messagebox.showinfo("Student Added!", newStudentAsString)


    def addEmptyStudent(self, tutorGroup, uniqueEmail):
        with open(PIK, 'ab') as output:
            newStudent = Student.newStudent(tutorGroup, uniqueEmail)
            pickle.dump(newStudent, output, pickle.HIGHEST_PROTOCOL)
        print("OK " + str(newStudent.uniqueId) + "\n")


    def loadAllStudents(self):
        with open(PIK,'rb') as input:
            while 1:
                try:
                    studentExisiting = pickle.load(input)
                except EOFError:
                    break
                students.append(studentExisiting)
        #DEPRECIATED METHOD:  RETAIN IN CASE OF ERRORS!
        # totalCount = Student.counterId
        # x = 1
        # with open(PIK, 'rb') as input:
        #     for x in range (x, totalCount):
        #         studentExisting = pickle.load(input)
        #         students.append(studentExisting)
        #         x += 1
        #         print('Student added: ' + str(len(students)))


    def viewAllStudents(self):
        print('ViewAllStudents array length: ' + str(len(students)))
        allStudents = ''
        for item in students:
            print("Unique Id: " + str(item.uniqueId) + ", Name: " + item.firstName)
            allStudents += "Unique Id: " + str(item.uniqueId) + ", Name: " + item.firstName + ' ' + item.surname + ', Address: ' + item.address + ', Tel: ' + item.telNumber + ', DOB: ' + item.DOB + ', Gender: ' + item.gender + ', Tutor Group: ' + item.tutorGroup + ', Email: ' + item.uniqueEmail + '\n\n'
        return allStudents


    def findAStudent(self, idNumber):
        # x = 1
        #Open the .dat file and append all student objects to students array
        # with open(PIK, 'rb') as input:
        #     for x in range (x, totalCount):
        #         studentExisting = pickle.load(input)
        #         students.append(studentExisting)
        #         x += 1
        #Iterate through the students array to find
        studentInfo = ''
        for item in students:
            if item.uniqueId == idNumber:
                studentInfo = ('The following information has been found for ' + str(item.uniqueId) + ':\n\nName: ' + item.firstName + ' ' + item.surname + '\nAddress: ' + item.address + '\nTel: ' + item.telNumber + '\nDOB: ' + item.DOB + '\nGender: ' + item.gender + '\nTutor Group: ' + item.tutorGroup + '\nEmail: ' + item.uniqueEmail + '\n')
                # print("Student counter is " + str(Student.counterId))
                # print('Array size: ' + str(len(students)))
                return studentInfo
                break


    def clearStudentsArray(self):
        students.clear()
        print('Array cleared.')


    def updateStudent(self, idNumber, firstName, surname, address, telNumber, DOB, gender, tutorGroup, uniqueEmail):
        x = 1
        print('Array length at updateStudent method call = ' + str(len(students)))
        replaceStudent = Student('X','X','X','X','X','X','X','X')
        replaceStudent.replacementStudentInfo(idNumber, firstName, surname, address, telNumber, DOB, gender, tutorGroup, uniqueEmail)
        #Iterate through the students array to find student object by IdNumber
        for n, i in enumerate(students):
            if i.uniqueId == idNumber:
                students[n] = replaceStudent
                print(replaceStudent.firstName + ' ' + replaceStudent.surname)
        print (str(students) + '\n')
        #Write new array to pickle.dat file
        with open(PIK, 'wb') as output:
            for item in students:
                studentId = item.uniqueId
                firstName = item.firstName
                surname = item.surname
                address = item.address
                telNo = item.telNumber
                DOB = item.DOB
                gender = item.gender
                tutorGrp = item.tutorGroup
                emailAddr = item.uniqueEmail
                newStudent = Student('X','X','X','X','X','X','X','X')
                newStudent.replacementStudentInfo(studentId, firstName, surname, address, telNo, DOB, gender, tutorGrp, emailAddr)
                pickle.dump(newStudent, output, pickle.HIGHEST_PROTOCOL)


    def updateStudentWithPopUp(self, idNumber, firstName, surname, address, telNumber, DOB, gender, tutorGroup, uniqueEmail):
        x = 1
        # print('Array length at updateStudent method call = ' + str(len(students)))
        replaceStudent = Student('X','X','X','X','X','X','X','X')
        replaceStudent.replacementStudentInfo(idNumber, firstName, surname, address, telNumber, DOB, gender, tutorGroup, uniqueEmail)
        #Iterate through the students array to find student object by IdNumber
        for n, i in enumerate(students):
            if i.uniqueId == idNumber:
                students[n] = replaceStudent
                print(replaceStudent.firstName + ' ' + replaceStudent.surname)
                messagebox.showinfo("Success!", 'Student record ' + replaceStudent.uniqueId + ' has been updated.\nPlease note the amended reference number.')
                with open(PIK, 'wb') as output:
                    for item in students:
                        studentId = item.uniqueId
                        firstName = item.firstName
                        surname = item.surname
                        address = item.address
                        telNo = item.telNumber
                        DOB = item.DOB
                        gender = item.gender
                        tutorGrp = item.tutorGroup
                        emailAddr = item.uniqueEmail
                        newStudent = Student('X','X','X','X','X','X','X','X')
                        newStudent.replacementStudentInfo(studentId, firstName, surname, address, telNo, DOB, gender, tutorGrp, emailAddr)
                        pickle.dump(newStudent, output, pickle.HIGHEST_PROTOCOL)
                return True
        print ('Student array length at updateStudentWithPopUp method = ' + str(students) + '\n')
        #Write new array with revised replacement student object to pickle.dat file
        # with open(PIK, 'wb') as output:
        #     for item in students:
        #         studentId = item.uniqueId
        #         firstName = item.firstName
        #         surname = item.surname
        #         address = item.address
        #         telNo = item.telNumber
        #         DOB = item.DOB
        #         gender = item.gender
        #         tutorGrp = item.tutorGroup
        #         emailAddr = item.uniqueEmail
        #         newStudent = Student('X','X','X','X','X','X','X','X')
        #         newStudent.replacementStudentInfo(studentId, firstName, surname, address, telNo, DOB, gender, tutorGrp, emailAddr)
        #         pickle.dump(newStudent, output, pickle.HIGHEST_PROTOCOL)


    #Create a report with list of boys or girls only
    def genderListReportFemale(self):
        # print('Students array length: ' + str(len(students)))
        allStudents = '\n<br/><br/>List of female students:  <br/>'
        for item in students:
            if item.gender == 'Female':
                #print("Unique Id: " + str(item.uniqueId) + ", Name: " + item.firstName + ' ' + item.surname)
                allStudents += "\n<br/>Unique Id: " + str(item.uniqueId) + ", Name: " + item.firstName + ' ' + item.surname + ', Address: ' + item.address + ', Tel: ' + item.telNumber + ', DOB: ' + item.DOB + ', Gender: ' + item.gender + ', Tutor Group: ' + item.tutorGroup + ', Email: ' + item.uniqueEmail + '<br/>\n'
        return allStudents


    def genderListReportMale(self):
        # print('Students array length: ' + str(len(students)))
        allStudents = '\n<br/><br/>List of male students:  <br/>'
        for item in students:
            if item.gender == 'Male':
                #print("Unique Id: " + str(item.uniqueId) + ", Name: " + item.firstName + ' ' + item.surname)
                allStudents += "\n<br/>Unique Id: " + str(item.uniqueId) + ", Name: " + item.firstName + ' ' + item.surname + ', Address: ' + item.address + ', Tel: ' + item.telNumber + ', DOB: ' + item.DOB + ', Gender: ' + item.gender + ', Tutor Group: ' + item.tutorGroup + ', Email: ' + item.uniqueEmail + '<br/>\n'
        return allStudents


    def genderListReport(self):
        females = self.genderListReportFemale()
        males = self.genderListReportMale()
        combined = females + males
        return combined


    #Create a report where student details need to be entered:
    def emptyStudentReport(self):
        allStudents = '\n<br/><br/>Students without details that need updating:  <br/>'
        for item in students:
            if not item.firstName:
                allStudents += "<br/>\nUnique Id: " + str(item.uniqueId) + ", Name: " + item.firstName + ' ' + item.surname + '<br/>'
        return allStudents


    #Create a report displaying all student names and email addresses:
    def emailListReport(self):
        allStudents = '\n<br/><br/>List of student email addresses:  <br/>'
        for item in students:
            allStudents += "<br/>\nName: " + item.firstName + ' ' + item.surname + ', Email: ' + item.uniqueEmail + '<br/>\n'
        return allStudents


    #Add 25 students
    def addStudents(self):
        self.addStudent('Anna', 'Peters', '1 The Street', '0982345321', '12/12/2000', 'Female', 'Hildegard 1', '1@gmail.com')
        self.addStudent('Lisa', 'Ash', '12 The Street', '0984654321', '09/09/2001', 'Female', 'Hildegard 2', '2@gmail.com')
        self.addStudent('Ama', 'Jones', '45 The Road', '0934674321', '27/06/1998', 'Female', 'Cassidy 3', '3@gmail.com')
        self.addStudent('Laura', 'James', '16 The Avenue', '0987233321', '23/02/1999', 'Female', 'Cassidy 4', '4@gmail.com')
        self.addStudent('Kelly', 'Kerrs', '24 The Top', '0987222221', '22/02/1997', 'Female', 'Jones 5', '5@gmail.com')
        self.addStudent('Ceila', 'Moora', '70 Market Road', '0982354321', '22/01/1999', 'Female', 'Jones 6', '6@gmail.com')
        self.addStudent('Kate', 'Terry', '55 Market Street', '0983434321', '26/04/2002', 'Female', 'Hildegard 7', '7@gmail.com')
        self.addStudent('Katie', 'Pettie', '77 Coronation Street', '0982323221', '02/06/1999', 'Female', 'Hildegard 8', '8@gmail.com')
        self.addStudent('Kerry', 'Matters', '34 Downing Street', '0987333331', '21/05/1998', 'Female', 'Smith 9', '9@gmail.com')
        self.addStudent('Lesley', 'West', '57 Avenue Street', '0966666621', '21/04/1999', 'Female', 'Smith 0', '0@gmail.com')
        self.addStudent('Matt', 'Peters', '1 The Street', '0982345321', '12/12/2000', 'Female', 'Hildegard 1', '1@gmail.com')
        self.addStudent('Pete', 'Ash', '12 The Street', '0984654321', '09/09/2001', 'Female', 'Hildegard 2', '2@gmail.com')
        self.addStudent('John', 'Jones', '45 The Road', '0934674321', '27/06/1998', 'Female', 'Cassidy 3', '3@gmail.com')
        self.addStudent('Percy', 'James', '16 The Avenue', '0987233321', '23/02/1999', 'Female', 'Cassidy 4', '4@gmail.com')
        self.addStudent('Chris', 'Kerrs', '24 The Top', '0987222221', '22/02/1997', 'Female', 'Jones 5', '5@gmail.com')
        self.addStudent('Sam', 'Moora', '70 Market Road', '0982354321', '22/01/1999', 'Female', 'Jones 6', '6@gmail.com')
        self.addStudent('Ash', 'Terry', '55 Market Street', '0983434321', '26/04/2002', 'Female', 'Hildegard 7', '7@gmail.com')
        self.addStudent('Paul', 'Pettie', '77 Coronation Street', '0982323221', '02/06/1999', 'Female', 'Hildegard 8', '8@gmail.com')
        self.addStudent('Mark', 'Matters', '34 Downing Street', '0987333331', '21/05/1998', 'Female', 'Smith 9', '9@gmail.com')
        self.addStudent('Luke', 'West', '57 Avenue Street', '0966666621', '21/04/1999', 'Female', 'Smith 0', '0@gmail.com')
        self.addStudent('John', 'Johnson', 'New York', '935', '16/04/1998', 'Male', 'Marx 1', 'me@me.com')
        self.addStudent('Kenny', 'Dope', 'Boston', '934', '03/11/1976', 'Male', 'Marx 1', 'me@me.com')
        self.addStudent('Todd', 'Edwards', 'Paris', '349', '05/01/1981', 'Male', 'Lush 1', 'me@me.com')
        self.addStudent('Gilly', 'Cooper', 'Canterbury', '456', '01/09/1986', 'Female', 'Kenny 1', 'me@me.com')
        self.addStudent('Alexandra', 'Kessie', 'London', '123', '19/07/1999', 'Female', 'Luke 1', 'me@me.com')

    #Add 5 empty students
    def addEmptyStudents(self):
        self.addEmptyStudent('Cassidy','1@1.com')
        self.addEmptyStudent('Cassidy','2@1.com')
        self.addEmptyStudent('Cassidy','3@1.com')
        self.addEmptyStudent('Cassidy','4@1.com')
        self.addEmptyStudent('Cassidy','5@1.com')




