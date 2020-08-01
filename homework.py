import datetime as dt

date_format = '%d.%m.%Y'
today = dt.datetime.now().date()
week = dt.timedelta(days=7)

class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []
        self.today_stats = 0
        self.week_stats = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        for i in self.records:
            if i.date == today:
                self.today_stats += i.amount
        return self.today_stats

    def get_week_stats(self):
        for i in self.records:
            if today - week <= i.date <= today:
                self.week_stats.append(i.amount)
        return sum(self.week_stats)


class CaloriesCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)

    def get_calories_remained(self):
        amount_left = self.limit - self.today_stats
        if amount_left < 0:
            return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {amount_left} кКал'
        else:
            return f'Хватит есть!'


class CashCalculator(Calculator):
    USD_RATE = float(70.01)
    EURO_RATE = float(80.01)
    RUB_RATE = 1
    exchange_rate = {
        'eur': (EURO_RATE, "Euro"),
        'usd': (USD_RATE, "USD"),
        'rub': (RUB_RATE, "руб")
    }

    def get_today_cash_remained(self, currency=None):
        if currency is None:
            currency = "rub"
        cash_balance = (self.limit - self.get_today_stats()) / self.exchange_rate.get(currency)[0]
        cash_balance = round(float(cash_balance), 2)
        cash_name = self.exchange_rate.get(currency)[1]
        if cash_balance > 0:
            return f"На сегодня осталось {cash_balance}{cash_name}"
        elif cash_balance == 0:
            return f"Денег нет, держись"
        elif cash_balance < 0:
            return f"Денег нет, держись: твой долг - {abs(cash_balance)}{cash_name}"


class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment

        if date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, date_format).date()


if __name__ == "__main__":
    cash_calculator = CashCalculator(1000)
    cash_calculator.add_record(Record(amount=145, comment='кофе'))
    cash_calculator.add_record(Record(amount=300, comment="Серёге за обед"))
    print(cash_calculator.get_today_cash_remained("rub"))
