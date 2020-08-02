import datetime as dt

date_format = '%d.%m.%Y'
today = dt.datetime.now().date()
week = dt.timedelta(days=7)


class Calculator:

    def __init__(self, limit: float):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        today_stats = 0
        for record in self.records:
            if record.date == today:
                today_stats += record.amount
        return today_stats

    def get_week_stats(self):
        week_stats = []
        for record in self.records:
            if today - week <= record.date <= today:
                week_stats.append(record.amount)
        return sum(week_stats)


class Record:

    def __init__(self, amount: float, comment: str, date=None):
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, date_format).date()


class CashCalculator(Calculator):
    
    USD_RATE = 70.01
    EURO_RATE = 60.01
    currencies = {
        'usd': (USD_RATE, "USD"),
        'eur': (EURO_RATE, "Euro"),
        'rub': (1, "руб")
    }

    def get_today_cash_remained(self, currency=None):
        if currency not in self.currencies:
            return f"неправильный курс"
        if currency is None:
            currency = "rub"
        cur_rate = self.currencies.get(currency)[0]
        cur_name = self.currencies.get(currency)[1]
        cash_balance = (self.limit - self.get_today_stats()) / cur_rate
        if cash_balance > 0:
            return f"На сегодня осталось {round(cash_balance, 2):.2f} {cur_name}"
        elif cash_balance == 0:
            return f"Денег нет, держись"
        elif cash_balance < 0:
            return f"Денег нет, держись: твой долг - {round(abs(cash_balance), 2):.2f} {cur_name}"


class CaloriesCalculator(Calculator):

    def __init__(self, limit):
        super().__init__(limit)

    def get_calories_remained(self):
        amount_left = self.limit - self.get_today_stats()
        if amount_left < 0:
            return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {amount_left} кКал'
        else:
            return f'Хватит есть!'


if __name__ == "__main__":

    cash_calculator = CashCalculator(1)
    cash_calculator.add_record(Record(amount=10, comment='кофе'))
    cash_calculator.add_record(Record(amount=300, comment="Серёге за обед"))
    cash_calculator.add_record(Record(amount=100000, comment="бар в Танин др", date="08.11.2019"))
    print(cash_calculator.get_today_cash_remained("rub"))
