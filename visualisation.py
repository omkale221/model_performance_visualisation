from flask import Flask, jsonify, request, render_template
from flask_restful import Resource, Api 
from pandas import DataFrame
import json
import seaborn as sns
import matplotlib.pyplot as plt
import config

app = Flask(__name__) 

api = Api(app)
class Visualise(Resource):


    def post(self):
        d = request.get_json()
        # print(d)
        with open('model_param.json', 'w+') as json_file:
            json_file.write(d)
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
    with open('model_param.json') as json_file:
        item = json.load(json_file)

    print(item)

    # # item = {
    #     "acc": config.model_acc,
    #     "cpu_ram": config.cpu_ram_util,
    #     "gpu_ram": config.gpu_ram_util,
    #     "latency":config.latency,
    #     "batch_size":config.batch_size,
    #     "avg_fps":config.avg_fps,
    #     "num_cams":config.num_cams,
    #     "dataset_model_version" : config.dataset_model_version,
    #     "infer_framework" : config.infer_framework,
    #     "infer_lang" : config.infer_lang,
    #     "dataset_samples" :config.dataset_samples,
    #     "trained_model_version" : config.trained_model_version,
    #     "precision" : config.precision,
    #     "recall" : config.recall,
    #     "avg_accuracy": config.avg_accuracy
    # }
    return render_template("index.html", item = item)

api.add_resource(Visualise, '/')

if __name__ == '__main__': 
	app.run(debug = True)

