import datetime

class Customer:

    def __init__(self):
        self.name = input("Name please")
        self.postcode = input("Postcode:")
        self.carddate = input("Card Date please")
        self.card_code  = input("Card Code").strip()


    def check_date(self):
        card = datetime.datetime.strptime(self.carddate, "%d,%m,%y").date()
        if datetime.date.today() < card:
            return True
        else:
            return False

    def check_code(self):

        code_list = list(str(self.card_code))
        check_digit = int(code_list[7])
        code_list.pop()

        code_list.reverse()

        for item in code_list:
            temp_location = code_list.index(item)
            if is_even(temp_location):
                code_list[temp_location] = int(item)*2


        for item in code_list:
            temp_location = code_list.index(item)
            if int(item) > 9:
                code_list[temp_location] = int(item) - 9

        sum_list = 0

        for item in code_list:
            sum_list += int(item)

        code_total = sum_list + int(check_digit)

        if code_total %10 == 0:
            return True
        else:
            return False

    def check_auth(self):
            """Checks the card's authenticity. """
            if self.check_code() and self.check_date():
                print("----------------------")
                print("Valid")
                print(self.name)
                print(self.postcode)
                print(self.card_date)
                print(self.card_code)
            else:
                print("----------------------")
                print("Invalid")
                print(self.name)
                print(self.postcode)

    def is_even(number):
            """Function used to test if a number is even."""
            if number % 2 == 0:
                return True
            else:
                return False


    if __name__ == '__main__':
        customer().check_auth()