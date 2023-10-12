class Students:
    def roll(self, roll_no):
        return roll_no

    def name(self, first_name, last_name):
        return first_name + ' ' + last_name

    def standard(self, std):
        return std


class Teachers:
    def __init__(self):
        print('Welcome Teacher!')

    def id(self, i_card_no):
        return i_card_no

    def name(self, first_name, last_name):
        return first_name + ' ' + last_name

    def standard(self, std):
        return std


# What is an instance?
student1 = Students()
teacher1 = Teachers()

student1.roll(12235)
student1.name('Rajini', 'Kanth')
student1.standard(5)


