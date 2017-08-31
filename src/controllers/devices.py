#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Auth: Fagner
# V = 1.0
##
## Funções de gerenciamento dos dispositivos
##

import json, requests, click

'''
	Lista os Switchs da rede
'''
def switchs(config):
	response = requests.get(
		"http://%s:%d/wm/core/controller/switches/json" % (config.ip, config.port)
		)
	print json.dumps( response.json(), indent=4, separators=(',', ': '))


'''
	
'''
def sw_infor(config):
	response = requests.get(
		"http://%s:%d/wm/core/switch/all/flow/json" % (config.ip, config.port)
		)
	print json.dumps( response.json(), indent=4, separators=(',', ': '))

'''
	Lista os dispositivos da rede
'''
def devices(config):
	response = requests.get(
		"http://%s:%d/wm/device/" % (config.ip, config.port)
		)
	print json.dumps( response.json(), indent=4, separators=(',', ': '))
