#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<hello>')
def printme(hello):
    print(f'{hello}')
    return f'{hello}'

@app.route('/count/<num>')
def countme(num):
    init = ""
    for i in range(int(num)):
        init += str(i) + '\n'
    return init

@app.route('/math/<num>/<operation>/<num2>')
def mathit(num, operation, num2):
    if operation == '+':
        x=int(num) + int(num2)
        return str(x)
    elif operation == '-':
        x=int(num) - int(num2)
        return str(x)
    elif operation == 'div':
        x=int(num) / int(num2)
        return str(x)
    elif operation == '*':
        x=int(num) * int(num2)
        return str(x)
    elif operation == '%':
        x=int(num) % int(num2)
        return str(x)

    

if __name__ == '__main__':
    app.run(port=5555, debug=True)
