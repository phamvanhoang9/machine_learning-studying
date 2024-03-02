# This file to demonstrate using Enum class in Python

from enum import Enum   

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

print(Color.RED) # Color.RED
print(Color.RED.name) # RED
print(Color.RED.value) # 1

