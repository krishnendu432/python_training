# Generate the random digit
# random is a built-in function in python
import random
# random.random() is a built-in function, it's generate random float number
print(f" The random value between 0.1 to 1 is: {random.random()}")
print("Display the random integer digits between 10 to 20")
# random.randint() is a built-in function, it's generate random int number between two integer
print(random.randint(10,20))
print("Display the random float digits between 3.8 to 4.2")
# random.uniform() is a built-in function, it's generate random float number between two float
print(random.uniform(3.8,4.2))
gift_list=["watch", "calculator", "sunglass", "bag", "water bottle", "tiffin box"]
print(f"The gift list are: {gift_list}")
print("After shuffle of the list: ")
random.shuffle(gift_list)
print(gift_list)
print("Pick the gift item randomly from the mentioned gift list:")
print(random.choice(gift_list))