import os
from flask import Flask
app = Flask(__name__)
port = int(os.getenv("PORT", 9099))
@app.route('/python/hello')
def hello():
  return "Hello World"
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=port)
