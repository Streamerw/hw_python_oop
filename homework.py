import datetime as dt

date_format = '%d.%m.%Y'

class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []
        self.today_stats = 0
        self.week_stats = 0

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        for i in self.records:
            pass
        return self.today_stats


    def get_week_stats(self):
        for i in self.records:
            pass
        return self.week_stats


class CaloriesCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)

    def get_calories_remained(self):
        amount_left = self.limit - self.today_stats
        if amount_left < 0:
            return f'Сегодня можно съесть что-нибудь ещё, '
            'но с общей калорийностью не более {amount_left} кКал'
        else:
            return f'Хватит есть!'


class CashCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)
    USD_RATE = float(70.01)
    EURO_RATE = float(80.01)
    RUB_RATE = 1

    def get_today_cash_remained(self, currency):
        self.currency = currency
        exchange_rate = {
            'eur': CashCalculator.EURO_RATE,
            'usd': CashCalculator.USD_RATE,
            'rub': CashCalculator.RUB_RATE
        }
        cash_balance = (self.limit - self.get_today_stats()) / self.conversion
        self.cash_balance = abs(round(self.cash_balance, 2))
        #balance = ?
        if cash_balance > 0:
            print(f"На сегодня осталось {self.cash_balance}")
        elif cash_balance == 0:
            print(f"Денег нет, держись")
        elif cash_balance < 0:
            print(f"Денег нет, держись: твой долг - {self.cash_balance}")


class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        formatted_date = '%d.%m.%Y'

        if date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strftime(date, formatted_date).date()


cash_calculator = CashCalculator(1000)
cash_calculator.add_record(Record(amount=145, comment='кофе'))
cash_calculator.add_record(Record(amount=300, comment="Серёге за обед"))
#cash_calculator.add_record(Record(amount=3000, comment="бар в Танин др", date="08.11.2019"))
print(cash_calculator.get_today_cash_remained("rub"))

# должно напечататься
# На сегодня осталось 555 руб
