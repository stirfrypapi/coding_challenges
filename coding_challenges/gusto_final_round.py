# ## Exercise

# Implement a service class that schedules payments to the IRS for federal income tax. The class will take a set of tax liabilities and any other necessary input and return an array of payments. The requirements for when to submit payments federal income tax are defined below.

# ## Deposit schedules

# A "deposit schedule" is the schedule on which a company must make tax payments to an agency. For federal income taxes paid to the IRS, there are two different schedules:

# * Monthly
# * Semiweekly

# ### Monthly

# > Under the monthly deposit schedule, deposit employment taxes on payments made during a month by the 15th day of the following month.

# ### Semiweekly

# > Under the semiweekly deposit schedule, deposit employment taxes for payments made on Wednesday, Thursday, and/or Friday by the following Wednesday. Deposit taxes for payments made on Saturday, Sunday, Monday, and/or Tuesday by the following Friday.

# #### Semiweekly Deposit Schedule

# | IF the payday falls on a . . .  | THEN deposit taxes by the following . . . |
# | ------------- | ------------- |
# | Wednesday, Thursday, and/or Friday  | Wednesday  |
# | Saturday, Sunday, Monday, and/or Tuesday  | Friday  |

# -----------------

# Gusto owes the IRS $10 from paying employee A on 12-02-2019. IRS wants Gusto to pay on a monthly basis.
# the deposit date is (MM+1)-15-YY
# Return [10, 12-15-19]

# month = 1, +1 = 2 % 12 = 2
# month = 12, +1 = 13 % 12 = 1
# month = 11, +1 = 12 % 12 = 0
# increment year if month becomes 1

# Gusto owes the IRS $10 from paying employee A on 12-02-2019. IRS wants Gusto to pay on a semiweekly basis.
# if the day is a Wed, Thurs, or Fri, then the deposit date is the following Wed
# else then the deposit date is the following Fri
# Return [10, 12-06-19]

import datetime

DAYS = {0: "Mon",
        1: "Tues",
        2: "Wed",
        3: "Thurs",
        4: "Fri",
        5: "Sat",
        6: "Sun"}


def get_deposit_date(month_in, date_in, year_in):
    # return the deposit date
    deposit_date = ""

    # determine the day of week
    # https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date
    # https://stackoverflow.com/questions/9223905/python-timestamp-from-day-month-year
    dt = datetime.datetime(year=year_in, month=month_in, day=date_in)
    day = dt.weekday()

    # https://stackoverflow.com/questions/6871016/adding-5-days-to-a-date-in-python/6871054

    # if day is Wed, Thurs, or Fri, return the date that is following Wed
    if day >= 2 and day <= 4:
        # get following Wed
        if day == 2:  # Wed
            deposit_date = dt + datetime.timedelta(days=7)
        elif day == 3:  # Thurs
            deposit_date = dt + datetime.timedelta(days=6)
        else:  # Fri
            deposit_date = dt + datetime.timedelta(days=5)
    else:  # Sat, Sun, Mon, Tues
        # get following Fri
        if day == 5:  # Sat
            deposit_date = dt + datetime.timedelta(days=6)
        if day == 6:  # Sun
            deposit_date = dt + datetime.timedelta(days=5)
        if day == 0:  # Mon
            deposit_date = dt + datetime.timedelta(days=4)
        if day == 1:  # Tues
            deposit_date = dt + datetime.timedelta(days=3)

    return deposit_date


# Assume the date is in the format MM-DD-YY as a string
# money_owed is a number
# deposit_basis is a string ["monthly", "semiweekly"]
def get_deposit_schedule(money_owed, date_paid, deposit_basis):
    deposit_date = "MM-DD-YY"
    if deposit_basis == "monthly":

        month = (int(date_paid[0:2]) + 1) % 12
        year = int(date_paid[-2:])
        date = 15

        if month == 1:
            year += 1
        elif month == 0:
            month = 12

        deposit_date = "{}-{}-{}".format(str(month), str(date), str(year))

    elif deposit_basis == "semiweekly":
        month = int(date_paid[0:2])
        year = 2000 + int(date_paid[-2:])
        date = int(date_paid[3:5])
        deposit_date = get_deposit_date(month, date, year)

        # MM-DD-YY
        # https://stackoverflow.com/questions/2158347/how-do-i-turn-a-python-datetime-into-a-string-with-readable-format-date
        deposit_date = deposit_date.strftime("%B %d, %Y")

    return [money_owed, deposit_date]


def get_all_deposit_dates(deposits, basis):
    # get each deposit date
    # for each date we get, add the deposit date to a dictionary where the key is the date
    # and the value is the running sum of money to pay

    irs_payments = {}

    for deposit in deposits:
        money_owed = deposit[0]
        date = deposit[1]
        schedule = get_deposit_schedule(money_owed, date, basis)

        if schedule[1] in irs_payments:
            irs_payments[schedule[1]] += schedule[0]
        else:
            irs_payments[schedule[1]] = schedule[0]

    return irs_payments


print(get_deposit_schedule(10, "12-02-19", "monthly"))  # [10, "1-15-20"]
print(get_deposit_schedule(10, "11-02-19", "monthly"))  # [10, "12-15-19"]
print(get_deposit_schedule(10, "01-02-19", "monthly"))  # [10, "2-15-19"]

#    December 2019
# Su Mo Tu We Th Fr Sa
#  1  2  3  4  5  6  7
#  8  9 10 11 12 13 14
# 15 16 17 18 19 20 21
# 22 23 24 25 26 27 28
# 29 30 31  1  2  3

print(get_deposit_date(11, 30, 2019))  # 12/6/2019
print(get_deposit_date(12, 1, 2019))  # 12/6/2019
print(get_deposit_date(12, 2, 2019))  # 12/6/2019
print(get_deposit_date(12, 3, 2019))  # 12/6/2019
print(get_deposit_date(12, 4,
                       2019))  # input is Wed, output should be 12/11/2019
print(get_deposit_date(12, 5, 2019))  # 12/11/2019
print(get_deposit_date(12, 6, 2019))  # 12/11/2019

print(get_deposit_schedule(10, "12-02-19", "semiweekly"))  # [10, "12-6-2019"]
print(get_deposit_schedule(10, "12-06-19", "semiweekly"))  # [10, "12-11-19"]
print(get_deposit_schedule(10, "12-31-19", "semiweekly"))  # [10, "1-3-20"]

# ([(10, "12-1-19"), (20, "12-15-19")], "monthly") => (30, "1-15-20")
print(get_all_deposit_dates(
    [(10, "12-01-19"), (20, "12-15-19"), (40, "01-01-19")], "monthly"))
print(
    get_all_deposit_dates([(10, "12-01-19"), (20, "12-15-19")], "semiweekly"))