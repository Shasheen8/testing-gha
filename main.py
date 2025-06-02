import flask
import yaml

@app.route("/yaml")
def vuln():
    return yaml.load("!!python/object/apply:os.system ['ls']", Loader=yaml.Loader)  # unsafe
