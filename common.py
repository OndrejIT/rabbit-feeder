import network
import urequests

import settings


def wifi_connect(ssid, password):
	sta_if = network.WLAN(network.STA_IF)
	if not sta_if.isconnected():
		sta_if.active(True)
		sta_if.connect(ssid, password)
		while not sta_if.isconnected():
			pass


def is_authenticate(request, password):
	authorization = request.headers[b"Authorization"].decode().split(" ")[-1] if b"Authorization" in request.headers else None
	return True if authorization == password else False


def light_on(status):
	url = settings.CAM_LIGH_ON_URL if status else settings.CAM_LIGH_OFF_URL
	header = {"Authorization": "Basic {0}".format(settings.CAM_BASIC_AUTH)}
	req = urequests.get(url, headers=header)

	return True if req.status_code == 200 else False
