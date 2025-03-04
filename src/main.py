import argparse
from calculator import Calculator

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("-op", "--operation", help="Operation to perform (sum, mean, etc.)", required=True)
    parser.add_argument("-val1", "--first_value", type=int, help="Give the first value")
    parser.add_argument("-val2", "--second_value", type=int, help="Give the second value")
    parser.add_argument("-list", "--values", nargs='+', type=float, help="Give the list of values")

    args = parser.parse_args()
    calc = Calculator()

    if args.operation == 'sum':
        if args.first_value is not None and args.second_value is not None:
            print(f'{args.first_value} + {args.second_value} = {calc.mysum(args.first_value, args.second_value)}')
        else:
            print("Error: sum operation requires --first_value and --second_value.")

    elif args.operation == 'mean':
        if args.values:
            print(f'Mean of {args.values} = {calc.my_mean(args.values)}')
        else:
            print("Error: mean operation requires a list of values with --values.")

    else:
        print('The function is not taken into account in our calculator.')
