#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
CLI application for currency converting.

Author: Tomas Bernat (tom.bernat@centrum.cz)
Created: 12.2.2019
"""
import argparse, json
from converter import Converter

def args_test(args):
    for k,v in vars(args).items():
        if v == None:
            raise Exception('Missing argument "{}".'.format(k))

parser = argparse.ArgumentParser()
parser.add_argument('--amount', 
                    help="amount which we want to convert ",
                    type= float)
parser.add_argument('--input_currency',
                    help="input currency - 3 letters name or currency symbol",
                    type= str)
parser.add_argument('--output_currency',
                    help="output currency - 3 letters name or currency symbol (optional)",
                    type= str,
                    default= 'all_currencies')
args=parser.parse_args()
args_test(args)

result = Converter(args.input_currency,args.output_currency).convert(args.amount)
print(json.dumps(result,indent=4,sort_keys=True))