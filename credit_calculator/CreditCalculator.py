import argparse
from CalculatorLogic import CalculatorLogic

def main():
    parser = argparse.ArgumentParser(description="Credit Calculator")
    parser.add_argument("--type", choices=["annuity", "diff"], help="Type of payment: annuity or diff")
    parser.add_argument("--principal", type=float, help="Loan principal amount")
    parser.add_argument("--periods", type=int, help="Number of periods (months)")
    parser.add_argument("--interest", type=float, help="Annual interest rate")
    parser.add_argument("--payment", type=float, help="Monthly payment amount for annuity type")
    args = parser.parse_args()

    calculator_logic = CalculatorLogic()
    calculator_logic.data_analyze(args.type, args.principal, args.periods, args.interest, args.payment)

if __name__ == "__main__":
    main()