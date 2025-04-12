list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Orignal list: {}".format(list1))
extracted_list = list1[0:5]
print("Extracted first five elements: {}".format(extracted_list))
extracted_list.reverse()
print("Reversed extracted elements: " + str(extracted_list))
