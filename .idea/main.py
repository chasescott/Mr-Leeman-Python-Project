import sys
import io
import time
import os
import PyPDF2
# from Student import *
# from TreeRoadSchool import *
import pickle
from tkinter import *
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText

from TreeRoadSchool import TreeRoadSchool
from Student import Student

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import portrait
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

newSchool = TreeRoadSchool("Tree Road School")
username = ''
psWord = ''
root = Tk()
PIK = "pickle.dat"
answer = "OK"

class Main:


    def __init__(self, master):
        root.title("Tree Road School System")
        self.textPad = ScrolledText(root, relief=SUNKEN, width=80, height=20)
        self.genderBtn = Button(None, text='Gender Report', width=20, justify=CENTER, command = lambda: self.genderReport())
        self.emailBtn = Button(None, text='Email Report', width=20, justify=CENTER, command = lambda: self.emailListReport())
        self.houseBtn = Button(None, text='Missing Details Report', width=20, justify=CENTER, command = lambda: self.missingDetailsReport())
        self.locateBtn = Button(None, text='Search', command = lambda: self.locateAStudent())
        self.saveBtn = Button(None, text='Save', command = lambda: self.addNewStudent())
        self.updateBtn = Button(None, text='Update', command = lambda: self.updateStudent())
        self.quitBtn = Button(None, text='Quit', command = lambda: self.logoutCheck())
        self.loginBtn = Button(None, text='Login', command = lambda: self.getUserAndPassword())
        self.logoutBtn = Button(None, text='Logout', command = lambda: self.logoutCheck())
        self.updateIdEntry = Entry(bg='white', relief=SUNKEN, width = 20, justify = CENTER)
        self.entry1 = Entry(bg='white', relief=SUNKEN, width = 20, justify = CENTER, textvariable = username)
        self.entry2 = Entry (show = "*", bg='white', relief=SUNKEN, width = 20, justify = CENTER, textvariable = psWord)
        self.logo = PhotoImage(file="../.idea/images/school.gif")
        self.locateLbl = Label(text="Enter the student ID:", width = 20, justify = CENTER)
        self.pwLbl = Label(text="Please enter your password", width = 20, justify = CENTER)
        self.updateIdTitleLbl = Label(text='''To update a student's details, please complete 
        the fields below including the student ID.''', padx = 20, font = "Verdana 14", width = 60, justify = CENTER)
        self.updateIdLbl = Label(text="Unique ID", width = 20, justify = CENTER)
        self.userLbl = Label(text="Please enter your username", width = 20, justify = CENTER)
        self.logoLbl = Label(image=self.logo, padx = 20, justify = CENTER)
        self.userLbl = Label(text="Please enter your username", width = 20, justify = CENTER)
        self.welcomeLbl = Label(text="""\nWelcome to the Tree Road School System.\n""", padx = 20, font = "Verdana 16 bold",justify = CENTER,width=60)
        self.uniqueId = Entry(bg='white', relief=SUNKEN, width = 20, justify = CENTER)
        self.firstName = Entry(bg='white', relief=SUNKEN, width = 20, justify = CENTER)
        self.surname = Entry(bg='white', relief=SUNKEN, width = 20, justify = CENTER)
        self.address = Entry(bg='white', relief=SUNKEN, width = 20, justify = CENTER)
        self.telNumber = Entry(bg='white', relief=SUNKEN, width = 20, justify = CENTER)
        self.DOB = Entry(bg='white', relief=SUNKEN, width = 20, justify = CENTER)
        self.gender = Entry(bg='white', relief=SUNKEN, width = 20, justify = CENTER)
        self.tutorGroup = Entry(bg='white', relief=SUNKEN, width = 20, justify = CENTER)
        self.uniqueEmail = Entry(bg='white', relief=SUNKEN, width = 20, justify = CENTER)
        self.firstNameLbl = Label(text="First name:", width = 20, justify = CENTER)
        self.surnameLbl = Label(text="Surname:", width = 20, justify = CENTER)
        self.addressLbl = Label(text="Address:", width = 20, justify = CENTER)
        self.telNumberLbl = Label(text="Tel No:", width = 20, justify = CENTER)
        self.DOBLbl = Label(text="DOB:", width = 20, justify = CENTER)
        self.genderLbl = Label(text="Gender:", width = 20, justify = CENTER)
        self.tutorGroupLbl = Label(text="Tutor Group:", width = 20, justify = CENTER)
        self.uniqueEmailLbl = Label(text="Email:", width = 20, justify = CENTER)

        #Load test data
        # newSchool.addStudents()
        # newSchool.addEmptyStudents()

        self.welcomeLbl.grid(row=0, columnspan = 5)
        self.logoLbl.grid(row=1, columnspan = 5)
        self.entry1.grid(row=2,column=2, columnspan = 2)
        self.pwLbl.grid(row=3,column=0, columnspan = 2)
        self.userLbl.grid(row=2,column=0,columnspan=2)
        self.entry2.grid(row=3,column=2, columnspan = 2)
        self.loginBtn.grid(row=50,column=0,columnspan=2)
        self.quitBtn.grid(row=50,column=3,columnspan=2)
        # newSchool.loadAllStudents()
        newSchool.viewAllStudents()


    def getUserAndPassword(self):
        username = self.entry1.get()
        psWord = self.entry2.get()
        if newSchool.loginCode(username, psWord) == True:
            self.entry1.grid_remove()
            self.entry2.grid_remove()
            self.loginBtn.grid_remove()
            self.userLbl.grid_remove()
            self.pwLbl.grid_remove()

            filemenu.add_command(label="Add a New Student", command= lambda: app.addNewStudentMenu())
            filemenu.add_command(label="View All Students", command= lambda: app.retrieveAllStudentsMenu())
            filemenu.add_command(label="Locate A Student", command= lambda: app.locateAStudentMenu())
            filemenu.add_command(label="Update A Student", command= lambda: app.updateAStudentMenu())

            filemenu.add_separator()

            filemenu.add_command(label="Run Reports", command= lambda: app.runReportsMenu())
            # filemenu.add_command(label="Run Email List Report", command= lambda: app.emailListMenu())
            # filemenu.add_command(label="Run Students Without Details Report", command= lambda: app.emptyStudentsMenu())
            self.logoutBtn.grid(row=50,column=0,columnspan=2)
            messagebox.showinfo("Success!","Sign in successful.  Please continue.")
            self.welcomeLbl = Label(text="""\nWelcome, Mr Leeman.\n
            Please select the required function from the 'File' menu above.""",
                                    padx = 20,
                                    font = "Verdana 16 bold",
                                    justify = CENTER,
                                    width=60).grid(row=0, columnspan = 5)
            filemenu.add_command(label="Logout", command= lambda: self.logoutCheck())
        else:
            messagebox.showwarning("Problem!","Username and/or password not recognised")


    def aboutApp(self):
        messagebox.showinfo("Tree School Road System", "This system has been developed by and for the strict usage of teachers and/or support staff at Tree Road School. If you have any queries or require your log in details be re-set, please contact the system administrator.")


    def logoutCheck(self):
        result = messagebox.askyesno("Are you sure you want to logout?","If you click yes, you will be logged out and the system closed down.")
        if result == True:
            quit()
        else:
            return


    def addNewStudentMenu(self):
        # self.logoutBtn.grid(row=10,column=1,columnspan=1)
        # self.quitBtn.grid(row=10,column=2,columnspan=1)
        self.genderBtn.grid_remove()
        self.houseBtn.grid_remove()
        self.emailBtn.grid_remove()
        self.firstNameLbl.grid(row=2,column=0)
        self.surnameLbl.grid(row=3,column=0)
        self.addressLbl.grid(row=4,column=0)
        self.telNumberLbl.grid(row=5,column=0)
        self.DOBLbl.grid(row=6,column=0)
        self.genderLbl.grid(row=7,column=0)
        self.tutorGroupLbl.grid(row=8,column=0)
        self.uniqueEmailLbl.grid(row=9,column=0)
        self.firstName.grid(row=2,column=1)
        self.surname.grid(row=3,column=1)
        self.address.grid(row=4,column=1)
        self.telNumber.grid(row=5,column=1)
        self.DOB.grid(row=6,column=1)
        self.gender.grid(row=7,column=1)
        self.tutorGroup.grid(row=8,column=1)
        self.uniqueEmail.grid(row=9,column=1)
        self.saveBtn.grid(row=9,column=3)
        self.textPad.grid_remove()
        self.locateBtn.grid_remove()
        self.locateLbl.grid_remove()
        self.uniqueId.grid_remove()
        self.updateBtn.grid_remove()
        self.updateIdEntry.grid_remove()
        self.updateIdLbl.grid_remove()
        self.updateIdTitleLbl.grid_remove()


    def addNewStudent(self):
        firstname = self.firstName.get()
        surname = self.surname.get()
        address = self.address.get()
        tel = self.telNumber.get()
        dob = self.DOB.get()
        gender = self.gender.get()
        ttrgrp = self.tutorGroup.get()
        email = self.uniqueEmail.get()
        result = messagebox.askyesno("Have you entered the details correctly?","If you click yes, a new student record will be created.")
        if result == True:
            newSchool.addStudentWithPopUp(firstname, surname, address, tel, dob, gender, ttrgrp, email)
            self.firstName.delete(0,END)
            self.surname.delete(0,END)
            self.address.delete(0,END)
            self.telNumber.delete(0,END)
            self.DOB.delete(0,END)
            self.gender.delete(0,END)
            self.tutorGroup.delete(0,END)
            self.uniqueEmail.delete(0,END)
        else:
            return


    def retrieveAllStudentsMenu(self):
        self.genderBtn.grid_remove()
        self.houseBtn.grid_remove()
        self.emailBtn.grid_remove()
        self.updateBtn.grid_remove()
        self.saveBtn.grid_remove()
        self.firstName.grid_remove()
        self.surname.grid_remove()
        self.address.grid_remove()
        self.telNumber.grid_remove()
        self.DOB.grid_remove()
        self.gender.grid_remove()
        self.tutorGroup.grid_remove()
        self.uniqueEmail.grid_remove()
        self.firstNameLbl.grid_remove()
        self.surnameLbl.grid_remove()
        self.addressLbl.grid_remove()
        self.telNumberLbl.grid_remove()
        self.DOBLbl.grid_remove()
        self.genderLbl.grid_remove()
        self.tutorGroupLbl.grid_remove()
        self.uniqueEmailLbl.grid_remove()
        self.textPad.grid_remove()
        self.locateBtn.grid_remove()
        self.locateLbl.grid_remove()
        self.uniqueId.grid_remove()
        self.updateIdEntry.grid_remove()
        self.updateIdLbl.grid_remove()
        self.updateIdTitleLbl.grid_remove()
        self.textPad.grid(row=12,column=0,columnspan=6)
        self.textPad.delete('1.0',END)
        newSchool.clearStudentsArray()
        newSchool.loadAllStudents()
        inputString = newSchool.viewAllStudents()
        print(inputString)
        self.textPad.insert(END, newSchool.viewAllStudents())
        return


    def locateAStudentMenu(self):
        self.genderBtn.grid_remove()
        self.houseBtn.grid_remove()
        self.emailBtn.grid_remove()
        self.updateBtn.grid_remove()
        self.saveBtn.grid_remove()
        self.firstName.grid_remove()
        self.surname.grid_remove()
        self.address.grid_remove()
        self.telNumber.grid_remove()
        self.DOB.grid_remove()
        self.gender.grid_remove()
        self.tutorGroup.grid_remove()
        self.uniqueEmail.grid_remove()
        self.firstNameLbl.grid_remove()
        self.surnameLbl.grid_remove()
        self.addressLbl.grid_remove()
        self.telNumberLbl.grid_remove()
        self.DOBLbl.grid_remove()
        self.genderLbl.grid_remove()
        self.tutorGroupLbl.grid_remove()
        self.uniqueEmailLbl.grid_remove()
        self.updateIdEntry.grid_remove()
        self.updateIdLbl.grid_remove()
        self.updateIdTitleLbl.grid_remove()
        self.locateLbl.grid(row=3, column=0,columnspan = 2)
        self.uniqueId.grid(row=3,column=2, columnspan = 2)
        self.locateBtn.grid(row=3,column=4,columnspan=1)
        self.textPad.grid(row=12,column=0,columnspan=6)
        self.textPad.delete('1.0',END)
        return


    def locateAStudent(self):
        self.textPad.delete('1.0',END)
        uniqueId = self.uniqueId.get()
        print('The unique ID is: ' + uniqueId)
        answer = newSchool.findAStudent(uniqueId)
        if answer is not None:
            print('The answer variable is: ' + answer)
            self.textPad.insert(END, answer)
        else:
            answerResult = 'The student for that ID cannot be found.\n\nPlease check the ID number and try again.'
            self.textPad.insert(END, answerResult)


    def updateAStudentMenu(self):
        self.genderBtn.grid_remove()
        self.houseBtn.grid_remove()
        self.emailBtn.grid_remove()
        self.saveBtn.grid_remove()
        self.updateIdTitleLbl.grid(row=2,column=0, columnspan = 6)
        self.updateIdEntry.grid(row=3,column=1)
        self.updateIdLbl.grid(row=3,column=0)
        self.firstNameLbl.grid(row=4,column=0)
        self.surnameLbl.grid(row=5,column=0)
        self.addressLbl.grid(row=6,column=0)
        self.telNumberLbl.grid(row=7,column=0)
        self.DOBLbl.grid(row=8,column=0)
        self.genderLbl.grid(row=9,column=0)
        self.tutorGroupLbl.grid(row=10,column=0)
        self.uniqueEmailLbl.grid(row=11,column=0)
        self.firstName.grid(row=4,column=1)
        self.surname.grid(row=5,column=1)
        self.address.grid(row=6,column=1)
        self.telNumber.grid(row=7,column=1)
        self.DOB.grid(row=8,column=1)
        self.gender.grid(row=9,column=1)
        self.tutorGroup.grid(row=10,column=1)
        self.uniqueEmail.grid(row=11,column=1)
        self.locateLbl.grid_remove()
        self.uniqueId.grid_remove()
        self.locateBtn.grid_remove()
        self.textPad.grid_remove()
        self.updateBtn.grid(row=11,column=3,columnspan=1)
        return


    def updateStudent(self):
        idNumber = self.updateIdEntry.get()
        firstname = self.firstName.get()
        surname = self.surname.get()
        address = self.address.get()
        tel = self.telNumber.get()
        dob = self.DOB.get()
        gender = self.gender.get()
        ttrgrp = self.tutorGroup.get()
        email = self.uniqueEmail.get()
        result = messagebox.askyesno("Do you want to proceed?","If you click yes, the students details will be overwritten.")
        if result == True:
            if newSchool.updateStudentWithPopUp(idNumber, firstname, surname, address, tel, dob, gender, ttrgrp, email) is True:
                self.updateIdEntry.delete(0,END)
                self.firstName.delete(0,END)
                self.surname.delete(0,END)
                self.address.delete(0,END)
                self.telNumber.delete(0,END)
                self.DOB.delete(0,END)
                self.gender.delete(0,END)
                self.tutorGroup.delete(0,END)
                self.uniqueEmail.delete(0,END)
            else:
                messagebox.showinfo("Error!", 'Student record could not be found and/or updated.  Please try again.')
        else:
            return


    def writeString(self, fileName,insertString):
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


    def runReportsMenu(self):
        self.genderBtn.grid(row=4, column=0, columnspan=6)
        self.houseBtn.grid(row = 6, column=0,columnspan=6)
        self.emailBtn.grid(row = 8, column=0,columnspan=6)
        self.saveBtn.grid_remove()
        self.updateIdTitleLbl.grid_remove()
        self.updateIdEntry.grid_remove()
        self.updateIdLbl.grid_remove()
        self.firstNameLbl.grid_remove()
        self.surnameLbl.grid_remove()
        self.addressLbl.grid_remove()
        self.telNumberLbl.grid_remove()
        self.DOBLbl.grid_remove()
        self.genderLbl.grid_remove()
        self.tutorGroupLbl.grid_remove()
        self.uniqueEmailLbl.grid_remove()
        self.firstName.grid_remove()
        self.surname.grid_remove()
        self.address.grid_remove()
        self.telNumber.grid_remove()
        self.DOB.grid_remove()
        self.gender.grid_remove()
        self.tutorGroup.grid_remove()
        self.uniqueEmail.grid_remove()
        self.locateLbl.grid_remove()
        self.uniqueId.grid_remove()
        self.locateBtn.grid_remove()
        self.textPad.grid_remove()
        self.updateBtn.grid_remove()


    def genderReport(self):
        self.writeString("Report-Gender.pdf",newSchool.genderListReport())


    def emailListReport(self):
        self.writeString("Report-Email.pdf",newSchool.emailListReport())


    def missingDetailsReport(self):
        self.writeString("Report-Missing.pdf",newSchool.emptyStudentReport())


#Set up menu bar
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_separator()
filemenu.add_command(label="Exit", command= lambda: exit())
menubar.add_cascade(label="File", menu=filemenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About...", command= lambda: app.aboutApp())
menubar.add_cascade(label="Help", menu=helpmenu)
root.config(menu=menubar)

#Run main GUI program
app = Main(root)
root.mainloop()

