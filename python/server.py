import os
from flask import Flask
app = Flask(__name__)
port = int(os.environ.get('PORT', 3000))
@app.route('/python/hello')
def hello():
  return "Hello World"
if __name__ == '__main__':
  app.run(port=port)