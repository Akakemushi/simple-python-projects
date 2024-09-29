spam = ["apples", "bananas", "tofu", "cats"]
length = len(spam)
final_index = length - 1
if length > 0:
    for index, item in enumerate(spam):
        if index == final_index:
            print(item)
        elif index == final_index - 1:
            print(item + " and ", end="")
        else:
            print(item + ", ", end="")
else:
    print("This list is empty.")
