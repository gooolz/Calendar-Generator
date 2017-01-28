"""Julia Foote
    This program takes the user's input of a desired year and creates a calendar that is displayed
    in the python console as well as saved into a file that it creates. This program also calculates
    when it is a leap year and alters the calendar accordingly."""

months = [("January", range(1, 32)), ("February", range(1, 29)), ("March", range(1, 32)), ("April", range(1, 31)),
          ("May", range(1, 32)), ("June", range(1, 31)), ("July", range(1, 32)), ("August", range(1, 32)),
          ("September", range(1, 31)), ("October", range(1, 32)), ("November", range(1, 31)),
          ("December", range(1, 32))]

week_display = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
week_val = [0, 1, 2, 3, 4, 5, 6]


def main():
    """In this main function, the user is prompted to input a year and within this function it uses
    the leap_year function to determine if that year is a leap year and if true, it will add an extra
    day to the month of february for that year. This function also uses the first_day function to
    determine which day of the week will be the 1st of January and then populate the calendar accordingly.
    Then the calendar will be printed to a file that is created based on the year inputted."""
    print("\nWelcome to the Calendar Generator, written by Julia Foote")
    year_input = input("Enter a year for the calendar: ")
    if not leap_year(year_input):
        start_pos = week_val.index((first_day((int(year_input)))) + 1)
    else:
        start_pos = week_val.index(first_day((int(year_input))))
    # Checks if it is a leap year
    if leap_year(int(year_input) == 0):
        months[1] = ("February", range(1, 30))
    if not leap_year(year_input):
        months[1] = ("February", range(1, 29))

    # This creates a new file for the calendar to be printed to
    with open(year_input + ".txt", 'w') as write_file:
        # Months and days for statement
        for m, d in months:
            # This prints the months to the file that was created
            write_file.write("\t\t  " + m + " " + year_input + '\n')
            write_file.write("".join(["{0:<5}".format(w) for w in week_display]) + '\n')
            write_file.write("{0:<5}".format('') * start_pos)

            # This prints the months to the python console for debugging
            print("\t\t  " + m + " " + year_input)
            print("".join(["{0:<5}".format(x) for x in week_display]))
            print("{0:<5}".format('') * start_pos, end="")
            # Days for statement
            for x in d:
                # This prints the days to the file that was created
                write_file.write("{0:<5}".format(x))
                # This prints the days to the calendar in the python console for debugging
                print("{0:<5}".format(x), end="")
                start_pos += 1
                if start_pos == 7:
                    write_file.write('\n')
                    print()
                    start_pos = 0
            print('\n')
            write_file.write('\n')
            write_file.write('\n')
    write_file.close()


def first_day(year):
    """This function calculates which day of the week that January 1st will be on. It takes the
    parameter called year which is the user's input year and uses the calculation below
    to find which day value will be returned. The value 'day_one' that is returned is a number
    between 0-6 which corresponds to the days of the week and then is returned to main."""
    day_one = ((year + ((year - 1) / 4) - ((year - 1) / 100) + ((year - 1) / 400)) % 7) - 1
    return round(day_one)


def leap_year(year):
    """This function determines if the year inputted is on a leap year. It takes the parameter
    called year and determines if it is divisible by 400 and if true then it is a leap year and also
    if the year is divisible by 4 and not by 100 then it is a leap year otherwise it is not. This
    function returns a boolean of True or False and returns it to main."""
    if int(year) % 400 == 0:
        return True
    if int(year) % 4 == 0 and not int(year) % 100 == 0:
        return True
    else:
        return False


main()
