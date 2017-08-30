
import json, requests, click

def lista(config):
	link = "http://%s:%s/wm/acl/rules/json" % (config.ip, config.port) 
	response = requests.get(link)
	responseJson = json.dumps( response.json(), indent=4, separators=(',', ': '))
	click.echo(click.style(responseJson , fg='green'))



def aclAction(prot, deny, allow, port_number, config):
	payload = ''
	regra_proto = ''
	regra_port = ''
	
	if(prot):
		regra_proto = ', "nw-proto":"%s"' % prot

		if(port_number != 0 and (prot == 'tcp' or prot == 'udp')):
			regra_port = ', "tp-dst":"%d"' % port_number

	if(deny[0] != None):
		deny = list(deny)
		deny.append(regra_proto)
		deny.append(regra_port)
		payload = '{"src-ip":"'+ deny[0] +'","dst-ip":"'+ deny[1] +'","action":"deny"'+ deny[2] + deny[3] +'}' 
	else:
		allow = list(allow)
		allow.append(regra_proto)
		allow.append(regra_port)
		payload = '{"src-ip":"'+ allow[0] +'","dst-ip":"'+ allow[1] +'","action":"allow"'+ allow[2] + allow[3] +'}'

	r = requests.post('http://%s:%d/wm/acl/rules/json' % (config.ip, config.port), data=payload)

	click.echo(r.content)