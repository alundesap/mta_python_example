import os
import sapjwt
from flask import Flask
app = Flask(__name__)
port = int(os.getenv("PORT", 9099))
@app.route('/python/hello')
def hello():
  return "Hello World"
@app.route('/spython/auth')
def auth_world():
  output = 'Hello World : Authorized \n'
  return output
@app.route('/spython/valid')
def auth_world():
  output = 'Hello World : Validated \n'
  jwtver = sapjwt.jwtValidation()
  output += 'SAPJWT version : ' + jwtver.getLibraryVersion() + ' \n'
  return output
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=port)
