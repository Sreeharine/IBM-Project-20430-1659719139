import requests
import json
# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "Dxm10MHxowMQ_iEVpafO4u_6KLcFX-1GJ-YyS6WW-5Ki"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"field": [['do','ph','co','bod','na','tc','year']], "values": [[7.4, 6.6, 64, 0.7, 0.29, 1425, 2009]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/9bb1c7b9-ec34-4f7e-a6b8-a90efcf8433e/predictions?version=2022-11-18', json=payload_scoring,
headers={'Authorization': 'Bearer ' + mltoken})
predictions = response_scoring.json()
pred = predictions['predictions'][0]['values'][0][0]
print(f"Water Quality index: {pred}")
