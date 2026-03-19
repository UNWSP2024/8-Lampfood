#Elliott Morris, 3/14/2026, Word Seperator.py

def main():
    try:
        #Get user input
        camel_case = input("Enter a camel case string: ").strip()

        #check that input is not empty
        if not camel_case:
            print("Input cannot be empty")

        else:
            sentence = ""
            for i, char in enumerate(camel_case):
                #If character is uppercase and not first letter add a space
                if char.isupper() and i !=0: #only add space on not the first letter
                    sentence += " " + char.lower()
                else :
                    sentence += char

        #fix formatting
        sentence = sentence[0].upper() + sentence[1:] + "."

        print(sentence)

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
