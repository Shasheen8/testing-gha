import yaml
from flask import Flask

app = Flask(__name__)

@app.route("/load")
def unsafe_yaml():
    data = "!!python/object/apply:os.system ['ls']"
    return yaml.load(data, Loader=yaml.Loader) 