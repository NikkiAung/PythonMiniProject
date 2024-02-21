first_name_list = []
last_name_list = []
the_pier = []
entrance_gate = []
paintingdecorating = []
joining_day = []
joining_month = []
joining_year = []
not_paid_members = []
volunteer_names = []
expired_members = []
fee_members = []
sponsor_message = []
member_number = int(input("How many members would you like to register: "))
for i in range(member_number):
    first_name = str(input("what is your first name: "))
    first_name_list.append(first_name)
    last_name = str(input("what is your last name: "))
    last_name_list.append(last_name)
    volunteer = input("do you want to become a volunteer(yes/no): ")
    if volunteer == "yes":
        volunteer_number = int(input("where would you like to volunteer from: \n the pier entrancegate(1) \n the gift shop(2) \n painting and decorating(3): "))
        if volunteer_number == 1:
            the_pier.append(first_name)
            volunteer_names.append(first_name)
        else:
            if volunteer_number == 2:
                entrance_gate.append(first_name)
                volunteer_names.append(first_name)
            else:
                if volunteer_number == 3:
                    paintingdecorating.append(first_name)
                    volunteer_names.append(first_name)
day = int(input("what is your day of joining(0-31): "))
joining_day.append(day)
month = int(input("what is your month of joining(1-12): "))
joining_month.append(month)
year = int(input("what is your year of joining(2000-2022): "))
joining_year.append(year)
if year < 2022:
    expired_members.append(first_name)
fee = input("have you paid the $75 fee?(yes/no) ")
if fee == "yes":
    fee_members.append(first_name)
else:
    if fee == "no":
        not_paid_members.append(first_name)
sponsor = input("do you want to sponsor a plank?(yes/no): ")
if sponsor == "yes":
    message = str(input("enter your message: "))
    sponsor_verification = input("is the message ok?(yes/no): ")
    if sponsor_verification == "no":
        message = str(input("enter your message again: "))
sponsor_message.append(message)
print(volunteer_names)
print(the_pier)
print(entrance_gate)
print(paintingdecorating)
print(expired_members)
print(not_paid_members)
print(sponsor_message)