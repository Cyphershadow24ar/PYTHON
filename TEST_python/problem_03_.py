# A happy year is the year with only distinct digits(e.g. 2019 is a happy year,2024 is not a happy year). write a python program that prints all happy years in between the given  range.

starting_year = int(input("Enter the start year of the range: "))
ending_year = int(input("Enter the end year of the range: "))

start = starting_year
end = ending_year
happy = []

for year in range(start, end + 1):
    if len(set(str(year))) == len(str(year)):
        happy.append(year)

print("Happy years in the range are:", happy)
