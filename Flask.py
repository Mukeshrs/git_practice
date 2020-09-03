#from database import getCustomerDetails
from ApiCall import apicall
from flask import Flask, request, render_template
import json
# import things
#from flask_table import Table, Col

app = Flask(__name__)


@app.route('/')
def my_form():
    return render_template('form.html')


@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['u']
    #a=getCustomerDetails(text)
    output = apicall(["Loan","Male","Yes","2","Graduate","No",1200,0,500,200,1,"Rural"])

    #print(output)
    #print(type(output))

    result = json.dumps(output)
    #print(type(result))
    #print(result)

    y = result.split(':')
    # print(y)
    z = y[3].split(',')
    # print(z)
    class_var = z[0][4]
    print(class_var)
    if class_var == 'N':
        Class_N = z[1][2:6]
        print(Class_N)
        pri = Class_N
    else:
        Class_Y = z[2][1:5]
        print(Class_Y)
        pri = Class_Y

    return class_var



if __name__ == '__main__':
    app.run()
