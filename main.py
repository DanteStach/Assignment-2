"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45


# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    """Give back what one semester costs."""
    return annual_cost / SEMESTERS_PER_YEAR


def cost_per_month(annual_cost):
    """Give back what one month of the academic year costs."""
    return annual_cost / MONTHS_PER_YEAR


def cost_per_day(annual_cost):
    """Give back what one class day costs."""
    return annual_cost / (SEMESTERS_PER_YEAR * CLASS_DAYS_PER_SEMESTER)


def cost_per_credit(annual_cost, credits):
    """Give back what one credit costs. credits is the number taken this semester."""
    return cost_per_semester(annual_cost) / credits


def cost_per_class(annual_cost, credits):
    """Give back what one 50-minute CS 1430 class meeting costs."""
    return (cost_per_credit(annual_cost, credits) * CS1430_CREDITS / CS1430_MEETINGS_PER_SEMESTER)

def cost_of_skipped_classes(annual_cost, credits, skipped):
    """Calculate the cost of skipped CS1430 classes."""
    return cost_per_class(annual_cost, credits) * skipped

# ---- PROGRAM ----

def main():
    print("Welcome to the Cost of College Calculator!")
    # Ask for the total cost for one year here.
    # Then ask for the credits this semester.
    
    annual_cost = float(input("Enter annual college cost: $"))
    credits = int(input("Enter credits per semester: "))

    while True:
        # Show your menu here.
        print("\nTHE COST OF COLLEGE")
        print("1. Cost per semester")
        print("2. Cost per month")
        print("3. Cost per class day")
        print("4. Cost per credit")
        print("5. Cost per CS 1430 class")
        print("6. Cost of skipped classes")
        print("Q. Quit")

        choice = input("Choose an option: ")
        if choice == "1":
            print(f"One semester costs ${cost_per_semester(annual_cost):,.2f}")

        elif choice == "2":
            print(f"One academic month costs ${cost_per_month(annual_cost):,.2f}")

        elif choice == "3":
            print(f"One class day costs ${cost_per_day(annual_cost):,.2f}")

        elif choice == "4":
            print(f"One credit costs ${cost_per_credit(annual_cost, credits):,.2f}")

        elif choice == "5":
            print(f"One CS 1430 class costs ${cost_per_class(annual_cost, credits):,.2f}")

        elif choice == "6":
            skipped = int(input("How many CS 1430 classes would you skip? "))
            total = cost_of_skipped_classes(annual_cost, credits, skipped)
            print(f"The cost of {skipped} skipped classes is ${total:,.2f}")
            
            
        elif choice == "Q":
            break

        # Add a branch for each menu option here.

        else:
            print("Invalid choice. Please select 1-6 or Q.")


# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
