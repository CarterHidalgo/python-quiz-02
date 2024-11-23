# Name: web.py
# Author: Carter Hidalgo
# 
# Purpose: push html to web server and get information when webserver changes

import http.server
from urllib.parse import parse_qs, urlparse
from data import Data

class WebUI(http.server.BaseHTTPRequestHandler):
	HOST_NAME = ''
	PORT_NUMBER = 8000
	UI = None
	TERMINATE = None

	# I found it easier to remove the .html and simply have a complete html broken up by lines here
	lines = [
		'<!DOCTYPE html>'
		'<html>'
		'<body>'
		'<h3>Quiz 02 Web UI</h3>'
		'<form method="post" action="/send">'
		'<label><input type="radio" name="lbl_type" value="F" {{temp_lbl_far}}> Fahrenheit</label>'
		'<label><input type="radio" name="lbl_type" value="C" {{temp_lbl_cel}}> Celcius</label>'
		'<p>Temperature: {{temp}} &deg;{{temp_lbl_type}}</p>'
		'<p>Humidity: {{hum}}</p>'
		'<label><input type="radio" name="set_type" value="F" {{temp_set_far}}> Fahrenheit</label>'
		'<label><input type="radio" name="set_type" value="C" {{temp_set_cel}}> Celcius</label><br>'
		'<label>Cool ({{cool}} {{temp_set_type}}): </label>'
		'<input type="text" name="set_cool"><br><br>'
		'<label>Heat ({{heat}} {{temp_set_type}}): </label>'
		'<input type="text" name="set_heat"><br><br>'
		'<p>Door: {{door}}</p>'
		'<input type="radio" name="lock" value=True {{locked}}> Lock</label>'
		'<input type="radio" name="lock" value=False {{unlocked}}> Unlock</label><br><br>'
		'<label>Inside Lights</label>'
		'<input type="radio" name="in_lights" value=True {{in_lights_on}}> On</label>'
		'<input type="radio" name="in_lights" value=False {{in_lights_off}}> Off</label><br><br>'
		'<label>Outside Lights</label>'
		'<input type="radio" name="out_lights" value=True {{out_lights_on}}> On</label>'
		'<input type="radio" name="out_lights" value=False {{out_lights_off}}> Off</label><br><br>'
		'<button type="submit">Push</button><br><br>'
		'</form>'
		'<form method="GET" action="/send">'
		'<button type="submit">Update</button>'
		'</form>'
		'</body>'
		'</html>'
	]

	def do_GET(self):
		self.path = urlparse(self.path).path

		if self.path == "/" or self.path == "/send":

			# replace format holders with real data from Data
			html_content = "\n".join(WebUI.lines).replace(
				"{{temp}}", Data.get_temp_str()
			).replace(
				"{{temp_lbl_type}}", Data.get_temp_lbl_type()	
			).replace(
				"{{hum}}", Data.get_hum_str()
			).replace(
				"{{temp_lbl_far}}", "checked" if Data.get_temp_lbl_type() == "F" else ""
			).replace(
				"{{temp_lbl_cel}}", "checked" if Data.get_temp_lbl_type() == "C" else ""
			).replace(
				"{{temp_set_far}}", "checked" if Data.get_temp_set_type() == "F" else ""
			).replace(
				"{{temp_set_cel}}", "checked" if Data.get_temp_set_type() == "C" else ""
			).replace(
				"{{temp_set_type}}", Data.get_temp_set_type()
			).replace(
				"{{cool}}", Data.get_cool_str()
			).replace(
				"{{heat}}", Data.get_heat_str()
			).replace(
				"{{door}}", Data.get_door_string()
			).replace(
				"{{in_lights_on}}", "checked" if Data.get_in_lights() else ""
			).replace(
				"{{in_lights_off}}", "checked" if not Data.get_in_lights() else ""
			).replace(
				"{{out_lights_on}}", "checked" if Data.get_out_lights() else ""
			).replace(
				"{{out_lights_off}}", "checked" if not Data.get_out_lights() else ""
			).replace(
				"{{locked}}", "checked" if Data.get_locked() else ""
			).replace(
				"{{unlocked}}", "checked" if not Data.get_locked() else ""
			)

			self.send_response(200)
			self.send_header("Content-type", "text/html")
			self.end_headers()
			self.wfile.write(html_content.encode())

	def do_POST(self):
		if self.path == "/send":
			content_length = int(self.headers['Content-Length'])
			post_data = self.rfile.read(content_length).decode()
			params = parse_qs(post_data)

			Data.set_temp_lbl_type(params.get("lbl_type")[0])
			Data.set_temp_set_type(params.get("set_type")[0])

			# read data from params and update Data using setters
			if "set_cool" in params:
				Data.set_cool(params.get("set_cool")[0])
			if "set_heat" in params:
				Data.set_heat(params.get("set_heat")[0])
			if "lock" in params and Data.get_door():
				print("found: " + params.get("lock")[0])
				Data.set_locked(params.get("lock")[0] == "True")
			if "in_lights" in params:
				Data.set_in_lights((params.get("in_lights")[0] == "True"))
			if "out_lights" in params:
				Data.set_out_lights((params.get("out_lights")[0] == "True"))

			WebUI.UI.update()

			self.send_response(303)
			self.send_header("Location", "/")
			self.end_headers()

	def run(tkui):
		# the web server will run forever, even after tkui and circuit terminate
		# to close, you will have to manually terminate the program
		WebUI.UI = tkui
		server = http.server.HTTPServer((WebUI.HOST_NAME, WebUI.PORT_NUMBER), WebUI)
		server.serve_forever()