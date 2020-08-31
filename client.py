import config
import requests
import json

url = 'http://127.0.0.1:5000/'
data = {'acc': config.accuracy, 'ram_util': config.cpu_ram_util, 'model_acc':config.model_acc, 'cpu_util':config.cpu_util, 'cuda_util':config.cuda_util}
js = json.dumps(data)
x = requests.post(url, json = js)
