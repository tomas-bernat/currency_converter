#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Currency converter class.

Author: Tomas Bernat (tom.bernat@centrum.cz)
Created: 12.2.2019
"""
import json
from forex_python.converter import CurrencyRates as cr

class Converter:
    
    currencies = {'AUD': '$', 'BGN': 'BGN', 'BRL': 'R$', 'CAD': '$',
                  'CHF': 'Fr.', 'CNY': '¥', 'CZK': 'Kč', 'EUR': '€',
                  'DKK': 'Kr', 'GBP': '£', 'HKD': 'HK$', 'HRK': 'kn',
                  'HUF': 'Ft', 'IDR': 'Rp', 'ILS': '₪', 'INR': '₹',
                  'ISK': 'kr', 'JPY': '¥', 'KRW': 'W', 'MXN': '$',
                  'MYR': 'RM', 'NOK': 'kr','NZD': 'NZ$', 'PHP': '₱',
                  'PLN': 'zł', 'RON': 'L', 'RUB': 'R', 'SEK': 'kr',
                  'SGD': 'S$', 'THB': '฿', 'TRY': 'TRY', 'USD': 'US$',
                  'ZAR': 'R'}
    # currencies supported by https://ratesapi.io/
    # symbols are from forex_python package


    def __init__(self,input_currency, output_currency):
        self.input_currency = self.get_codes(input_currency)
        self.output_currency = self.get_codes(output_currency)

        
    def get_codes_from_symbol(self,symbol):
        """Return list of currency codes according to symbol"""
        codes = []
        for k, v in self.currencies.items():
            if v == symbol:
                codes.append(k)
        return(codes)

        
    def get_codes(self,currency):
        """Return list of currency codes if currency is supported"""
        if currency in self.currencies.keys() or currency =='all_currencies':
            codes = [currency]
        elif currency in self.currencies.values():
            codes = self.get_codes_from_symbol(currency)
        else:
            exception ="""Currency '{0}' is not supported.\n\nSupported currencies:\n{1}
                """.format(currency,json.dumps(self.currencies,indent=4,sort_keys=True))
            raise Exception(exception.encode('windows-1250'))
        return(codes)


    def convert(self,amount):
        """Convert amount from input currencies to output currencies"""
        result = {}
        i = 0
        for in_cur in self.input_currency:
            i +=1
            if len(self.input_currency) == 1:
                n = ''
            else:
                n = str(i)+'.'
            values = {}
            for out_cur in self.output_currency:
                if out_cur == 'all_currencies':
                    values = cr().get_rates(in_cur)
                    for k,v in values.items():
                        values.update({k:round(v*amount,2)})
                    # faster than one by one cr().convert()
                else:
                    value = round(cr().convert(in_cur,out_cur,amount),2)
                    values.update({out_cur:value})
            result["{0}input".format(n)] = {"amount":amount,"currency":in_cur}
            result["{0}output".format(n)] = values
        return(result)