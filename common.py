import network


def wifi_connect(ssid, password):
	sta_if = network.WLAN(network.STA_IF)
	if not sta_if.isconnected():
		sta_if.active(True)
		sta_if.connect(ssid, password)
		while not sta_if.isconnected():
			pass
