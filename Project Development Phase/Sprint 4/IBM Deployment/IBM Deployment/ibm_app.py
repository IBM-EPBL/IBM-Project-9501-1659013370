import requests
import json
# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "<K09NTcGFskKVbpURhofU4UwPIAb3wPOQn-uK6NBKK6b6 >"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}


# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"fields": [array_of_input_fields], "values": [array_of_values_to_be_scored, another_array_of_values_to_be_scored]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/6b7d2b7c-2ae3-48b2-89e0-20c59173e7c3/predictions?version=2022-11-12', json=payload_scoring,
 headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
print(response_scoring.json())

predictions = response_scoring.json()
pred=print(predictions['prediction'][0]['values'][0][0])
if(pred !=1):
    print(" YOUR ARE SAFE! This is a Legitimate Website")
else:
    print("YOUR ARE ON THE WRONG SITE! Be Cautious!")
