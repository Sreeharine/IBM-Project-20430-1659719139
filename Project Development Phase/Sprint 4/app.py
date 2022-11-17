from urllib import request
from flask import *
import joblib
import numpy as np

app = Flask(__name__)

@app.route('/',  methods=['GET', 'POST'])
def hello_world():
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
        loaded_rf = joblib.load("my_random_forest.joblib")
        test = [param5, param2, param3, param4, param6, param7, param1]
        X_test = np.array(test)
        print(X_test.shape)
        pred = loaded_rf.predict([X_test])
        print(pred)
        res = str(pred[0])
        return render_template("index.html", result=res)
    return render_template("index.html", result=res)