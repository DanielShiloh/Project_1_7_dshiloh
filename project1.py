"""
Dog Registration Form-Filler
Daniel Shiloh
Pre-fill a registration form with owner and dog information
June 17, 2026
"""

FORM_WIDTH = 40
blank_line = "|" + " " * FORM_WIDTH + "|"
dog_db = []
all_dogs_names = ""

def print_intro():
    """Print intro message to user"""
    intro = "Thank you for choosing Daniel's Dog Clinic."
    intro += "\nPlease fill out this form to request an appointment."
    print(intro)

def decline_pet():
    """Decline non-dog pet, give chance to enter another pet"""
    print(f"We don't see {species}s here, just dogs.  Try MedVet.")
    species = input("Think carefully... what species is your pet? ")

def get_human_info():
    """Get human's name"""
    human_first_name = input("What is your first name? ").title()
    human_last_name = input("What is your last name? ").title()
    return human_first_name, human_last_name

def print_registration_form(first, last, dog):
    """Print human and dog info to screen
    Args:
        first (str): human first name
        last (str): human last name
        dog (dict): name, age, sex, breed, medical history (list)
    """

    print("\n " + "_" * FORM_WIDTH)
    
    print(blank_line)
    
    print(f'|{"Daniel's Dog Clinic":^{FORM_WIDTH}}|')
    
    print(blank_line)
    
    print(f"|{f' Owner: {first} {last}':<{FORM_WIDTH}}|")
    print(f"|{f' Dog: {dog['name']}, {dog['age']} y/o {dog['sex']} {dog['breed']}':<{FORM_WIDTH}}|")
    
    print(blank_line)
    
    print(f"|{' Medical History:':<{FORM_WIDTH}}|")

    if dog['history']:
        for item in dog['history']:
            print(f"|{f'     {item}':<{FORM_WIDTH}}|")
    else:
        print(f"|{'     none':<{FORM_WIDTH}}|")
    
    print(blank_line)
    
    print(" " + "-" * FORM_WIDTH)




print_intro()

species = input("What species is your pet? ")

while species != "dog":
    decline_pet()

print("Great!  Let's get some information on you and your dog.")
    
first, last = get_human_info()

while True: #register infinite dogs

    current_dog = {
        'name': input("What is your dog's name? ").title(),
        'sex': input("What is your dog's sex? ").lower(),
        'breed': input("What is your dog's breed? ").lower(),
        'age': input("What is your dog's age in years? "),
        'history': [],
    }
    
    print(f"Please answer a few questions about {current_dog['name']}'s medical history.")
    has_dx = input("Do you have any previous diagnoses to report [y/n]? ")
    while has_dx.lower() == "y":
        dx_name = input("What was the diagnosis? ")
        current_dog['history'].append(dx_name)
        has_dx = input("Do you have another diagnosis to report [y/n]? ")

    dog_db.append(current_dog)

    print(f"Please bring {current_dog['name']}'s completed form to your visit.")
    
    print_registration_form(first, last, current_dog)

    repeat = input("\nWould you like to register another dog [y/n]? ")
    if repeat.lower() != "y":
        break

for dog in dog_db:
    all_dogs_names += dog['name'] + ", "
print(f"\nThank you for registering {all_dogs_names[:-2]}.")
print("We'll totally for sure be in touch.\n")