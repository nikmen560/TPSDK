from datetime import datetime
def user_input_int_in_range(start, end, message):
    while True:
        try:
            n = int(input(message))
        except ValueError:
            print("Вы ввели не число. Попробуйте снова.")
        else:
            if start <= n <= end:
                return n
            print(f'Вам нужно ввести номер от {start} до {end}')

def convert_str_to_date(message):
    while True:
        try:
            str_date = input(message)
            d = datetime.strptime(str_date, '%d/%m/%y')
        except ValueError:
            print("Вы ввели неверный формат даты. Необходимо ввести: дд/мм/гг. Попробуйте снова.")
         #TODO: str var and d var

        else:
            return d.date()
