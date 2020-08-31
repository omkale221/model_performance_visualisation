from flask import Flask, jsonify, request, render_template
from flask_restful import Resource, Api 
from pandas import DataFrame
import json
import seaborn as sns
import matplotlib.pyplot as plt


app = Flask(__name__) 
api = Api(app) 

class Visualise(Resource):
    def post(self): 
        d = request.get_json()
        data = json.loads(d)
        classes = ['model']
        accuracies = [data['model_acc']]
        for cls, acc in data['acc'].items():
            classes.append(cls)
            accuracies.append(acc)
        df = {'class': classes, 'acc': accuracies}
        acc_df = DataFrame(data=df)
        sns.set(style="whitegrid")
        ax = sns.barplot(x="class", y="acc", data=acc_df)
        plt.savefig('static/acc.png')
        plt.clf()
        classes = ['cpu', 'gpu']
        util = [data['cpu_util'], data['cuda_util']]
        df = {'processor': classes, 'utilisation': util}
        per_df = DataFrame(data=df)
        sns.set(style="whitegrid")
        ax = sns.barplot(x="processor", y="utilisation", data=per_df)
        plt.savefig('static/per.png')

        response = jsonify({'data': data})   
        response.status_code = 200
        return response
        
@app.route('/')
def index():
    return render_template("index.html")

api.add_resource(Visualise, '/')

if __name__ == '__main__': 
	app.run(debug = True)

