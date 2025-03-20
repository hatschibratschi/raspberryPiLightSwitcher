from flask import Flask, request, redirect, url_for, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

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

@app.route('/shutdownPi', methods=['POST'])
def shutdown_pi():
    # Add your logic to safely shut down the Raspberry Pi
    os.system("sudo shutdown now")
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
