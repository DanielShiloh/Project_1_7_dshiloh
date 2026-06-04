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
            'name': input("What is your dog's name? ").lower(),
            'sex': input("What is your dog's sex? ").lower(),
            'breed': input("What is your dog's breed? ").lower(),
            'age': input("What is your dog's age in years? "),
            'history': [],
        }
        
        #add medical history
        print(f"Please answer a few questions about {current_dog['name']}'s medical history.")
        has_dx = input("Do you have any previous diagnoses to report [y/n]? ")
        while has_dx.lower() == "y":
            dx_name = input("What was the diagnosis? ")
            current_dog['history'].append(dx_name)
            has_dx = input("Do you have another diagnoses to report [y/n]? ")
  
        #add this dog's dictionary to the owner's list of dogs
        dog_db.append(current_dog)

        ######done adding things to this dict

        ######print lil form with the data

    ######would you like to register another pet

    #####great we wont be in touch