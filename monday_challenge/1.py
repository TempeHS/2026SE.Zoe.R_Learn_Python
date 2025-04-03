#create two lists of items

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
bothlists = [list1, list2]


#create two lists with an id so line items can be paired



#print the two lists as a table

print ("| list 1 | list 2 |")
print ("| ------ | ------ |")

var1 = int(-1)

for i in list1:
    print(f'|   {i}    |', end = ' ')
    var1 = int(var1 + 1)
    if var1 > 3:
        print(f'  {list2[var1]}   |')
    else:
        print(f'   {list2[var1]}   |')
    print('', end = "")

print ("| ------ | ------ |")

#user inputs an item to a prompt and only that name from the table prints 

numfromlist1 = int(input('item from list 1: '))

if numfromlist1 > 0 and numfromlist1 < 6: 
    for num in list1:
        if num == numfromlist1:
            print(f'number = {list1[numfromlist1 - 1]}')
else: 
    print('number is not in list (womp womp)')

#add a new item and sort the lists

addnumtolist1 = input('*evil wizard voice* WHAT NUMBER DO YOU WISH TO ADD TO LIST ONE, TRAVELLER? ').lower()

if "list2" in addnumtolist1 or "list 2" in addnumtolist1 or "listtwo" in addnumtolist1 or "list two" in addnumtolist1:
    print('NO.')
else:
    addnumtolist1 = int(addnumtolist1)
    if addnumtolist1 > 0:
        if addnumtolist1 < 6:
            print('ALREADY IN THE LIST, TRAVELLER')
        elif addnumtolist1 < 11:
            print('BRO THINK HE LIST TWO')
            print (f'{list1[0]}, {list1[1]}, {list1[2]}, {list1[3]}, {list1[4]}, {addnumtolist1}')
        else: 
            print (f'{list1[0]}, {list1[1]}, {list1[2]}, {list1[3]}, {list1[4]}, {addnumtolist1}')
    else: 
        print (f'{addnumtolist1}, {list1[0]}, {list1[1]}, {list1[2]}, {list1[3]}, {list1[4]}')



#create a text document with the lists



#read from the lists



#edit lines and write to lists



#
