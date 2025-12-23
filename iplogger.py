from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def log_ip():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    ua = request.headers.get('User-Agent')
    with open('visitors.log', 'a', encoding='utf-8') as f:
        f.write(f"{datetime.now()} | {ip} | {ua}\n")
    return "<h1>IP logged!</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
