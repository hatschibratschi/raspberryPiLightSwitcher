# Flask infos

## Install

```
sudo apt update
sudo apt install python3-pip
python3 -m venv flaskEnv
source flaskEnv/bin/activate
pip3 install flask
```

## Allow Flask to Execute the Command Without Password Prompt

To avoid being prompted for a password when running the command, you can configure sudo to allow the tee command without a password:

Edit the sudoers file:
`sudo visudo`

Add the following line to the end of the file:
`www-data ALL=(ALL) NOPASSWD: /usr/bin/tee /sys/bus/usb/drivers/usb/unbind`

Replace www-data with your username if necessary.

## Run flask server

`python3 app.py`

## Start as a service

`sudo nano /etc/systemd/system/flaskapp.service`

```
[Unit]
   Description=Flask App
   After=network.target

   [Service]
   User=pi
   WorkingDirectory=/home/pi/git/raspberryPiLightSwitcher
   ExecStart=/home/pi/git/raspberryPiLightSwitcher/flaskEnv/bin/python3 /home/pi/git/raspberryPiLightSwitcher/flask/flaskSwitchUsbPower.py 
   Restart=always
   Environment="FLASK_APP=flaskSwitchUsbPower.py"
   Environment="FLASK_ENV=test"

   [Install]
   WantedBy=multi-user.target
```

After creating the service file, enable and start it:

Reload systemd to recognize the new service:
```sudo systemctl daemon-reload```

Enable the Flask app service to start on boot:
```sudo systemctl enable flaskapp.service```

Start and restart the service immediately:
```
sudo systemctl start flaskapp.service
sudo systemctl restart flaskapp.service
```

Check the status to ensure it's running:
```sudo systemctl status flaskapp.service```

