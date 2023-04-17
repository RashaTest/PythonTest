import requests
import json
patient_names = []
matching_patients= []


def get_fhir_resources(url):
    # Send a request to the specified URL
    response = requests.get(url)
    json_data = json.loads(response.text)
    # Process the FHIR resources in the response
    for resource in json_data["entry"]:
         patient = resource["resource"]
         name = patient["name"][0]
         given_name = " ".join(name["given"])
         family_name = name["family"]
         patient_name = f"{given_name} {family_name}"
         patient_names.append(patient_name)
         for i, patient in enumerate(patient_names):
           print(i,patient)
    # Check if there is a "next" link in the response headers
    if "link" in json_data:
        for link in json_data["link"]:
           if link["relation"] == "next":
              next_url = link["url"]
              get_fhir_resources(next_url)  

def main():
    base_url = "http://87.121.228.85/fhir/Patient?name:startswith=A"
    get_fhir_resources(base_url)

if __name__ == '__main__':
    main()