from programowanie_obiektowe.zadanie_2 import Employee



# class Employee:
#
#     def __init__(self, firstname, lastname, hour_pay):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.hour_pay = hour_pay
#         self.registered_normal_hours = 0
#         self.registered_overhours = 0
#
#     def register_time(self, hours):
#         self.registered_normal_hours = hours
#         if hours > 8:
#             self.registered_overhours = hours - 8
#             self.registered_normal_hours = 8
#         else:
#             self.registered_normal_hours += hours
#
#     def pay_salary(self):
#         worked_hours = self.registered_normal_hours * self.hour_pay + \
#                        self.registered_overhours * self.hour_pay * 2
#         self.registered_normal_hours = 0
#         self.registered_overhours = 0
#         return worked_hours


class PremiumEmployee(Employee):

    def __init__(self, firstname, lastname, hour_pay):
        super().__init__(firstname, lastname, hour_pay)
        self.bonus = 0

    def give_bonus(self, pay):
        self.bonus += pay

    def pay_salary(self):
        return super().pay_salary() + self.give_bonus


# employee = PremiumEmployee("Jan", "Nowak", 100)
# employee.register_time(5)
# employee.give_bonus(1000)
# print(employee.pay_salary())



def test_premium_employee_give_bonus():
    employee = PremiumEmployee("Jan", "Nowak", 500)
    employee.register_time(5)
    employee.give_bonus(1000)
    assert employee.pay_salary == 1500