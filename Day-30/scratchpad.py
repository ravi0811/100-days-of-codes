#FilelNOtFound
# with open("a_file.txt") as file:
#     file.read()
    
#keyError
# a_dictionary= {"key":"Value"}
# value= a_dictionary["non_existent_key"]

#IndexError
#fruit_list= ["Apple","Banana","Pear"]
# fruit= fruit_list[3]

#TypeError
# text="abc"
# print(text+5)

# Try Except Syntax
# try:
    #something that might cause an exception
# except:
    #Do this fi there was an exception
# else:
    #Do this if there were no exception
# finally:
    #Do this no matter what happens
# try:
#     file= open("a_file.txt")
#     a_dictionary={"key":"value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file=open("a_file.txt","w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"{error_message} key does not exit.")
# else:
#     content= file.read()
#     print(content)

# finally:
#     raise TypeError("This is an error that I made up.")

# height= float(input("Height"))
# weight= int(input("Weight"))

# if height>3:
#     raise ValueError("Human Height should not be over 3 meters.")

# bmi= weight/height**2
# print(bmi)

# fruits = ["Apple", "Pear", "Orange"]

# Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#     fruit = fruits[index]
#     print(fruit + " pie")


# make_pie(4)



# JSON
# write= json.dump()
# read= json.load()
# update= json.update