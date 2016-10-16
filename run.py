# for setting up the web presence
from flask import Flask, request, redirect

# for playing with sms
import twilio.twiml

# for encoding/decoding unicode strings coming from twilio POST objects
import codecs

# for parsing sms jobs patterns
import re

# for os.system (please don't hurt me)
import os

app = Flask(__name__)

port = 5000 # default port for flask
phone_number = None
required_SMS_beginning = None

jobs = [] # 2D list; [[regex pattern, bash instruction], ..etc]

@app.route("/", methods=["GET", "POST"])
def handle_sms():
	incomingFromNumber = request.form['From']
	if phone_number != None and incomingFromNumber.lstrip('+') != codecs.decode(phone_number, 'utf-8'):
		return "" # don't respond

	messageBody = codecs.encode(request.form['Body']).strip('\n')
	if required_SMS_beginning != None and not messageBody.startswith(required_SMS_beginning):
		return "" # don't respond

	print messageBody[len(required_SMS_beginning):]
	do_sms_job(messageBody[len(required_SMS_beginning):])
	response = twilio.twiml.Response()
	response.message("Operation A-ccomplished!")
	return str(response)

def do_sms_job(command):
	cmd = ""
	for job in jobs:
		m = job[0].match(command)
		if m == None:
			continue;
		cmd = job[1].replace("\\$","!@1o9358!@%#@!@#%")
		arg = re.search(r'\$([0-9]+)', cmd)
		while arg != None:
			try:
				#print m.groups()
				#print m.group(int(arg.group(1)))
				#print cmd[arg.end(0):] 
				cmd = cmd[:arg.start(0)]+m.group(int(arg.group(1)))+cmd[arg.end(0):] 
			except IndexError:
				print "Bad pattern matching for job in map!"
				exit()
			arg = re.search(r'\$([0-9]+)', cmd)
		cmd = cmd.replace("!@1o9358!@%#@!@#%", '$')
		break
	print "Executing: {0}".format(cmd)
	os.system(cmd)

def get_file_content(fileDir):
	fcontent = ""
	try:
		f = open(fileDir, 'r')
		fcontent = f.read().split("\n")
		f.close()
	except IOError as e:
		print "I/O error ({0}): {1}".format(e.errno, e.strerror)
		exit()

	return fcontent

def parse_job_maps():
	fcontent = get_file_content('jobs/maps')

	for line in fcontent:
		tagValuePair = line.split("-->")
		if len(tagValuePair) != 2:
			continue; # ignore
		pattern = re.compile(tagValuePair[0], re.DOTALL | re.UNICODE)
		jobs.append([pattern, tagValuePair[1]])
		
		

if __name__ == "__main__":
	fcontent = get_file_content('info.init')
	
	for line in fcontent:
		tagValuePair = line.split('=')
		if len(tagValuePair) != 2:
			continue; # ignore line

		if tagValuePair[0].strip(' ') == "SMS_BEGIN":
			required_SMS_beginning = tagValuePair[1].strip('\n')
			continue

		if tagValuePair[0].strip(' ') == "PORT":
			try:
				port = int(tagValuePair[1].strip(' '))
				continue
			except ValueError:
				print "The port must be a number in the range [0, 65536]"
				exit()

		if tagValuePair[0].strip(' ') == "MY_PHONE_NUMBER":		
			try:
				phone_number = int(tagValuePair[1].replace(' ', ''))
				phone_number = str(phone_number)
				continue
			except ValueError:
				print "The phone *number must be a *number"
				exit()	
	parse_job_maps()
	#do_sms_job("camrecord 00:00:10")
	#do_sms_job("move mouse 200 100")
	#app.run(debug=True, port=port)

#https://demo.twilio.com/welcome/sms/reply/
