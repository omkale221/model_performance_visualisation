import config
import requests
import json

url = 'http://127.0.0.1:5000/'
data = {'acc': config.accuracy, 'model_acc':config.model_acc, 'cpu_util':config.cpu_util, 'cuda_util':config.cuda_util,
        'gpu_ram':config.gpu_ram_util , 'cpu_ram':config.cpu_ram_util, "latency":config.latency,
         "batch_size":config.batch_size,
         "avg_fps":config.avg_fps,
         "num_cams":config.num_cams,
         "dataset_model_version" : config.dataset_model_version,
         "infer_framework" : config.infer_framework,
        "infer_lang" : config.infer_lang,
         "dataset_samples" :config.dataset_samples,
         "trained_model_version" : config.trained_model_version,
         "precision" : config.precision,
         "recall" : config.recall,
         "avg_accuracy": config.avg_accuracy

        }
js = json.dumps(data)
x = requests.post(url, json = js)
