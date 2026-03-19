#Elliott Morris, 3/14/2026, Capital Quiz.py

import random
def main():
    # Dictionary of U.S. states and their capitals
    states_and_capitals = {
        "Alabama": "Montgomery",
        "Alaska": "Juneau",
        "Arizona": "Phoenix",
        "Arkansas": "Little Rock",
        "California": "Sacramento",
        "Colorado": "Denver",
        "Connecticut": "Hartford",
        "Delaware": "Dover",
        "Florida": "Tallahassee",
        "Georgia": "Atlanta",
        "Hawaii": "Honolulu",
        "Idaho": "Boise",
        "Illinois": "Springfield",
        "Indiana": "Indianapolis",
        "Iowa": "Des Moines",
        "Kansas": "Topeka",
        "Kentucky": "Frankfort",
        "Louisiana": "Baton Rouge",
        "Maine": "Augusta",
        "Maryland": "Annapolis",
        "Massachusetts": "Boston",
        "Michigan": "Lansing",
        "Minnesota": "Saint Paul",
        "Mississippi": "Jackson",
        "Missouri": "Jefferson City",
        "Montana": "Helena",
        "Nebraska": "Lincoln",
        "Nevada": "Carson City",
        "New Hampshire": "Concord",
        "New Jersey": "Trenton",
        "New Mexico": "Santa Fe",
        "New York": "Albany",
        "North Carolina": "Raleigh",
        "North Dakota": "Bismarck",
        "Ohio": "Columbus",
        "Oklahoma": "Oklahoma City",
        "Oregon": "Salem",
        "Pennsylvania": "Harrisburg",
        "Rhode Island": "Providence",
        "South Carolina": "Columbia",
        "South Dakota": "Pierre",
        "Tennessee": "Nashville",
        "Texas": "Austin",
        "Utah": "Salt Lake City",
        "Vermont": "Montpelier",
        "Virginia": "Richmond",
        "Washington": "Olympia",
        "West Virginia": "Charleston",
        "Wisconsin": "Madison",
        "Wyoming": "Cheyenne"
    }

    # Counters for correct and incorrect answers
    correct_count = 0
    incorrect_count = 0

    # List of states to quiz
    states = list(states_and_capitals.keys())

    print("Welcome to the U.S. States Capitals Quiz!")
    print("Type 'exit' at any time to quit.\n")

    while True:
        # Pick a random state
        state = random.choice(states)
        answer = input(f"What is the capital of {state}? ").strip()

        if answer.lower() == "exit":
            break
        elif answer.lower() == states_and_capitals[state].lower():
            print("Correct!\n")
            correct_count += 1
        else:
            print(f"Incorrect. The capital of {state} is {states_and_capitals[state]}.\n")
            incorrect_count += 1

    print("Quiz over!")
    print(f"Correct answers: {correct_count}")
    print(f"Incorrect answers: {incorrect_count}")

if __name__ == "__main__":
    main()
