#Works with Key-Value Pairs
#Instead of using locarions to index as it would be in arrays,
#a key can be used to index it's value
#If arrays had been used, a lot of position memorization would be required

#CREATING DICTIONARIES

print("Color Code: Color(Key), Color Meaning(Value)\n")

colorCode = {"Red":"Stop", "Yellow":"Wait", "Green":"Go"}

print(colorCode)

print("\nWe can now index the Color Meaning(Value), using the Colors(Key)\n")

print("Red Means " + colorCode["Red"])
print("Yellow Means " + colorCode["Yellow"])
print("Green Means " + colorCode["Green"])


print("\n Great!!! We have indexed values using their keys quite simply\n")

print("Now let us create a health record dictionary with patients as the keys and the disease as the values")
print("The dictionary would look something like this:\n")

patients = {"patient1":"Malaria", "patient2":"Ulcers","patient3":"Tuberculosis","patient4":"Common cold","patient5":"Cancer","patient6":"Typhoid"}

print(patients)

print("\nWe can print out individual patients and index the diseases they are having\n")

print("Patient1: " + patients["patient1"])
print("Patient2: " + patients["patient2"])
print("Patient3: " + patients["patient3"])
print("Patient4: " + patients["patient4"])
print("Patient5: " + patients["patient5"])

print("\nDictionaries can be updated\n")
print("In our case, let us say patient5 died and patient3 was misdiagnosed\n")
print("We can update the dictionary\n")

#UPDATING DICTIONARIES

patients["patient3"] = "Pneumonia"


#DELETING RECORDS FROM DICTIONARIES

del patients["patient5"]


print(patients)
