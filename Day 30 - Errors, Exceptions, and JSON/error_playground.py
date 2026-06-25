# FileNotFound
# with open("non-existent-file.txt") as file:
#     file.read()

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["non-existent-key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# else: # Will run if there were no errors
#     content = file.read()
#     print(content)
# finally: # Will run no matter what
#     file.close()
#     print("File was closed.")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 8:
    raise ValueError("Human height should not be over 8ft.")

bmi = weight / height ** 2
print(bmi)

# KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non-existent-key"]

# IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text + 5)