import requests
import pandas as pd
import sqlalchemy

url = 'http://api.coincap.io/v2/assets'
header={
	"Content-Type":"application/json",
	"Accept-Encoding":"deflate"
}

response = requests.get(url, headers=header)
print(response)

responseData = response.json()
print(responseData)


