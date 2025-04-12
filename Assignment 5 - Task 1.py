name = input("Enter the student's name: ")
marks_dictionary = {"alice": "85", "nick": "70", "mikey": "90"}
if name.lower() in marks_dictionary:
    print("{}'s marks: {}".format(name, marks_dictionary[name.lower()]))
elif print(marks_dictionary.get("{}", "{} is not a student here.").format(name, name)):
    print("Thank you")
