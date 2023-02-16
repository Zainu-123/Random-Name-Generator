
import random
input_names = input("Enter the names")

# %%
list_names= input_names.split(" ")
print(list_names)

# %%
number_names= input("How many names do you want to select")
number_names=int(number_names)
random.choices(list_names,k=number_names)


