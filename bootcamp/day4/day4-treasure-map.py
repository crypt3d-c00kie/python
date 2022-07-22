#day4
#treasure-map 
# 🥞🥞🥞🥞

row1 = ["🥞", "🥞", "🥞"]
row2 = ["🥞", "🥞", "🥞"]
row3 = ["🥞", "🥞", "🥞"]
map = [row1,row2,row3] # nested list

print(f"{row1}\n{row2}\n{row3}")
position = input("where do you want to put the apple? : ")

#code [x,y]
horizontal  = int(position[0]) #x
vertical = int(position[1]) #y

#map[0] = row1 and likewise
#method 1
#selected_row = map[vertical - 1]
#selected_row[horizontal - 1] = '🍎'

#method 2
map[vertical-1][horizontal-1] = "🍎"

print(f"{row1}\n{row2}\n{row3}")