from flask import Flask
import requests
from requests.auth import HTTPBasicAuth
import json
app = Flask(__name__)

@app.route("/createJIRA", methods=['POST'])

def createJIRA():
    url = "https://basantmohanty7.atlassian.net/rest/api/3/issue"
    API_TOKEN= "ATATT3xFfGF0a-3WTRSawllDRs6VAJ2lwVyx_HV2RpjRQrfI0I2-W37p-nhOkkiaZxt6mK-E9N7S2H9844GUVoPDHmzHgm4odPyhM6wFH-guBPsyp4fCRnWGDJ3WIS-CohbAe2JbBZA9PD60TqpsykH1WIQrv85bBfbRPtC-TeCNsi6Q6V36yoM=DBB3563F"
    auth = HTTPBasicAuth("basantmohanty7@gmail.com", API_TOKEN)

    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    payload = json.dumps( {
    "fields": {
    "description": {
        "content": [
            {
            "content": [
                {
                "text": "Hi Team,\nPlease take a look into this issue.",
                "type": "text"
                }
            ],
            "type": "paragraph"
            }
        ],
        "type": "doc",
        "version": 1
        },
        "issuetype": {
        "id": "10002"
        },
    "project": {
        "key": "KAN"
        },
    
        "summary": "Fix the bug problem",
    },
    "update": {}
    } )

    response = requests.request(
    "POST",
    url,
    data=payload,
    headers=headers,
    auth=auth
    )

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

app.run("0.0.0.0", port=5000)
