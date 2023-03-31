import json
import os
import requests


#fhir server endpoint
URL = "http://localhost:8080/fhir"

#fhir server json header content
headers = {"Content-Type": "application/fhir+json;charset=utf-8"}

count = 0
#loop over all files in the output folder in order to upload each json file for each patient.
for dirpath, dirnames, files in os.walk('/Users/RashaTolba/PythonTest/Sample'):
    count += len(files)
    print('Records:', count)

    for file_name in files:
        with open('/Users/RashaTolba/PythonTest/Sample/'+file_name, "r", encoding='utf-8') as bundle_file:
                data = bundle_file.read() 
        # POST         
        r = requests.post(url = URL, data = data.encode('utf-8'), headers = headers)

        #output file name that was processed
        print(file_name)
       
# Get the size of the terminal >>>> I thought that the JSON output has been truncated bcz the size of the termial, so I maximized it.
size = os.get_terminal_size()
os.system(f'mode con: cols=25 lines=80') 
print(size)

# GET
r = requests.get('http://localhost:8080/fhir/Patient', headers=headers)
# print the connection status as I thought the problem in HTTP request
print(r.raise_for_status())
print(r.json)
print(json.dumps(r.json(), indent=2))




    
