import time
import machine
import ujson

import picoweb

from common import wifi_connect, is_authenticate, light_on
import settings

app = picoweb.WebApp(__name__)

water_pin = machine.Pin(settings.WATER_PIN, machine.Pin.OUT)
food_pin = machine.Pin(settings.FOOD_PIN, machine.Pin.OUT)


class Light:
	on = False


@app.route("/")
def index(request, response):
	if not is_authenticate(request, settings.WEB_BASIC_AUTH):
		yield from picoweb.start_response(
			response, content_type="text/html", headers='WWW-Authenticate: Basic realm="private"', status="401"
		)
		return

	yield from picoweb.start_response(response, content_type="text/html")
	yield from app.render_template(response, "index.tpl", (settings.WEB_URL, settings.CAM_STREAM_URL))

@app.route("/resources", methods=["POST"])
def resources(request, response):
	if not is_authenticate(request, settings.WEB_BASIC_AUTH):
		yield from picoweb.start_response(
			response, content_type="text/html", headers='WWW-Authenticate: Basic realm="private"', status="401"
		)
		return

	if request.method == "POST":
		yield from request.read_form_data()
		resource = request.form.get("resource")
		if resource:
			status = "Error"
			if resource[0] == "food":
				status = "Ok"
				food_pin.value(1)
				time.sleep(settings.FOOD_TIME)
				food_pin.value(0)
			elif resource[0] == "water":
				status = "Ok"
				water_pin.value(1)
				time.sleep(settings.WATER_TIME)
				water_pin.value(0)
			elif resource[0] == "light":
				if not light.on:
					light.on = True
					light_on(True)
					status = "On"
				else:
					light.on = False
					light_on(False)
					status = "Off"

			yield from picoweb.jsonify(response, {"resource": resource[0], "status": status})
			return

	yield from picoweb.start_response(response, content_type="application/json", status="400")
	yield from response.awrite(ujson.dumps({"error": "400 Bad Request"}))

light = Light()

wifi_connect(settings.WIFI_SSID, settings.WIFI_PASSWD)

app.run(host=settings.WEB_HOST, port=settings.WEB_PORT)
