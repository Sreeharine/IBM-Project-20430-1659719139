from flask import *
from functools import wraps
import pymongo
import requests
import json
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)
SECRETKEY = os.getenv("SECRETKEY")
app.secret_key = SECRETKEY
PASSWORD=os.getenv("PASSWORD")
CONNECTION_STRING = f"mongodb+srv://ramnath2001:{PASSWORD}@cluster0.owf41o7.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('flask')
user_collection = pymongo.collection.Collection(db, 'user')

# Decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/')
    return wrap

from user import routes

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard/', methods=['GET', 'POST'])
@login_required
def dashboard():
    res = ""
    if request.method == "POST":
        param1 = float(request.form.get("param1"))
        print(param1)
        param2 = float(request.form.get("param2"))
        print(param2)
        param3 = float(request.form.get("param3"))
        print(param3)
        param4 = float(request.form.get("param4"))
        print(param4)
        param5 = float(request.form.get("param5"))
        print(param5)
        param6 = float(request.form.get("param6"))
        print(param6)
        param7 = float(request.form.get("param7"))
        print(param7)
        API_KEY = os.getenv("PASSWORD")
        token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
        API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
        mltoken = token_response.json()["access_token"]
        
        header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}
        
        # NOTE: manually define and pass the array(s) of values to be scored in the next line
        payload_scoring = {"input_data": [{"field": [['do','ph','co','bod','na','tc','year']], "values": [[param5, param2, param3, param4, param6, param7, param1]]}]}
        
        response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/9bb1c7b9-ec34-4f7e-a6b8-a90efcf8433e/predictions?version=2022-11-18', json=payload_scoring,
        headers={'Authorization': 'Bearer ' + mltoken})
        predictions = response_scoring.json()
        res = predictions['predictions'][0]['values'][0][0]
        print(f"Water Quality index: {res}")
        return render_template("dashboard.html", result=res)
    return render_template('dashboard.html', result=res)

# @app.route("/test")
# def test():
#     user_collection.insert_one({"name": "ram"})
#     return "Connected to the data base!"