from apiget import currency_rate
from dbconnect import add_data, read_data
from formatedprints import print_format, print_history


def main():
    while True:
        usr_input = input("Enter desired currencies:\n").upper()
        if usr_input == "QUIT":
            break
        if usr_input == "HISTORY":
            # Get all the data stored in our database and print it out
            print_history(read_data())
        else:
            try:
                currency1, currency2 = usr_input.split()
                # Get all the desired data about the currencies from the api
                rates = currency_rate(currency1, currency2)
                # Print the exchange rate in the desired format
                print_format(rates)
                # Add all of the data to our PSQL database
                add_data(rates)

            except:
                print("Wrong input! Try again!")


if __name__ == "__main__":
    main()
