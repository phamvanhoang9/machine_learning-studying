import random 
import os 

def generate_random_numbers(amount, lower=0, upper=1050505):

    return [random.randint(lower, upper) for _ in range(amount)]

def save_numbers_to_file(numbers, file_path):
    # Ensure the directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Write numbers to file
    with open(file_path, 'w') as file:
        for number in numbers:
            file.write(f"{number}\n")

amount_of_numbers = 1000000
random_numbers = generate_random_numbers(amount_of_numbers)
file_path = 'data/numbers/1000000.txt'

save_numbers_to_file(random_numbers, file_path)
