import flask
import yaml

@app.route("/yaml")
def vuln():
    return yaml.load("!!python/object/apply:os.system ['ls']", Loader=yaml.Loader)  # unsafe



AWS_SECRET_ACCESS_KEY=AKIAIOSFODNN7EXAMPLE
PRIVATE_KEY=-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBg...
GITHUB_TOKEN=ghp_1234567890abcdefghijklmnopqrstuv
slack_token=xoxb-123456789012-1234567890123-ABCDEFGHIJKLMNO