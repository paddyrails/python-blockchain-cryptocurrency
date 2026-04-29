
names = ["Sohan", "brijesh", "Nancyhouse", "Calhoun", "brittany", "Moana", "Padmanabhan", "Christopher"]

print(f"name with length > 5 and containin n or N")
for name_index in range(len(names)):
    # print(f"{names[name_index]} - length is {len(names[name_index])}")
    
    if(len(names[name_index]) > 5):
        if(names[name_index].__contains__('n') or names[name_index].__contains__('N')):
            print(f"{names[name_index]} - length is {len(names[name_index])}")


list_empty = False

while not list_empty:
    removed_index = names.pop()
    print(removed_index)
    list_empty = len(names) == 0
else:
    print("List is now empty")