# ring.com2ciscospark
A small script to send the last recording from RING.COM's doorbell video recording service to Cisco Spark

1) Get the following https://github.com/tchellomello/python-ring-doorbell this is foundation integrating with your RING device.
2) clone this repository
3) update the config.py file with your authentication details
4) Press your doorbell and see 

NOTE 
- the first run of the script will send the latest video to the Cisco Spark room then wait for subsequent recording updates
- requires Video recording service from RING.COM

Enjoy
