
import json, requests

def switchs(config):
	response = requests.get(
		"http://%s:%d/wm/core/controller/switches/json" % (config.ip, config.port)
		)
	print json.dumps( response.json(), indent=4, separators=(',', ': '))

def sw_infor(config):
	response = requests.get(
		"http://%s:%d/wm/core/switch/all/flow/json" % (config.ip, config.port)
		)
	print json.dumps( response.json(), indent=4, separators=(',', ': '))

def devices(config):
	response = requests.get(
		"http://%s:%d/wm/device/" % (config.ip, config.port)
		)
	print json.dumps( response.json(), indent=4, separators=(',', ': '))

def deny(config):
	
	payload = {"src-ip":"10.0.0.1/32","dst-ip":"10.0.0.2/32","action":"deny"}
	
	response = requests.post("http://%s:%d/wm/acl/rules/json" % (config.ip, config.port), json=payload)
	print response.text
