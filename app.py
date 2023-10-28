from flask import Flask
from flask import request
from flask import jsonify
import pandas as pd

app = Flask(__name__)

def findUser(dataset, userName, passWord, searchByUserName):
    found = False
    for i in range(len(dataset)):
        print(dataset.loc[i][5],passWord,dataset.loc[i][5] == passWord,type(dataset.loc[i][5]), type(passWord))
        if(searchByUserName == True):
            found = dataset.loc[i][0] == userName
        elif (dataset.loc[i][5] == passWord and dataset.loc[i][0] == userName):
            found = True
    return found

@app.route('/', methods=['GET'])
def hello():
    return 'Hello World! From Flask Application.'


@app.route('/aboutus',methods=['GET'])
def aboutus():
    return "This is abouts us page"


@app.route('/contactus',methods=['GET'])
def contactus():
    return "This is contact us page"
    

@app.route('/login',methods=['POST'])
def login():
    formData = request.get_json()
    userData = pd.read_csv('user.csv')
    print("Pass",formData['password'])
    userFound = findUser(userData, formData['username'], formData['password'], False)
    print("userf",type(userFound), userFound)
    if(userFound == True):
        return jsonify("Login Successfull")
    else:
        return jsonify('Wrong Entry')


if __name__ == '__main__':
    app.run(debug=False,port=80)

