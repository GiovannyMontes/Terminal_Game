

print("Welcome to HOW TO BE A MILLIONAIRE!\n\n")

###############################
#       QUESTION ONE          #
###############################
print("Question 1:", "In the UK, the abbreviation NHS stands for National what Service?\n")
print("A. Humanity", "\nB. Health", "\nC. Honour")
print("\n\nEnter A, B, or C\n")

ans1 = input()

#Invalid input case
def invalid(ans):
    if ans == "A" or ans == "C":
        print("Sorry, but that is incorrect.\n")
    elif ans == "B":
        print("CORRECT!")
    else:
        print("Invalid answer, please try again")
        ans = input()
        invalid(ans)
invalid(ans1)


###############################
#       QUESTION TWO          #
###############################
print("\n\nQuestion 2:", "Which of these cetaceans is classified as a “toothed whale”?")
print("A. Gray Whale", "\nB. Humpback Whale", "\nC. Sperm Whale")
print("\n\nEnter A, B, or C\n")

ans2 = input()

#invalid case
def invalid_2(ans):
    if ans == "A" or ans == "B":
        print("Sorry, but that is incorrect.\n")
    elif ans == "C":
        print("CORRECT!")
    else:
        print("Invalid answer, please try again")
        ans = input()
        invalid_2(ans)
invalid_2(ans2)


###############################
#       QUESTION THREE        #
###############################
print("\n\nQuestion 3:", "A geologist would likely be LEAST helpful for answering questions about which of the following?")
print("A. Precious Stones", "\nB. Igneous Rock", "\nC. Fruity Pebbles")
print("\n\nEnter A, B, or C\n")

ans3 = input()

#invalid case
def invalid_3(ans):
    if ans == "A" or ans == "B":
        print("Sorry, but that is incorrect.\n")
    elif ans == "C":
        print("CORRECT!")
    else:
        print("Invalid answer, please try again")
        ans = input()
        invalid_3(ans)
invalid_3(ans3)