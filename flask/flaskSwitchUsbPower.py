from flask import Flask, render_template_string, request, redirect, url_for
import os

app = Flask(__name__)

# HTML template for the web page
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>USB Power Control</title>
    <style>
        button {
            padding: 20px 40px; /* Increase padding for larger buttons */
            font-size: 24px; /* Increase font size */
            width: 300px; /* Set a fixed width */
            height: 100px; /* Set a fixed height */
            color: white; /* Set text color to white */
            border: none; /* Remove borders */
            border-radius: 10px; /* Add rounded corners */
            cursor: pointer; /* Change cursor to pointer */
        }

        /* Styling for the ON button */
        form[action="/powerOn"] button {
            background-color: #4CAF50; /* Green background */
        }

        form[action="/powerOn"] button:hover {
            background-color: #388E3C; /* Darker green for hover */
        }

        /* Styling for the OFF button */
        form[action="/powerOff"] button {
            background-color: #f44336; /* Red background */
        }

        form[action="/powerOff"] button:hover {
            background-color: #D32F2F; /* Darker red for hover */
        }

        body {
            text-align: center; /* Center the content */
            font-family: Arial, sans-serif; /* Set a clean font */
            margin-top: 50px; /* Add some margin at the top */
        }
    </style>
</head>
<body>
    <h1>USB Power Control</h1>
    <form action="/powerOn" method="post">
        <button type="submit">USB Power ON</button>
    </form>
    <br> <!-- Add spacing between buttons -->
    <form action="/powerOff" method="post">
        <button type="submit">USB Power OFF</button>
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
