# This file to demonstrate using Enum class in Python

from enum import Enum   

"""
Enum are used in various senorios in Python where we need to define a set of constants or options
that we want to present with more expressive and type-safe semantics."""

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

print(Color.RED) # Color.RED
print(Color.RED.name) # RED
print(Color.RED.value) # 1

