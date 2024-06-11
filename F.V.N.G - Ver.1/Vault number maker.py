import random

def generate_vault_number_with_exclusions(start=1, end=120, exclusions=None):
    """
    Generate a random Fallout vault number within the specified range, excluding certain numbers.
    
    Args:
    - start (int): The starting number of the range (inclusive).
    - end (int): The ending number of the range (inclusive).
    - exclusions (list): A list of numbers to exclude from the generated result.

    Returns:
    - int: A randomly generated vault number that is not in the exclusions list.
    """
    if exclusions is None:
        exclusions = []

    exclusions = [int(num) for num in exclusions]

    possible_numbers = [num for num in range(start, end + 1) if num not in exclusions]

    if not possible_numbers:
        raise ValueError("No valid vault numbers available in the specified range with the given exclusions.")
    
    vault_number = random.choice(possible_numbers)
    return vault_number

def save_vault_number_to_file(filename, vault_number):
    with open(filename, "w") as file:
        file.write(str(vault_number))

if __name__ == "__main__":
    # Excluded vaults from Fallout 1, 2, 3, 4, 76,
    excluded_vaults = [
         0, 1, 3, 4, 6, 8, 11, 12, 13, 15, 17, 19, 21, 22, 31, 32, 33, 34, 36, 42, 43, 51, 53, 55, 56, 63, 68, 69, 70, 75, 76, 77, 79, 81, 87, 92, 94, 95, 96, 101, 106, 108, 111, 112, 114, 118, 119, 120, 170, 177, 199, 314, 333, 404, 525, 666, 730, 813, 899, 909
    ]

    vault_number = generate_vault_number_with_exclusions(exclusions=excluded_vaults)

    # This will save the number to a .txt
    save_vault_number_to_file("vault_number.txt", vault_number)
