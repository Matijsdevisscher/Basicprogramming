

def print_list(my_list_name, my_list):
    print(my_list_name)
    for element in my_list:
        print("Element {0} staat op index {1}" .format(element, my_list.index(element)))

list1 = [10,12,24,-15]
list2 = [10.2, 2.34, 5.67, 7.89]
list3 = ["Johan", "Mike", "Pol", "Piet"]

print_list("list1", list1)
print_list("list2", list2)
print_list("list3", list3)