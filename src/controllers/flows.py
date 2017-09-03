#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Auth: Fagner
# V = 1.0
##
## Controle dos fluxos inseridos no 
##
import json, requests, click

def addflow(file, config):
	#payload = '{"switch":"00:00:00:00:00:00:00:01", "name":"flow-mod-1", "cookie":"0", "priority":"32768", "in_port":"1","active":"true", "actions":"output=2"}'
	request = requests.post('http://%s:%d/wm/staticentrypusher/json' % (config.ip, config.port), data=file)
	return request.content


def sw_infor(config):
	response = requests.get(
		"http://%s:%d/wm/core/switch/all/flow/json" % (config.ip, config.port)
		)
	return json.dumps( response.json(), indent=4, separators=(',', ': '))