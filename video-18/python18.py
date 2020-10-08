# # list

# list1 = ['apple','pen','copy','python']


# # print(type(list1))

# # # for i in list1 :
# # #     print('i have to buy', i)
# # print(list1[0]) # indexing start from 0 that why it gives apple as output
# # print(list1[1]) # indexing start from 0 that why it gives pen as output

# # print(list1[-1]) # negative indexing start from last elements

# # print(list1[-2]) # negative indexing start from last elements
# # print(list1[0:3])  # print element from 0 to 2nd element
# list1 = ['apple','pen','copy','python']
# list1.append('glue') # add a new elements in the last
# # list2 = list1  # list1 change also reflect in list2 
# list1.insert(2,"ghari")
# print(list1)
# # print(list2)
# list1.remove('pen')
# print(list1)
# # print(list1.pop()) # it delete last elements 
# # print(list1.pop(0)) 
# list1.clear()  # it delete all the elements in list
# print(list1)

list1 = ["a","b","c"]
list2 = [1,2,3]
	
list1.extend(list2)
print(list1)