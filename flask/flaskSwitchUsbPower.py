from flask import Flask, render_template_string, request, redirect, url_for
import os

app = Flask(__name__)

# HTML template for the web page
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Cyberpunk Apartment Power</title>
    <style>
        /* General Body Styling */
        body {
            background-color: #0d0d0d; /* Dark background */
            color: #00ffcc; /* Neon cyan text color */
            font-family: 'Orbitron', sans-serif; /* Futuristic font */
            text-align: center; /* Center the content */
            margin: 0;
            padding: 0;
        }

        h1 {
            font-size: 3em;
            text-shadow: 0 0 10px #00ffcc, 0 0 20px #00ffcc, 0 0 30px #00ffcc; /* Neon glow effect */
            margin-top: 50px;
        }

        /* Button Styling */
        button {
            padding: 20px 40px;
            font-size: 1.5em;
            font-weight: bold;
            color: black; /* Text color */
            background: linear-gradient(45deg, #ff007f, #ffcc00); /* Neon gradient */
            border: none;
            border-radius: 15px;
            box-shadow: 0 0 20px #ff007f, 0 0 40px #ffcc00; /* Neon glow */
            cursor: pointer;
            transition: all 0.3s ease-in-out;
        }

        button:hover {
            background: linear-gradient(45deg, #ffcc00, #ff007f); /* Reverse gradient on hover */
            box-shadow: 0 0 30px #ffcc00, 0 0 60px #ff007f; /* Stronger glow on hover */
            transform: scale(1.1); /* Slightly enlarge the button */
        }

        /* Styling for ON button */
        form[action="/powerOn"] button {
            background: linear-gradient(45deg, #00ffcc, #0077ff); /* Neon cyan/blue gradient */
            box-shadow: 0 0 20px #00ffcc, 0 0 40px #0077ff; /* Cyan/blue glow */
        }

        form[action="/powerOn"] button:hover {
            background: linear-gradient(45deg, #0077ff, #00ffcc); /* Reverse gradient on hover */
            box-shadow: 0 0 30px #0077ff, 0 0 60px #00ffcc; /* Stronger glow */
        }

        /* Styling for OFF button */
        form[action="/powerOff"] button {
            background: linear-gradient(45deg, #ff007f, #ff0000); /* Neon pink/red gradient */
            box-shadow: 0 0 20px #ff007f, 0 0 40px #ff0000; /* Pink/red glow */
        }

        form[action="/powerOff"] button:hover {
            background: linear-gradient(45deg, #ff0000, #ff007f); /* Reverse gradient on hover */
            box-shadow: 0 0 30px #ff0000, 0 0 60px #ff007f; /* Stronger glow */
        }

        /* Add some spacing between buttons */
        form {
            margin: 20px 0;
        }
    </style>
    <!-- Import a futuristic font -->
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap" rel="stylesheet">
</head>
<body>
    <h1>Cyberpunk Apartmen F9042</h1> 
    <h2>Main Power Switch</h2>
    <form action="/powerOn" method="post">
        <button type="submit">Power ON</button>
    </form>
    <form action="/powerOff" method="post">
        <button type="submit">Power OFF</button>
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
