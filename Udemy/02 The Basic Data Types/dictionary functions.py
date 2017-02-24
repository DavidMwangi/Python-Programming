#DICTIONARY FUNCTIONS

print ("Back to our patients dicctionary\n")

patients = {"patient1":"Malaria", "patient2":"Ulcers","patient3":"Tuberculosis","patient4":"Common cold","patient5":"Cancer","patient6":"Typhoid"}

print(patients)

print("\n")

print("Patient1: " + patients["patient1"])
print("Patient2: " + patients["patient2"])
print("Patient3: " + patients["patient3"])
print("Patient4: " + patients["patient4"])
print("Patient5: " + patients["patient5"])
print("Patient6: " + patients["patient6"])

print ("\nWe have already learnt how to update a dictionary, say replace or delete a record\n")

del patients["patient5"]

patients["patient2"] = "Acnes"

print (patients)

print("\n")

print("Patient1: " + patients["patient1"])
print("Patient2: " + patients["patient2"])
print("Patient3: " + patients["patient3"])
print("Patient4: " + patients["patient4"])
#print("Patient5: " + patients["patient5"])
print("Patient6: " + patients["patient6"])

#LENGTH OF A DICTIONARY

print ("\nLenth of the patients dictionary\n")

print (len(patients))

#PRINTING OUT KEYS

print ("\nWe can separate the keys amd values in a dictionary and print them separately\n")

print ("Our Dictionay's Keys")

print (patients.keys())

#PRINTING OUT VALUES

print ("\nOur Dictionary Values\n")

print (patients.values())

#CLEARING A DICTIONARY

print ('\nWe can also clear the keys and values in a dictionary and remain with an empty dictionary\n')

patients.clear()

print (patients)

#UPDATING A DICTIONARY

print ("\nLet's create another patient dictionary\n")

newPatients = {"patient7":"Headaches","patient8":"Stomach upsets","patient9":"Broken leg"}

print (newPatients)
print ("Patient 7: " + newPatients["patient7"])
print ("Patient 8: " + newPatients["patient8"])
print ("Patient 9: " + newPatients["patient9"])

print("\n")

print (newPatients.keys())

print ("\n")

print (newPatients.values())

#Remember dictioanries are unordered so you can not index with positions

print ("\nNow we have a new patients dictionary. Remember the first patients dictioanry is empty\n")

print (patients)

print ("\nIt is possible to update the first dictionary with the contents of the new dictionary\n")

patients.update(newPatients)

print ("First Dictionary\n")

print (patients)

print ("\nNew Patient Dictionary\n")

print (newPatients)

#patients.update("patient10";"Depression")

#DELETING A DICTIONARY

del newPatients




