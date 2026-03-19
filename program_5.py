#Elliott Morris, 3/15/2026, Course.py


def main():
    # Dictionary to store course ID as key and course name as value
    courses = {}

    print("Enter course ID and course name.")
    print("Type 'exit' as the course ID to stop.\n")

    # Loop to collect course information
    while True:
        try:
            course_id = input("Enter course ID (example: COS 2005): ").strip()

            if course_id.lower() == "exit":
                break

            course_name = input("Enter course name: ").strip()

            courses[course_id] = course_name

        except:
            print("Error entering course. Try again.")

    # Ask the user for the subject to search
    subject = input("\nEnter a subject to search for (example: COS): ").strip().upper()

    print("\nMatching courses:")

    found = False  # Keeps track if any course matches

    # Loop through the dictionary to find matching subjects
    for course_id, course_name in courses.items():
        try:
            # Get the subject part of the course ID (before the number)
            course_subject = course_id.split()[0].upper()

            # Check if the subject matches what the user entered
            if course_subject == subject:
                print(course_id, "-", course_name)
                found = True
        except:
            pass

    if not found:
        print("No courses found for that subject.")

if __name__ == "__main__":
    main()
