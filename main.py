import flask
import yaml

@app.route("/yaml")
def vuln():
    return yaml.load("!!python/object/apply:os.system ['ls']", Loader=yaml.Loader)  # unsafe

flask==0.12  # vulnerable to multiple issues including CVE-2018-1000656
django==1.11  # EOL, known CVEs
pyyaml==4.1  # CVE-2017-18342

GITHUB_TOKEN = "ghp_a1b2c3d4e5f6g7h8i9j0exampletoken"
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"