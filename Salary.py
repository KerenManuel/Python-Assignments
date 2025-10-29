try:
    reg_hrs = 40
    reg_pay_M = 500
    reg_pay_F = 550
    over_pay_week_M = 750
    over_pay_week_F = 825

    while True:

        def calculate_pay():
            hrs_per_week = int(input("Enter hours worked: "))
            gender = input("Male or Female? (M or F): ").upper()
            children = int(input("How many children?: "))

            gross_pay = 0

            if hrs_per_week <= reg_hrs:
               if gender == 'M':
                  gross_pay = hrs_per_week * reg_pay_M

               elif gender == 'F':
                  gross_pay = hrs_per_week * reg_pay_F

            else:
                if gender == 'M':
                  gross_pay= (hrs_per_week- reg_hrs) * over_pay_week_M + (reg_pay_M * reg_hrs)

                elif gender == 'F':
                  gross_pay = (hrs_per_week - reg_hrs) * over_pay_week_F + (reg_pay_F * reg_hrs)

            edu_fund = 0

            if children > 3:
                if gender == 'M':
                 edu_fund = (children - 3) * 10
                elif gender == 'F':
                    edu_fund = (children - 3) * 20

            income_tax = 0.15 * gross_pay
            nchl = 0.025 * gross_pay
            district_tax = 0.01 * gross_pay

            net_pay = gross_pay - (income_tax + nchl + district_tax + edu_fund )

            return gross_pay,net_pay

        print(calculate_pay())

        user_continue = input("Do you want to continue?(y/n): ").lower()
        if user_continue == 'n':
           print("Thank You")
           break

except ValueError:
        print("Enter a valid value")


