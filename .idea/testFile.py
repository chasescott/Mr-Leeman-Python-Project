import sys
import pickle
import PyPDF2
import io
from TreeRoadSchool import TreeRoadSchool
from Student import Student

import time
import os
import webbrowser
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import portrait
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

class testFile:

    def __init__(self):
        testFile.name = "TEST FILE"

def test():
        print('CHASE:  Creating a new Tree Road School Object...')
        #Create a new Tree Road School Class object
        newSchool = TreeRoadSchool("SCHOOL TEST")
        #Log in to the school system
        print('CHASE:  Logging onto the system...')
        newSchool.loginCode("Mr Leeman", "123456")
        #Adding 20 new students (10 female)
        print('CHASE:  Adding 20 new students...')
        newSchool.addStudent('Anna', 'Peters', '1 The Street', '0982345321', '12/12/2000', 'Female', 'Hildegard 1', '1@gmail.com')
        newSchool.addStudent('Lisa', 'Ash', '12 The Street', '0984654321', '09/09/2001', 'Female', 'Hildegard 2', '2@gmail.com')
        newSchool.addStudent('Ama', 'Jones', '45 The Road', '0934674321', '27/06/1998', 'Female', 'Cassidy 3', '3@gmail.com')
        newSchool.addStudent('Laura', 'James', '16 The Avenue', '0987233321', '23/02/1999', 'Female', 'Cassidy 4', '4@gmail.com')
        newSchool.addStudent('Kelly', 'Kerrs', '24 The Top', '0987222221', '22/02/1997', 'Female', 'Jones 5', '5@gmail.com')
        newSchool.addStudent('Ceila', 'Moora', '70 Market Road', '0982354321', '22/01/1999', 'Female', 'Jones 6', '6@gmail.com')
        newSchool.addStudent('Kate', 'Terry', '55 Market Street', '0983434321', '26/04/2002', 'Female', 'Hildegard 7', '7@gmail.com')
        newSchool.addStudent('Katie', 'Pettie', '77 Coronation Street', '0982323221', '02/06/1999', 'Female', 'Hildegard 8', '8@gmail.com')
        newSchool.addStudent('Kerry', 'Matters', '34 Downing Street', '0987333331', '21/05/1998', 'Female', 'Smith 9', '9@gmail.com')
        newSchool.addStudent('Lesley', 'West', '57 Avenue Street', '0966666621', '21/04/1999', 'Female', 'Smith 0', '0@gmail.com')
        #And 10 male students...
        newSchool.addStudent('Matt', 'Peters', '1 The Street', '0982345321', '12/12/2000', 'Male', 'Hildegard 1', '1@gmail.com')
        newSchool.addStudent('Pete', 'Ash', '12 The Street', '0984654321', '09/09/2001', 'Male', 'Hildegard 2', '2@gmail.com')
        newSchool.addStudent('John', 'Jones', '45 The Road', '0934674321', '27/06/1998', 'Male', 'Cassidy 3', '3@gmail.com')
        newSchool.addStudent('Percy', 'James', '16 The Avenue', '0987233321', '23/02/1999', 'Male', 'Cassidy 4', '4@gmail.com')
        newSchool.addStudent('Chris', 'Kerrs', '24 The Top', '0987222221', '22/02/1997', 'Male', 'Jones 5', '5@gmail.com')
        newSchool.addStudent('Sam', 'Moora', '70 Market Road', '0982354321', '22/01/1999', 'Male', 'Jones 6', '6@gmail.com')
        newSchool.addStudent('Ash', 'Terry', '55 Market Street', '0983434321', '26/04/2002', 'Male', 'Hildegard 7', '7@gmail.com')
        newSchool.addStudent('Paul', 'Pettie', '77 Coronation Street', '0982323221', '02/06/1999', 'Male', 'Hildegard 8', '8@gmail.com')
        newSchool.addStudent('Mark', 'Matters', '34 Downing Street', '0987333331', '21/05/1998', 'Male', 'Smith 9', '9@gmail.com')
        newSchool.addStudent('Luke', 'West', '57 Avenue Street', '0966666621', '21/04/1999', 'Male', 'Smith 0', '0@gmail.com')
        #Add 5 students without full details...
        print("CHASE:  Adding 5 new students without full details...")
        newSchool.addEmptyStudent('Smethwick9','1@mail.com')
        newSchool.addEmptyStudent('Smethwick8','2@mail.com')
        newSchool.addEmptyStudent('Warwick9','3@mail.com')
        newSchool.addEmptyStudent('Warwick8','4@mail.com')
        newSchool.addEmptyStudent('Perry5','5@mail.com')
        #View all students
        print('CHASE:  Loading all students to view...')
        newSchool.loadAllStudents()
        newSchool.viewAllStudents()
        #Clear students array
        print('CHASE:  Clearing the students array...')
        newSchool.clearStudentsArray()
        print('CHASE:  Loading all students again...')
        #Locate 5 specific students
        newSchool.loadAllStudents()
        #Find specific students
        print('CHASE:  Find 5 specific students...')
        newSchool.findAStudent(2)
        newSchool.findAStudent(8)
        newSchool.findAStudent(13)
        newSchool.findAStudent(22)
        newSchool.findAStudent(18)
        print('CHASE:  Clear students array and reload all students...')
        newSchool.clearStudentsArray()
        newSchool.loadAllStudents()
        #View all students
        print('CHASE:  View All Students...')
        newSchool.viewAllStudents()
        #Updating 3 students...
        print('CHASE:  Updating student 1...')
        #newSchool.updateStudent(1, 'Kim', 'Jong Un', 'Pyongyang', '999', '01/01/1980', 'Male', 'DPK 1', 'me@jong.com')
        print('CHASE:  Updating student 2...')
        #newSchool.updateStudent(2, 'Margaret', 'Thatcher', 'London', '999', '01/01/1925', 'Female', 'Thatcher 1', 'me@thatcher.com')
        print('CHASE:  Updating student 3...')
        #newSchool.updateStudent(3, 'Karl', 'Marx', 'Moscow', '999', '01/01/1900', 'Male', 'Marx 1', 'me@marx.com')
        #Update students 21 - 25
        print('CHASE: Updating students 21 to 25...')
        #newSchool.updateStudent(21, 'John', 'Johnson', 'New York', '935', '16/04/1998', 'Male', 'Marx 1', 'me@me.com')
        #newSchool.updateStudent(22, 'Kenny', 'Dope', 'Boston', '934', '03/11/1976', 'Male', 'Marx 1', 'me@me.com')
        #newSchool.updateStudent(23, 'Todd', 'Edwards', 'Paris', '349', '05/01/1981', 'Male', 'Lush 1', 'me@me.com')
        #newSchool.updateStudent(24, 'Gilly', 'Cooper', 'Canterbury', '456', '01/09/1986', 'Female', 'Kenny 1', 'me@me.com')
        #newSchool.updateStudent(25, 'Alexandra', 'Kessie', 'London', '123', '19/07/1999', 'Female', 'Luke 1', 'me@me.com')
        #View all students
        print('CHASE:  Displaying All Students... Have they updated?')
        newSchool.viewAllStudents()
        print('CHASE:  Displaying students by Gender...')
        # print(newSchool.genderListReportFemale())
        # print(newSchool.genderListReportMale())
        print(newSchool.genderListReport())
        print(newSchool.emailListReport())
        print(newSchool.emptyStudentReport())
        # #Logout from the system
        # print('CHASE:  Logout from the system...')
        # newSchool.clearStudentsArray()
        # newSchool.logoutFromSystem()
        writeString("Report-Gender.pdf",newSchool.genderListReport())
        writeString("Report-Missing.pdf",newSchool.emptyStudentReport())
        writeString("Report-Email.pdf",newSchool.emailListReport())


def writeString(fileName,insertString):
        doc = SimpleDocTemplate(fileName,pagesize=letter,
                                rightMargin=72,leftMargin=72,
                                topMargin=72,bottomMargin=18)
        Story=[]
        logo = "../.idea/images/school.gif"

        formatted_time = time.ctime()

        im = Image(logo, 2*inch, 2*inch)
        Story.append(im)

        styles=getSampleStyleSheet()
        styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
        ptext = '<font size=12>%s</font>' % formatted_time

        Story.append(Paragraph(ptext, styles["Normal"]))
        Story.append(Spacer(1, 12))

        ptext = insertString

        Story.append(Paragraph(ptext, styles["Justify"]))
        Story.append(Spacer(1, 12))

        ptext = '<font size=12>--- END OF REPORT ---</font>'
        Story.append(Paragraph(ptext, styles["Normal"]))
        Story.append(Spacer(1, 12))
        doc.build(Story)
        if os.name == 'nt':
                os.system("start "+fileName)
        elif os.name == 'posix':
                os.system("open "+fileName)
        elif os.name == 'mac':
                os.system("open "+fileName)
        else:
                os.sysconf("open "+fileName)


test()
