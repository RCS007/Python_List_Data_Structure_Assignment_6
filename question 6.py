# Question 6

# Ask the user to enter the names of three people they want to invite to a party and store them in a list. After
# they have entered all three names, ask them if they want to add another. If they do, allow them to add
# more names until they answer “no”. When they answer “no”, display how many people they have invited
# to the party.

# Note : This assignment will need looping statement. Therefore, you may solve this problem later after we
# discuss looping construct.


# Create an empty list to store the names of people invited to the party
invited_people = []

# Ask the user to enter the names of three people
for i in range(3):
    name = input(f"Enter the name of person {i+1} to invite: ")
    invited_people.append(name)

# Ask the user if they want to add more people
while True:
    add_more = input("Do you want to add another person? (yes/no): ").lower()
    
    if add_more == "yes":
        name = input("Enter the name of the person to invite: ")
        invited_people.append(name)
    elif add_more == "no":
        break
    else:
        print("Please respond with 'yes' or 'no'.")

# Display how many people have been invited
print(f"\nYou have invited {len(invited_people)} people to the party.")
