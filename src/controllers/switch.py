
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