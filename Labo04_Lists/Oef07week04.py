#Schrijf een functie ‘max_num_in_list’ met als paramenter een list van getallen die uit de list
#het maximum opzoekt en teruggeeft.


list = [1, 2, 1000, 500, -29]

def get_max(my_list):
    nmbr = 0
    for element in my_list:
        if (element>0):
            max_nmbr = element
        return max_nmbr

print(max(list))
print(get_max(list))

