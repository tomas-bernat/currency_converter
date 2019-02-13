#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Web API application for currency converting.

Author: Tomas Bernat (tom.bernat@centrum.cz)
Created: 12.2.2019
"""
import flask
from flask import request, jsonify
from converter import Converter

app = flask.Flask(__name__)

def get_arg(arg):
    try:
        return(request.args[arg])
    except:
        if arg == 'output_currency':
            return('all_currencies')
        else:
            raise Exception('Missing argument "{}".'.format(arg))

@app.route('/currency_converter', methods=['GET'])
def api():
    amount = float(get_arg('amount'))
    input_currency = get_arg('input_currency')
    output_currency = get_arg('output_currency')
    
    result = Converter(input_currency,output_currency).convert(amount)

    return(jsonify(result))

app.run(debug=True, host='0.0.0.0', port=5000)