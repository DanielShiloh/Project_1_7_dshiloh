"""
Dog Registration Form-Filler
Daniel Shiloh
Pre-fill a registration form with owner and dog information
June 11, 2026
"""

FORM_WIDTH = 40
blank_line = "|" + " " * FORM_WIDTH + "|"
dog_db = []
all_dogs_names = ""

intro = "Thank you for choosing Daniel's Dog Clinic."
intro += "\nPlease fill out this form to request an appointment."
print(intro)

species = input("What species is your pet? ")

while species != "dog":
    print(f"We don't see {species}s here, just dogs.  Try MedVet.")
    species = input("Think carefully... what species is your pet? ")

print("Great!  Let's get some information on you and your dog.")
    
human_first_name = input("What is your first name? ").title()
human_last_name = input("What is your last name? ").title()

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
    
    #print registration form --start
    print("\n " + "_" * FORM_WIDTH)
    
    print(blank_line)
    
    print(f'|{"Daniel's Dog Clinic":^{FORM_WIDTH}}|')
    
    print(blank_line)
    
    print(f"|{f' Owner: {human_first_name} {human_last_name}':<{FORM_WIDTH}}|")
    print(f"|{f' Dog: {current_dog['name']}, {current_dog['age']} y/o {current_dog['sex']} {current_dog['breed']}':<{FORM_WIDTH}}|")
    
    print(blank_line)
    
    print(f"|{' Medical History:':<{FORM_WIDTH}}|")

    if current_dog['history']:
        for item in current_dog['history']:
            print(f"|{f'     {item}':<{FORM_WIDTH}}|")
    else: #no history was reported
        print(f"|{'     none':<{FORM_WIDTH}}|")
    
    print(blank_line)
    
    print(" " + "-" * FORM_WIDTH)
    #print registration form --end

    repeat = input("\nWould you like to register another dog [y/n]? ")
    if repeat.lower() != "y":
        break

for dog in dog_db:
    all_dogs_names += dog['name'] + ", "
print(f"\nThank you for registering {all_dogs_names[:-2]}.")
print("We'll totally for sure be in touch.\n")