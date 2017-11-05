import random

class Student:
    counterId = 1

    def __init__(self, firstName, surname, address, telNumber, DOB, gender, tutorGroup, uniqueEmail):
        self.firstName = firstName
        self.surname = surname
        self.address = address
        self.telNumber = telNumber
        self.DOB = DOB
        self.gender = gender
        self.tutorGroup = tutorGroup
        self.uniqueEmail = uniqueEmail
        self.random = random.randint(101,999)
        self.uniqueId = str(self.random) + '-' + self.firstName[:3]
        Student.counterId += 1

    @classmethod
    def newStudent(self, tutorGroup, uniqueEmail):
        firstName = ""
        surname = ""
        address = ""
        telNumber = ""
        DOB = ""
        gender = ""
        return Student(firstName, surname, address, telNumber, DOB, gender, tutorGroup, uniqueEmail)

    @classmethod
    def updateStudentInfo(self, firstName, surname, address, telNumber, DOB, gender, tutorGroup, uniqueEmail):
        studentId = self.uniqueId
        self.firstName = firstName
        self.surname = surname
        self.address = address
        self.telNumber = telNumber
        self.DOB = DOB
        self.gender = gender
        self.tutorGroup = tutorGroup
        self.uniqueEmail = uniqueEmail
        self.uniqueId = studentId

    def replacementStudentInfo(self, uniqueId, firstName, surname, address, telNumber, DOB, gender, tutorGroup, uniqueEmail):
        self.firstName = firstName
        self.surname = surname
        self.address = address
        self.telNumber = telNumber
        self.DOB = DOB
        self.gender = gender
        self.tutorGroup = tutorGroup
        self.uniqueEmail = uniqueEmail
        # self.uniqueId = uniqueId
        self.uniqueId = uniqueId[:3] + '-' + firstName[:3]

    @property
    def uniqueId(self):
        return self.__uniqueId

    @uniqueId.setter
    def uniqueId(self, uniqueId):
        self.__uniqueId = uniqueId

    @property
    def firstName(self):
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName):
        self.__firstName = firstName

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        self.__surname = surname

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address

    @property
    def telNumber(self):
        return self.__telNumber

    @telNumber.setter
    def telNumber(self, telNumber):
        self.__telNumber = telNumber

    @property
    def DOB(self):
        return self.__DOB

    @DOB.setter
    def DOB(self, DOB):
        self.__DOB = DOB

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender):
        self.__gender = gender

    @property
    def tutorGroup(self):
        return self.__tutorGroup

    @tutorGroup.setter
    def tutorGroup(self, tutorGroup):
        self.__tutorGroup = tutorGroup

    @property
    def uniqueEmail(self):
        return self.__uniqueEmail

    @uniqueEmail.setter
    def uniqueEmail(self, uniqueEmail):
        self.__uniqueEmail = uniqueEmail

