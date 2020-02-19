import json
import family_classes

json_file_name = "data/family_data.json"

#Open the JSON file
with open(json_file_name, "r") as reader:
    #load the JSON data and store it in the variable family_json_data
    family_json_data = json.load(reader)

#Get the parents array from the JSON data (it is an array of strings)
parents = family_json_data["parents"]
#Create a new Family object that is initialized with the parents
new_family = family_classes.Family(parents);

#Get the kids array from the JSON data (it is an array of dicts)
kids = family_json_data["kids"]
#Iterate through the kids array
for kid in kids:
    #Creat a new Kid with the "name" and "age" from the JSON data
    new_kid = family_classes.Kid(kid["name"], kid["age"])
    #Add the Kid to the Family
    new_family.add_kid(new_kid)

print(new_family)
