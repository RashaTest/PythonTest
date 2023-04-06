import json
import requests

base_url = "http://87.121.228.85/fhir" # replace with your FHIR server's base URL
headers = {"Content-Type": "application/fhir+json;charset=utf-8"}
response = requests.get(f"{base_url}/Patient", headers=headers)
json_data = json.loads(response.text)

#json_object = json.dumps(json_data, indent = 2) 
global next_json_data
patient_names = []
matching_patients = []
while True: 
 if "link" in json_data and len(json_data["link"]) > 0:
    for link in json_data["link"]:
     if link["relation"] == "next":
        next_url = link["url"]
        next_response = requests.get(next_url)
        next_json_data = json.loads(next_response.text)
        next_entry = next_json_data["entry"][0]  
        for entry in next_json_data["entry"]:
         patient = entry["resource"]
         name = patient["name"][0]
         given_name = " ".join(name["given"])
         family_name = name["family"]
         patient_name = f"{given_name} {family_name}"
         patient_names.append(patient_name)
         if patient_name.startswith("R"):
           matching_patients.append(patient_name)

 print("Patient names as list:",*patient_names,sep = "\n")
 print("\nPatients names start with 'A' :",*matching_patients, sep = "\n")

