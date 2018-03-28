### Rename this file to settings.py ###

# WIFI #
WIFI_SSID = "ssid"
WIFI_PASSWD = "passwd"

# Web server
WEB_HOST = "0.0.0.0"
WEB_PORT = 80
WEB_URL = "http://rabbit.example.com"
# Basic auth (Need base64 encryption)
WEB_BASIC_AUTH = "ZXhhbXBsZTpiYXNpYw=="

# GPIO
WATER_PIN = 22
FOOD_PIN = 21

# Resources timing
WATER_TIME = 15
FOOD_TIME = 4

# Cam stream url #
CAM_STREAM_URL = "http://login:passwd@cam.example.com/mjpg/video.mjpg?streamprofile=online"
# Cam Light
CAM_LIGH_ON_URL = "http://192.168.1.5/axis-cgi/io/lightcontrol.cgi?action=L1:-100"
CAM_LIGH_OFF_URL = "http://192.168.1.5/axis-cgi/io/lightcontrol.cgi?action=L1:-0"
# Basic auth (Need base64 encryption)
CAM_BASIC_AUTH = "ZXhhbXBsZTpiYXNpYw=="
