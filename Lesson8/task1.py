import datetime

class Date:

    def __init__(self, string):
        self.string = string

    @classmethod
    def date_to_int(cls, string):
        try:
            day = int(string[:2])
            month = int(string[3:5])
            year = int(string[6:])
            cls.validation(year, month, day)
        except ValueError:
            print('Pattern mismatch!')            

    @staticmethod
    def validation(y, m, d):
        try:
            Date.date = datetime.datetime(y, m, d)              
        except ValueError:
            print('Wrong date!')
        else:
            print('You typed the correct date!')  

Date.date_to_int(input('Type the date (dd-mm-yyyy): '))
