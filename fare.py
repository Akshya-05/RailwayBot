from flask import Flask
from flask import request
from flask import make_response
import json
import requests

#flask set up
app = Flask(__name__)
@app.route('/fare', methods=["GET","POST"])
def fare():
    req = request.get_json(silent=True, force=True)
    intentname = req["queryResult"]["intent"]["displayName"]
    if intentname == "number":
        return trainfare(req)
def trainfare(req):
    quota=req["queryResult"]["parameters"]["quota"]
    action=req["queryResult"]["action"]
    if quota=="AC First Class":
        response=requests.get("http://indianrailapi.com/api/v2/TrainFare/apikey/f0b655638770e7ffc18f1dcef0385648/TrainNumber/12565/From/SEE/To/NDLS/Quota/AC First Class").json()
        train_fare = response["Fares"][0]["Fare"]
    elif quota == "AC 2-Tier":
        response = requests.get("http://indianrailapi.com/api/v2/TrainFare/apikey/f0b655638770e7ffc18f1dcef0385648/TrainNumber/12565/From/SEE/To/NDLS/Quota/AC 2-Tier").json()
        train_fare = response["Fares"][1]["Fare"]
    elif quota == "AC 3-Tier":
        response = requests.get("http://indianrailapi.com/api/v2/TrainFare/apikey/f0b655638770e7ffc18f1dcef0385648/TrainNumber/12565/From/SEE/To/NDLS/Quota/AC 3-Tier").json()
        train_fare = response["Fares"][2]["Fare"]
    elif quota == "Sleeper":
        response = requests.get("http://indianrailapi.com/api/v2/TrainFare/apikey/f0b655638770e7ffc18f1dcef0385648/TrainNumber/12565/From/SEE/To/NDLS/Quota/Sleeper").json()
        train_fare = response["Fares"][3]["Fare"]
    elif quota == "General":
        response = requests.get("http://indianrailapi.com/api/v2/TrainFare/apikey/f0b655638770e7ffc18f1dcef0385648/TrainNumber/12565/From/SEE/To/NDLS/Quota/General").json()
        train_fare = response["Fares"][4]["Fare"]
    return train(train_fare, action)


def train(fare,action):
    if action=="TextResponse":
        return {
            "fulfillment": "The fare is "+str(fare)
        }


if __name__ == '__main__':
    app.run(port=3000,debug=True)