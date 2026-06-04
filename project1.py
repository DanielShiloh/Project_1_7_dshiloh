intro = "Thank you for choosing Daniel's Dog Clinic."
intro += "\nPlease fill out this form to request an appointment."
print(intro)

species = input("What species is your pet? ")
if species.lower() != "dog":
    print(f"We don't see {species}s here, just dogs.  Try MedVet.")
else:
    print("Great!  Let's get some information on you and your dog.")

######first time only - get owner name

while species.lower() == "dog":
    #######make this into dictionary, humanNameDogName = name:name, sex:sex, breed:breed...
    name = input("What is your dog's name? ")
    sex = input("What is your dog's sex? ")
    breed = input("What is your dog's breed? ")
    age = input("What is your dog's age in years? ")

    print(f"Please answer a few questions about {name} the {age} y/o {sex} {breed}'s medical history.")

    has_dx = input("Do you have any previous diagnoses to report [y/n]? ")
    while has_dx.lower() == "y":
        break
        #####get dx and date
        #####repeat question

    ######done adding things to this dict

    ######print lil form with the data

######would you like to register another pet

#####great we wont be in touch