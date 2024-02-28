import math
import sys

class CalculatorLogic:

    def data_analyze(self, calculation_type, principal, periods, interest, payment):
        try:
            if not calculation_type or not principal or not periods or not interest:
                raise ValueError("Incorrect parameters")

            principal_amount = float(principal)
            number_of_payments = int(periods)
            annual_interest_rate = float(interest) / 100
            monthly_payment_amount = 0

            if calculation_type == "annuity":
                if not payment:
                    # Розрахунок щомісячного платежу
                    monthly_payment_amount = self.calculate_annuity_payment(principal_amount, number_of_payments, annual_interest_rate)
                    print(f"Your annuity payment = {math.ceil(monthly_payment_amount)}!")
                else:
                    # Розрахунок терміну погашення
                    months = self.calculate_number_of_payments(principal_amount, float(payment), annual_interest_rate)
                    years = months // 12
                    months %= 12
                    print(f"It will take {years} years and {months} months to repay this loan!")
            elif calculation_type == "diff":
                if payment:
                    raise ValueError("Incorrect parameters")
                # Розрахунок диференційованих платежів
                self.calculate_differential_payments(principal_amount, number_of_payments, annual_interest_rate)
            else:
                raise ValueError("Incorrect parameters")

        except ValueError as e:
            print(e)
            sys.exit(1)

    def calculate_annuity_payment(self, principal, number_of_payments, interest):
        return principal * interest * math.pow(1 + interest, number_of_payments) / (math.pow(1 + interest, number_of_payments) - 1)

    def calculate_number_of_payments(self, principal, monthly_payment, interest):
        base = 1 + interest
        exponent = math.log(monthly_payment / (monthly_payment - interest * principal)) / math.log(base)
        return math.ceil(exponent)

    def calculate_differential_payments(self, principal, number_of_payments, interest):
        total_payments = 0
        for month in range(1, number_of_payments + 1):
            payment = (principal / number_of_payments) + interest * (principal - (principal * (month - 1) / number_of_payments))
            total_payments += payment
            print(f"Month {month}: payment is {math.ceil(payment)}")
        overpayment = total_payments - principal
        print(f"Overpayment = {math.ceil(overpayment)}")
