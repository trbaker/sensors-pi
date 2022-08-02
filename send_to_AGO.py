import requests
import json

url = 'https://services3.arcgis.com/GzteEaZqBuJ6GIYr/arcgis/rest/services/survey123_910b6ea1c50743269a5b171a91fe6cc7_fieldworker/FeatureServer/0/addFeatures'
params={"f":"pjson","token":"","rollbackOnFailure":"false","features":'{ \
        "attributes" : { \
            "controller" : "My controller 2", \
            "Longitude": -94.2342}}'
            }

x = requests.post(url, params=params)
print('ok')
