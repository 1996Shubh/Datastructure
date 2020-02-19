"""Creating calender class"""
class Calender:

    """Function gives first day of the month"""
    def first_day_month(self, year, month, day=1):
        """Using Gregorian calendar formulas"""
        y = year
        m = month
        d = day
        y0 = y - (14 - m) / 12
        x = y0 + y0 / 4 - y0 / 100 + y0 / 400
        m0 = m + 12 * ((14 - m) / 12) - 2
        d0 = int((d + x + (31 * m0 / 12))) % 7
        return d0

    """Function gives number of day in month"""
    def days(self,year,month):
        if month in (1, 3, 5, 7, 8, 10, 12):
            return 31
        elif month in (4, 6, 9, 11):
            return 30
        elif month == 2:
            if Calender.leap_year(self, year):
                return 29
            else:
                return 28

    """Checking the year is leap or not"""
    def leap_year(self, year):
        if  year % 4 == 0:
            return True
        return False

    """Function return the calender of the month"""
    def month(self, year, month):
        """Gives first day of the month"""
        first_day= Calender.first_day_month(self, year, month)

        """Number of days in the month"""
        days = Calender.days(self, year, month)

        month = []
        day = 1
        """Week days"""
        weak_days = ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa']
        month.append(weak_days)
        for number in range(0, 6):
            """If day in month is higher then days"""
            if days < day:
                break
            """days of the week"""
            temp = []
            for day_of_week in range(0, 7):
                if days < day:
                   temp.append("  ")
                   continue
                elif number == 0 and day_of_week < first_day:
                    temp.append("  ")
                    continue
                elif day < 10:
                    temp.append(f'0{day}')
                else:
                    temp.append(f'{day}')
                day += 1
            month.append(temp)
        return month