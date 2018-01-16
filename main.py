import ujson
import picoweb

from common import wifi_connect

SSID = ""
PASSWORD = ""
url = ""

app = picoweb.WebApp(__name__)
 
 
@app.route("/")
def index(request, response):
	yield from picoweb.start_response(response, content_type="text/html")
	yield from app.render_template(response, "index.tpl", (url,))

@app.route("/resources", methods=["POST"])
def resources(request, response):
	if request.method == "POST":
		yield from request.read_form_data()
		resource = None
		if request.form.get("resource"):
			if request.form.get("resource")[0] == "food":
				resource = "food"
			elif request.form.get("resource")[0] == "water":
				resource = "water"
			if resource:
				yield from picoweb.jsonify(response, {"success": resource})
				return

	yield from picoweb.start_response(response, content_type="application/json", status="400")
	yield from response.awrite(ujson.dumps({"error": "400 Bad Request"}))


wifi_connect(SSID, PASSWORD)

app.run(host="0.0.0.0", port=80)
