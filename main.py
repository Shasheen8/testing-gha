import yaml
import pickle
import subprocess
import os
import random
from flask import Flask, request, redirect, render_template_string
import xml.etree.ElementTree as ET

app = Flask(__name__)

# ❌ VULNERABLE: Hardcoded secrets
API_KEY = "sk-1234567890abcdef"
DATABASE_PASSWORD = "admin123"
JWT_SECRET = "my-super-secret-key"

@app.route("/load")
def unsafe_yaml():
    data = "!!python/object/apply:os.system ['ls']"
    return yaml.load(data, Loader=yaml.Loader)

@app.route("/pickle")
def unsafe_pickle():
    # ❌ VULNERABLE: Unsafe deserialization
    data = request.args.get('data')
    if data:
        return str(pickle.loads(data.encode()))
    return "No data provided"

@app.route("/eval")
def code_injection():
    # ❌ VULNERABLE: Code injection via eval
    code = request.args.get('code', '1+1')
    return str(eval(code))

@app.route("/exec")
def command_injection():
    # ❌ VULNERABLE: Command injection
    cmd = request.args.get('cmd', 'echo hello')
    result = os.system(cmd)
    return f"Command executed: {result}"

@app.route("/file")
def path_traversal():
    # ❌ VULNERABLE: Path traversal
    filename = request.args.get('file', 'default.txt')
    with open(f"/var/www/files/{filename}", 'r') as f:
        return f.read()

@app.route("/redirect")
def unsafe_redirect():
    # ❌ VULNERABLE: Open redirect
    url = request.args.get('url', 'https://example.com')
    return redirect(url)

@app.route("/template")
def template_injection():
    # ❌ VULNERABLE: Server-side template injection
    name = request.args.get('name', 'World')
    template = f"Hello {name}!"
    return render_template_string(template)

@app.route("/xml")
def xxe_vulnerability():
    # ❌ VULNERABLE: XML External Entity (XXE)
    xml_data = request.data.decode()
    if xml_data:
        root = ET.fromstring(xml_data)
        return ET.tostring(root).decode()
    return "No XML data"

@app.route("/random")
def weak_random():
    # ❌ VULNERABLE: Weak random number generation for security purposes
    session_token = str(random.random())
    return f"Your session token: {session_token}"

@app.route("/subprocess")
def unsafe_subprocess():
    # ❌ VULNERABLE: Subprocess injection
    user_input = request.args.get('input', 'ls')
    result = subprocess.run(user_input, shell=True, capture_output=True, text=True)
    return result.stdout

# ❌ VULNERABLE: SQL injection helper (referenced but not implemented)
def get_user_by_id(user_id):
    query = f"SELECT * FROM users WHERE id = {user_id}"
    # This would execute the query in a real scenario
    return query 