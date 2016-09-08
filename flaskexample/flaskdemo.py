from flaskexample import app
from flask import Flask, jsonify, render_template, request
 
@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/echo/', methods=['GET'])
def echo():
    ret_data = {"ac_ft_rt": request.args.get('echoValue')}
    print(ret_data)
    return jsonify(ret_data)
