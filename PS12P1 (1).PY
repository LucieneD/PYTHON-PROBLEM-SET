#Prompt the user for a number and create a list with that number of items
num_items = 0
try:
    num_items = int(input("Enter the number of items in the list: "))
except ValueError:
    print("Please enter a valid integer.")
    # handle a non-integer input or exit gracefully
    # You can choose to exit the program here if the user input is not a valid integer
items_list = []
for _ in range(num_items):
    # Handle non-integer input for list items
    while True:
        try:
            item = int(input("Enter an integer: "))
            break
        except ValueError:
            print("Please enter a valid integer.")
    items_list.append(item)
print("List with", num_items, "items:", items_list)

# 2. Insert the score of 99 at position 1 within the list
items_list.insert(1, 99)
print("List after inserting 99 at position 1:", items_list)

#Replace the value of 99 with 100
items_list[items_list.index(99)] = 100
print("List after replacing 99 with 100:", items_list)

#Create a second list and extend the first list with it
second_list = [500, 600, 700, 800, 900]
print("Second list:", second_list)
items_list.extend(second_list)
print("First list after extending with the second list:", items_list)

#Remove the value 800 from the first list
if 800 in items_list:
    items_list.remove(800)
print("First list after removing 800:", items_list)

#Remove the third item from the first list
if len(items_list) >= 3:
    del items_list[2]
print("First list after removing the third item:", items_list)

#Create a list of grades
grades = ["A", "B", "C", "A", "A", "C"]

#Display the count of the number of A grades
print("Number of A grades:", grades.count("A"))

#Display the index of the first B grade
if "B" in grades:
    print("Index of the first B grade:", grades.index("B"))

# Look for F grade and display a message if not found
if "F" not in grades:
    print("F is not in the list.")

#Clear the second list of integers
second_list.clear()
print("Second list after clearing:", second_list)

#Delete the second list and try to display it
del second_list
# print(second_list)  # This line will raise an error as the list no longer exists

#Create a list of players and sort it
players = ["Rizzo", "Davis", "Baez", "Happ", "Bryan"]
players_sorted = sorted(players)
print("Sorted list of players:", players_sorted)

#Make a copy of the list of players called players2
players2 = players.copy()
print("Copy of the list of players (players2):", players2)

#Reverse the order of players2
players2.reverse()
print("Reversed players list:", players)
print("Reversed players2 list:", players2)