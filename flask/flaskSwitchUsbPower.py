from flask import Flask, render_template_string, request, redirect, url_for
import os

app = Flask(__name__)

# HTML template for the web page
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>USB Power Control</title>
</head>
<body>
    <h1>USB Power Control</h1>
    <form action="/powerOn" method="post">
        <button type="submit" style="padding: 10px 20px; font-size: 16px;">USB Power ON</button>
    </form>
    <form action="/powerOff" method="post">
        <button type="submit" style="padding: 10px 20px; font-size: 16px;">USB Power OFF</button>
    </form>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html_template)

@app.route("/powerOn", methods=["POST"])
def powerOn():
    # Command to switch USB power on
    os.system("echo '1-1' | sudo tee /sys/bus/usb/drivers/usb/bind")
    return redirect(url_for("home"))

@app.route("/powerOff", methods=["POST"])
def powerOff():
    # Command to switch USB power off
    os.system("echo '1-1' | sudo tee /sys/bus/usb/drivers/usb/unbind")
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
