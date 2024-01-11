# Shu and Michael want to create a workout schedule to decide who's enjoying sports and who's babysitting.
# Shu wants to go to gym, then have a rest day, then go to yoga to restore.
# Michael wants to go climbing on Shu's rest days.
# On Sundays and Wednesdays Shu also wants to run.
# They start on 1 Jan 2024, because this year starts on Monday and it's beautiful.
# The next time a new year begins on Monday will be, wait a second

# TODO:

# The code, when run, must display whose workout it is today.


from datetime import datetime, date

startdate = datetime(2024, 1, 1)

today = datetime.today().date()
weekday = datetime.today().weekday()
delta = (today - startdate.date()).days

cycle_day = delta % 3

if cycle_day == 1:
    print('Shu goes to gym.')
elif cycle_day == 2:
    print('Michael goes climbing.')
else:
    print('Shu goes to yoga.')

if weekday == (3 or 7):
    print('Also, Shu is running today.')