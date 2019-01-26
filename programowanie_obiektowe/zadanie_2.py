class Employee:

    def __init__(self, firstname, lastname, hour_pay ):
        self.firstname = firstname
        self.lastname = lastname
        self.hour_pay = hour_pay
        self.registered_normal_hours = 0
        self.registered_overhours = 0

    def register_time(self, hours):
        self.registered_normal_hours = hours
        if hours > 8:
            self.registered_overhours = hours - 8
            self.registered_normal_hours = 8
        else:
            self.registered_normal_hours += hours



    def pay_salary(self):
        worked_hours = self.registered_normal_hours * self.hour_pay + \
                       self.registered_overhours * self.hour_pay * 2
        self.registered_normal_hours = 0
        self.registered_overhours = 0
        return worked_hours









# def test_employee_initialization():
#     employee = Employee('Jan', 'Nowak', 100.0)
#
#     assert employee.firstname == 'Jan'
#     assert employee.lastname == 'Nowak'
#     assert employee.hour_pay == 100
#
# def test_salary_without_register_time():
#     employee = Employee('Jan', 'Nowak', 100.0)
#     assert employee.pay_salary() == 0
#
#
# def test_pay_salary():
#     employee = Employee('Jan', 'Nowak', 100.0)
#     employee.register_time(5)
#
#     assert employee.pay_salary() == 1000
#     assert employee.pay_salary() == 0
#
#
# def test_pay_salary_over_hours():
#     employee = Employee('Jan', 'Nowak', 100.0)
#     employee.register_time(10)
#
#     assert employee.pay_salary() == 800+400
#     assert employee.pay_salary() == 0
#
# def test_many_registrations():
#     employee = Employee('Jan', 'Nowak', 100)
#     employee.register_time(5)
#     employee.register_time(5)
#     assert employee.pay_salary() == 1000
#     assert employee.pay_salary() == 0