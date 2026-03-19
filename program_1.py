#Elliott Morris, 3/14/2026, Intitals.py

def main():
    try:
        # Get user input
        full_name = input("Enter your first, middle, and last name: ").strip()

        # Split the name into parts
        names = full_name.split()

        # Check that exactly three names were entered
        if len(names) != 3:
            print("Please enter a first, middle, and last name.")
        else:
            # Extract initials
            first_initial = names[0][0].upper()
            middle_initial = names[1][0].upper()
            last_initial = names[2][0].upper()

            # Display initials
            print(f"{first_initial}. {middle_initial}. {last_initial}.")

    except Exception as e:
        print("An unexpected error occurred:", e)

if __name__ == "__main__":
    main()
