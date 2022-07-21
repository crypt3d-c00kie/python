#list is a data-structure in python
#list is heterogenous collection unlike arrays

#fruits = [item1,item2] is an example of a simple list
#fruits = ["cherry", "apple", "kiwi"]

southern_states_of_india = ["Tamil Nadu", "Kerala", "Andra Pradesh", "Telangana", "Karnataka"]
#index starts with 0

print(southern_states_of_india[0])
print(southern_states_of_india[1])
print(southern_states_of_india[2])

southern_states_of_india[1] = "Gujarat"

print("Modifying the list, replacing Kerala with Gujarat")
print(southern_states_of_india[1])

#adding an item at the end of list
#.append() is for adding one item
#.extend() is for adding multiple items at the end of the list
print("Adding two items at the end of the list using .extend()")
southern_states_of_india.extend(["Maharastra", "Punjab"]) #adds both list items at the end of the list
print(southern_states_of_india[5])
print(southern_states_of_india[6])

