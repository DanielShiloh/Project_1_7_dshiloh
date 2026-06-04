#constants
FORM_WIDTH = 40

#introductory message
intro = "Thank you for choosing Daniel's Dog Clinic."
intro += "\nPlease fill out this form to request an appointment."
print(intro)

#confirm that this is a dog
species = input("What species is your pet? ")
if species.lower() != "dog":
    print(f"We don't see {species}s here, just dogs.  Try MedVet.")
else:
    print("Great!  Let's get some information on you and your dog.")
    
    #get owner name
    human_first_name = input("What is your first name? ").title()
    human_last_name = input("What is your last name? ").title()

    #initialize list of dogs
    dog_db = []

    #register a dog
    while True:

        #create dog's profile
        current_dog = {
            'name': input("What is your dog's name? ").title(),
            'sex': input("What is your dog's sex? ").lower(),
            'breed': input("What is your dog's breed? ").lower(),
            'age': input("What is your dog's age in years? "),
            'history': [],
        }
        
        #add medical history list
        print(f"Please answer a few questions about {current_dog['name']}'s medical history.")
        has_dx = input("Do you have any previous diagnoses to report [y/n]? ")
        while has_dx.lower() == "y":
            dx_name = input("What was the diagnosis? ")
            current_dog['history'].append(dx_name)
            has_dx = input("Do you have another diagnosis to report [y/n]? ")
  
        #add this dog's dictionary to the owner's list of dogs
        dog_db.append(current_dog)



        #print registration form

        blank_line = "|" + " " * FORM_WIDTH + "|"

        print(f"Please bring {current_dog['name']}'s completed form to your visit.")

        print("\n " + "_" * FORM_WIDTH) #upper bound of form
        
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
        
        print(" " + "-" * FORM_WIDTH) #lower bound of form

        #register another pet
        repeat = input("\nWould you like to register another dog [y/n]? ")
        if repeat.lower() != "y":
            break
    
    #outro message
    all_dogs_names = ""
    for dog in dog_db:
        all_dogs_names += dog['name'] + ", "
    print(f"\nThank you for registering {all_dogs_names[:-2]}.")
    print("We'll totally for sure be in touch.\n")