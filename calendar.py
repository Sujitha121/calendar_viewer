import calendar
def display_month_calendar():
    print(" View Monthly Calendar ")
year = int(input("Enter year (e.g., 2025): "))
    month = int(input("Enter month (1-12): "))
    
    if 1 <= month <= 12:
        print(f"\nCalendar for {calendar.month_name[month]}, {year}:\n")
        print(calendar.month(year, month))
else:
        print("Invalid month entered. Please try again.")
def display_year_calendar():
    print("View Full Year Calendar ")
    year = int(input("Enter year (e.g., 2025): "))
print(f"\nFull Calendar for {year}:\n")
    print(calendar.calendar(year, 2, 1, 6))
print("\n======== PYTHON CALENDAR VIEWER ========")
        print("1. View specific month")
        print("2. View entire year")
        print("3. Exit")



