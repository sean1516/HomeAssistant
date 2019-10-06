
<p align="center">
  <img src="https://github.com/home-assistant/home-assistant-assets/blob/master/loading-screen.gif">
</p>

These are the [Home Assistant](https://home-assistant.io/) configuration files used in my Home Assistant (HA) setup. I relied on repositories of other HA users quite a bit when I was getting started for ideas and example code.  Hopefully this repository will help someone else who is getting started. 

# Automations:
A detailed description of each of my automations and a link to the yaml file is located [HERE](https://github.com/SilvrrGIT/HomeAssistant/tree/master/automation#automations)

This is the most important part of Home Assistant!  Remote control and voice commands are nice, however, that is not home automation, just remote control.  Automations should make your life easier, look at what you do every day, the simplest things, and automate them.  To me Home Automation is collecting data about your home and automatically acting based on that data.

# Hardware Running My Home Assistant Setup:

__[Raspberry Pi 3B+](https://www.raspberrypi.org/products/raspberry-pi-3-model-b-plus/)__ This Raspberry Pi is running [HassOS ](https://github.com/home-assistant/hassos) and HomeAssistant.  It also runs the following add-ons. 

* [Configurator](https://www.home-assistant.io/addons/configurator/)
* [Backup to Google Drive](https://github.com/sabeechen/hassio-google-drive-backup)
* [Dasshio](https://github.com/SilvrrGIT/hassio-addons)
* [DuckDNS](www.home-assistant.io/addons/duckdns/)
* [Network UPS Tools](https://github.com/SilvrrGIT/hassio-addons)
* [PiHole](https://github.com/hassio-addons/addon-pi-hole)
* [RPC Shutdown](https://www.home-assistant.io/addons/rpc_shutdown/)
* [SSH](https://www.home-assistant.io/addons/ssh/)
* [Samba](https://www.home-assistant.io/addons/samba/)

I'm currently running [Home Assistant](https://home-assistant.io) version __0.98.1__

__[Raspberry Pi 2B](https://www.raspberrypi.org/products/raspberry-pi-2-model-b/)__ This Raspberry Pi is running [HassOS ](https://github.com/home-assistant/hassos) and HomeAssistant mainly for the ease of adding add-ons and sending load data to the main instance

There is a seperate repository for this instance located [Here](https://github.com/SilvrrGIT/Raspberry-Pi2B-Server) 

# Network & Home Assistant Instance Security:
I think this is an often overlooked part of any internet connected project.  I am far from a security expert, however, these are the steps I have taken to add some level of security to my Home Assistant instance.
- Simple protections like enabling a [password](https://github.com/SilvrrGIT/HomeAssistant/blob/master/configuration.yaml#L45) and limiting the number of incorrect [login attempts](https://github.com/SilvrrGIT/HomeAssistant/blob/master/configuration.yaml#L48).
- Setup [Multi Factor Authentication](https://www.home-assistant.io/docs/authentication/multi-factor-auth/) wherever possible
- Anything that doesn't need an internet connection is blocked from any inbound or outbound traffic at the router level.
- Open ports are limited to access only from the IPs I designate.  The Ubiquiti USG has a 'limited' option when opening ports. As a result, port scanners and other tools see these ports as closed/filtered.
- Failed login attempts to the Home Assistant Front end generate a [notification](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/pc_security.yaml#L23) to me with the source IP.
- My Home Assistant Traffic is encrypted with [Let's Encrypt](https://letsencrypt.org/).  I used [this guide](https://github.com/SilvrrGIT/HomeAssistant/wiki/Let's-Encrypt-Setup-(Hassbian,-Python-Virtual-Environment)) to get it setup on Hassbian and now use the [DuckDNS](www.home-assistant.io/addons/duckdns/) add-on in Hass.io to do the same thing.
- [Test your security and test it often](https://community.home-assistant.io/t/test-your-security-and-test-it-often/76354).

# Editing the Configuration Files:
I create a Samba share that I can then edit on any computer in my house.  I accomplished this with the Samba add-on for Hass.io.  For other install methods [this](https://github.com/SilvrrGIT/HomeAssistant/wiki/Hassbian-Quick-Reference-Sheet#setting-up-a-samba-share) is a good tutorial. 

After you have the Samba share setup, I liked to use [Visual Studio Code](https://code.visualstudio.com/) to edit my files with the [Home Assistant Config Helper][Visual Studio Code](https://code.visualstudio.com/).  It works on both Windows and Linux, has a great interface and some nice features. 

# A Few Stats On my Setup:
| Tracked Devices | Lights | Binary Sensors | Switches | Automations | Scripts | Sensors | Zwave Devices |
|:---------------:|:------:|:--------------:|:--------:|:-----------:|:-------:|:-------:|:-------------:|
|41               |10      |7               |42        |86           |4        |210      |7              | 

# Connected Devices:

### Cloud Controlled Devices:
* [Amazon Echo Dot](https://www.amazon.com/All-New-Amazon-Echo-Dot-Add-Alexa-To-Any-Room/dp/B01DFKC2SO) Used for voice commands to turn devices on/off using the [Emulated Hue Component](https://home-assistant.io/components/emulated_hue/)
* [iPhone XR](https://www.apple.com/iphone-xr/) Used for presence detection

### Wifi Connected Devices
* [Xiaomi Yeelight RGBW E27 Smart LED Bulbs](http://www.gearbest.com/smart-lighting/pp_361555.html) *
* [Xiaomi Yeelight E27 Smart LED Bulbs](http://www.gearbest.com/smart-light-bulb/pp_278478.html) *
* [Broadlink RM Mini 3](https://www.amazon.com/BroadLink-Control-Universal-Remote-RMMINI3-EN/dp/B01FK2SDOC/ref=sr_1_2?ie=UTF8&qid=1499475366&sr=8-2&keywords=broadlink+mini3)*
* [Sonoff Basic (Flashed with Tasmota)](https://www.amazon.com/Sonoff-Wireless-Modified-Low-cost-Compatible/dp/B06WWNBD3Y?ref=ast_p_ei)*
* [Sonoff POW (Flashed with Tasmota)](https://www.amazon.com/Sonoff-Consumption-Monitoring-Appliances-Compatible/dp/B06XSD6PD6?ref=ast_p_ei)*
* [Sonoff TH16 (Flashed with Tasmota)](https://www.amazon.com/Sonoff-TH16-Temperature-Monitoring-Compatible/dp/B06XTNSJ46)*
* [OpenGarage Door Controller ](https://www.amazon.com/OpenGarage-WiFi-enabled-Garage-Door-Opener/dp/B01M4RL0CL)*
* [Kuled WiFi Light Switches (Flashed with Tasmota)](https://www.amazon.com/Required-Wireless-Requires-Schedule-Compatible/dp/B079FDTG7T)*
* [Firefly Electronix Wifi Doorbell](https://www.fireflyelectronix.com/product/wifidoorbell)*

### Zwave / Zigbee Devices
* [Ikea TRÅDFRI LED Bulbs](http://www.ikea.com/us/en/catalog/products/20318267/)
* [Ikea TRÅDFRI Remote](http://www.ikea.com/us/en/catalog/products/20303317/)
* [Mono Price Z-wave Door Tilt Sensor ](https://www.monoprice.com/product?p_id=11987)
* [GE Z-Wave Plus Hinge Pin Door Sensors ](https://www.amazon.com/GE-Wireless-Attaches-Existing-32563/dp/B01KQDIUAW/)
* [Aeotec Z-wave Range Extender ](https://www.amazon.com/Aeotec-Range-Extender-Z-Wave-repeater/dp/B01M6CKJXC)
* [Dome Miniature, Z-Wave Plus Door/Window Sensor](https://www.amazon.com/Dome-Home-Automation-Miniature-DMWD1/dp/B01JGMZNNG)
* [Go Control Thermostat](https://www.gocontrol.com/detail.php?productId=3)

### Hardwired Devices
* [Cyberpower CP1500PFCLCD UPS ](https://www.amazon.com/CyberPower-CP1500PFCLCD-Sinewave-Outlets-Mini-Tower/dp/B00429N19W) used to detect power outages and keep network and HA running in a power outage.
* [Ubiquiti Unifi AP-AC Long Range - Wireless Access Point](https://www.ui.com/unifi/unifi-ap-ac-lr/) used for presence detection
* [Ubiquiti Unifi Security Gateway](https://www.ui.com/unifi-routing/usg/) used for network stats
* [Ikea TRÅDFRI Gateway](http://www.ikea.com/us/en/catalog/products/00337813/) *

*Block these from external network access and they will still work on your local network with Home Assistant.

# Front End Screen Shots:

## Home
<p align="center">
  <img src="https://raw.githubusercontent.com/SilvrrGIT/HomeAssistant/master/www/rooms.png">
</p>

## Switches
<p align="center">
  <img src="https://raw.githubusercontent.com/SilvrrGIT/HomeAssistant/master/www/switches.png">
</p>

## HVAC
<p align="center">
  <img src="https://raw.githubusercontent.com/SilvrrGIT/HomeAssistant/master/www/hvac.png">
</p>

## Device Status
<p align="center">
  <img src="https://raw.githubusercontent.com/SilvrrGIT/HomeAssistant/master/www/devicestatus.png">
</p>

## Network Status
<p align="center">
  <img src="https://raw.githubusercontent.com/SilvrrGIT/HomeAssistant/master/www/networkstatus.png">
</p>

## Home Assistant Status
<p align="center">
  <img src="https://raw.githubusercontent.com/SilvrrGIT/HomeAssistant/master/www/ha.png">
</p>

## Raspberry Pi2B Status
<p align="center">
  <img src="https://raw.githubusercontent.com/SilvrrGIT/HomeAssistant/master/www/rpi2status.png">
</p>

## Weather
<p align="center">
  <img src="https://raw.githubusercontent.com/SilvrrGIT/HomeAssistant/master/www/weather.png">
</p>

## Automations
<p align="center">
  <img src="https://raw.githubusercontent.com/SilvrrGIT/HomeAssistant/master/www/automations.png">
</p>

## Trains
<p align="center">
  <img src="https://raw.githubusercontent.com/SilvrrGIT/HomeAssistant/master/www/statsndata.png">
</p>


# Questions?

The best way to get help on Home Assistant is the [Home Assistant Forum](https://community.home-assistant.io/).  If you have a specific question about my configuration send me a Private Message on the HA forum, my username over there is [Silvrr](https://community.home-assistant.io/u/silvrr/).  If you have found something incorrect, please submit an issue here on Github and I will get it fixed.
