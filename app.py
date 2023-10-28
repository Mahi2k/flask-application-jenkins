from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    return 'Hello World! From Flask Application.'


@app.route('/aboutus',methods=['GET'])
def aboutus():
    return "This is abouts us page"


@app.route('/contactus',methods=['GET'])
def contactus():
    return "This is contact us page"
    

if __name__ == '__main__':
    app.run(debug=True,port=80)

