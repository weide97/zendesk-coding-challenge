from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from dotenv import load_dotenv
load_dotenv()
import os
app = Flask(__name__)
CORS(app)


@app.route("/getTicket")
def getTicket():
    url = 'https://zendeskcodingchallenge4412.zendesk.com/api/v2/tickets.json?per_page=25'
    user = os.environ.get("user") + '/token'
    pwd = os.environ.get("pwd")

    response = requests.get(url, auth=(user, pwd))

    if response.status_code != 200:
        return jsonify (
            {
                "code": response.status_code,
                "message": "Error: Couldn't Autenticate you"
            }
        )

    return jsonify(
        {
            "code":response.status_code,
            "data": response.json(),
            'total_ticket': response.json()
        }
    )
    


@app.route("/getTicketByPage", methods=["POST"])
def getTicketByPage():
    data = request.get_json()
    url = data['url']
    user = os.environ.get("user") + '/token'
    pwd = os.environ.get("pwd")


    response = requests.get(url, auth=(user, pwd))

    if response.status_code != 200:
        return jsonify (
            {
                "code": response.status_code,
                "message": "Error: Couldn't Autenticate you"
            }
        )

    return jsonify(
        {
            "code":response.status_code,
            "data": response.json()
        }
    )
    
@app.route("/userIdentity", methods=["POST"])
def userIdentity():
    data = request.get_json()
    url = "https://zendeskcodingchallenge4412.zendesk.com/api/v2/users/"+str(data["id"])+"/identities"
    user = os.environ.get("user") + '/token'
    pwd = os.environ.get("pwd")


    response = requests.get(url, auth=(user, pwd))

    if response.status_code != 200:
        return jsonify (
            {
                "code": response.status_code,
                "message": "Error: Couldn't Autenticate you"
            }
        )

    return jsonify(
        {
            "code":response.status_code,
            "data": response.json()
        }
    )
    



if __name__ == "__main__":
    app.run(port=5000, debug=True)