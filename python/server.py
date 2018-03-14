import os
import json
import sapjwt
from flask import Flask
app = Flask(__name__)
port = int(os.getenv("PORT", 9099))
@app.route('/')
def webroot():
  return '<a href="/python/hello">Hello World</a><br />\n<a href="/spython/auth">Force Login</a><br />\n<a href="/spython/valid">Validate JWT</a><br />\n'
@app.route('/python/hello')
def hello():
  return "Hello World"
@app.route('/spython/auth')
def auth_world():
  output = 'Hello World : Authorized \n'
  return output
@app.route('/spython/valid')
def auth_valid():
  output = 'Hello World : Validation Check <br />\n'
  output = '<br />\n'

  jwtver = sapjwt.jwtValidation()
  output += 'SAPJWT version : ' + jwtver.getLibraryVersion() + ' <br />\n'
  output += '<br />\n'

  svcs_json = str(os.getenv("VCAP_SERVICES", 0))
  svcs = json.loads(svcs_json)

  # Verify the JWT before proceeding. or refuse to process the request.
  # https://jwt.io/ JWT Debugger Tool and libs for all languages

  # From the vcap_services environment variable pull out these things for later.
  vkey = svcs["xsuaa"][0]["credentials"]["verificationkey"]
  secret = svcs["xsuaa"][0]["credentials"]["clientsecret"]

  jwtver.setVerificationKey(secret)
  _rc = jwtver.checkToken(vkey)
  
  if _rc != 0:
    output += 'Validation error: ' + jwtver.getErrorDescription() + ' <br />\n'
  else:
    output += 'Validation key-Id from JWT: ' +jwtver.getKeyId() + ' <br />\n'
    output += 'Validation succeeded, payload from JWT: ' + jwtver.getPayload() + ' <br />\n'

  output += '<br />\n'

  return output
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=port)
