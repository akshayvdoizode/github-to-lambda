import subprocess
import json
import requests 
import pandas as pd
       
        
def lambda_handler(event,context):
    print("Event:", event)
    response = requests.get("https://api.github.com/users/ironhack-datalabs/repos")
    data = response.json()
    print("Data:", data)
    d={"col1": [1,2,3], "col2": [4,5,6]}
    df = pd.DataFrame(data=d)
    print("DataFrame:", df)
    print("done")
    
    
