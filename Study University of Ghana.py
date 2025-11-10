try:

    semester_hour = 1000
    regular_room = 500000
    air_condition_room = 1000000
    academic_facilities = 500000
    matriculation = 200000
    graduating_student = 300000


    room_type = input("Enter your room type (A or R) : ").upper()
    credit_hours = int(input("Enter your credit hours? : "))
    graduating_status = input("Are you graduating (Y or N): ").upper()

    student_id = int(input("Enter student id number (not more than 4 digit) : "))
    if student_id > 4:
        print("Warning!!! Student Id exceeds 4 digits. Enter 4 digits.")

    credit_cost = 0
    if 15 <= credit_hours <= 21:
        credit_cost = credit_hours * semester_hour

    extra_cost = 0
    if room_type == 'R':
       extra_cost = regular_room + academic_facilities + matriculation
    elif room_type == 'A':
        extra_cost = air_condition_room + academic_facilities + matriculation

    if graduating_status == "Y":
        degree_certificate = 300000
        print(f'Graduation cost:{'Y' if graduating_status == 'Y' else 'No' } ')

    else:
        degree_certificate = 0


    fees = credit_cost + extra_cost + degree_certificate
    print('==========================================================================')
    print(f'Student_id: {student_id} ')
    print(f'Extra cost includes room,academic_facilities,matriculation: {extra_cost} ')
    print(f'Graduation fee is:{degree_certificate} ')
    print(f'Credit cost: {credit_cost} ')
    print(f'Fees: {fees}')


except ValueError:
        print("Enter a valid value")







