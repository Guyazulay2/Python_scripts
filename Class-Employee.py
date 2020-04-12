class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

print('-------------------------------')
emp_1 = Employee('Guy','Azulayy')
emp_1.fullname = "Guy Azulay"
print('First name >> ',emp_1.first)
print('Email >> ',emp_1.email)
print('Full Name >>',emp_1.fullname)
print('-------------------------------')
