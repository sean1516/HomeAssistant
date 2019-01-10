
<p align="center">
  <img src="https://github.com/home-assistant/home-assistant-assets/blob/master/loading-screen.gif">
</p>

These are the [Home Assistant](https://home-assistant.io/) configuration files used in my Home Assistant (HA) setup. I relied on repositories of other HA users quite a bit when I was getting started for ideas and example code.  Hopefully this repository will help someone else who is getting started. 

# Automations:
A detailed description of each of my automations and a link to the yaml file is located [HERE](https://github.com/SilvrrGIT/HomeAssistant/tree/master/automation#bedtime_notificationsyaml-automations)

This is the most important part of Home Assistant!  Remote control and voice commmands are nice, however, that is not home automation, just remote control.  Automations should make your life easier, look at what you do everyday, the simplest things, and automate them.  To me Home Automation is collecting data about your home and automatically acting based on that data.

# Server Running My Home Assistant Setup:
* __[Dell Optiplex 9010 Small Form Factor (SFF) ](http://i.dell.com/sites/doccontent/shared-content/data-sheets/en/Documents/Dell_OptiPlex_9010_spec_sheet.pdf)__ This desktop has a i5 3470T (low power CPU) swapped in.  The machine is running  [VMWare ESXi](https://www.vmware.com/products/esxi-and-esx.html) which is a bare metal hypervisor that allows me to run mutiple virtual machines on the same physical hardware.  The HA virtual machine is given 2 cores, 2GB of RAM and a 16GB disk. I also run a [Router](https://www.pfsense.org/) and NAS from the same box.  

The virtual machine is running [Ubuntu Server 16.04.5](https://www.ubuntu.com/) as an operating system and [Hass.io](https://www.home-assistant.io/hassio/).  I am also running the following add-ons:

* __[Backup to Google Drive](https://github.com/samccauley/addon-hassiogooglebackup)__ Store a backup of my config in a google drive account. 
* __[Dasshio](https://github.com/theastropath/dasshio)__ Simple add-on to use Amazon Dash buttons to make service calls. 
* __[DuckDNS](www.home-assistant.io/addons/duckdns/)__ Provides DuckDNS updates and creates a Lets Encrypt Certificate
* __[Mosquitto MQTT broker](https://www.home-assistant.io/addons/mosquitto/)__ MQTT Broker
* __[Network UPS Tools](https://github.com/colindunn/hassio-addons)__ A NUT Server
* __[RPC Shutdown](https://www.home-assistant.io/addons/rpc_shutdown/)__ Shutdown Windows Computers
* __[SSH](https://www.home-assistant.io/addons/ssh/)__ SSH for Hass.io
* __[Samba](https://www.home-assistant.io/addons/samba/)__ Samba share of config files and backup files
* __[TasmoAdmin](https://github.com/hassio-addons/addon-tasmoadmin)__ Easy managment of tasmota flashed devices
* __[Unifi Controller](https://github.com/hassio-addons/addon-unifi)__ Unifi Device Controller

I'm currently running [Home Assistant](https://home-assistant.io) version __0.84.5__.

# Network & Home Assistant Instance Security:
I think this is an often overlooked part of any internet connected project.  I am far from a security expert, however, these are the steps I have taken to add some level of security to my Home Assistant instance.
- Simple protections like enabling a [password](https://github.com/SilvrrGIT/HomeAssistant/blob/master/configuration.yaml#L45) and limiting the number of incorrect [login attempts](https://github.com/SilvrrGIT/HomeAssistant/blob/master/configuration.yaml#L48).
- Anything that doesn't need an internet connection is blocked from any inbound or outbound traffic at the router level. 
- Using the tools in PFSense I block a large amount of traffic from ever reaching my network using PFblockerNG, Suricata and a combination of published lists, and custom rules.
- Failed login attempts to the Home Assistant Front end generate a [notification](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/pc_security.yaml#L23) to me with the source IP.
- My Home Assistant Traffic is encrypted with [Let's Encrypt](https://letsencrypt.org/).  I used [this guide](https://github.com/SilvrrGIT/HomeAssistant/wiki/Let's-Encrypt-Setup-(Hassbian,-Python-Virtual-Environment)) to get it setup on Hassbian and now use the __[DuckDNS](www.home-assistant.io/addons/duckdns/)__ add-on in Hass.io to do the same thing.
- [Test your secuirty and test it often](https://community.home-assistant.io/t/test-your-security-and-test-it-often/76354).

# Editing the Configuration Files:
What works for me is creating a Samba share that I can then edit on any computer in my house.  I am doing this with the Samba add-on for Hass.io.  For other install methods [this](https://github.com/SilvrrGIT/HomeAssistant/wiki/Hassbian-Quick-Reference-Sheet#setting-up-a-samba-share) is a good tutorial. 

After you have the Samba share setup, I like to use [Atom](https://atom.io/) to edit my files.  It works on both Windows and Linux, has a great interface and some nice features. [NotePad++](https://notepad-plus-plus.org/) is also easy to use and is a bit more lightweight than Atom (no Linux support though)

# A Few Stats On my Setup:
| Components Used | Network Devices | Lights | Binary Sensors | Switches | Automations | Scripts | Sensors | Zwave Devices |
|:----------:|:---------------:|:------:|:--------------:|:--------:|:-----------:|:-------:|:-------:|:-------------:|
| 86         |39               |8       |6               |17        |72           |5        |120      |7              |         
# Connected Devices:

## Cloud Controlled Devices:
* __[Amazon Echo Dot](https://www.amazon.com/All-New-Amazon-Echo-Dot-Add-Alexa-To-Any-Room/dp/B01DFKC2SO)__ Used for voice commands to turn devices on/off using the [Emulated Hue Component](https://home-assistant.io/components/emulated_hue/)
* __[Amazon Fire TV Stick 4K](https://www.amazon.com/Introducing-Fire-TV-Stick-4K-with-All-New-Alexa-Voice-Remote/dp/B079QHML21)__ 
* __[Apple iCloud Presence Detection / iPhone XR](https://www.apple.com/iphone-xr/)__

## Wifi Connected Devices
* __[Xiaomi Yeelight RGBW E27 Smart LED Bulbs](http://www.gearbest.com/smart-lighting/pp_361555.html)__ *
* __[Xiaomi Yeelight E27 Smart LED Bulbs](http://www.gearbest.com/smart-light-bulb/pp_278478.html)__ *
* __[Broadlink RM Mini 3](https://www.amazon.com/BroadLink-Control-Universal-Remote-RMMINI3-EN/dp/B01FK2SDOC/ref=sr_1_2?ie=UTF8&qid=1499475366&sr=8-2&keywords=broadlink+mini3)__*
* __[Sonoff Basic (Flashed with Tasmota)](https://www.amazon.com/Sonoff-Wireless-Modified-Low-cost-Compatible/dp/B06WWNBD3Y?ref=ast_p_ei)__*
* __[Sonoff POW (Flashed with Tasmota)](https://www.amazon.com/Sonoff-Consumption-Monitoring-Appliances-Compatible/dp/B06XSD6PD6?ref=ast_p_ei)__*
* __[OpenGarage Door Controller ](https://www.amazon.com/OpenGarage-WiFi-enabled-Garage-Door-Opener/dp/B01M4RL0CL)__*
* __[Kuled WiFi Light Switches (Flashed with Tasmota)](https://www.amazon.com/Required-Wireless-Requires-Schedule-Compatible/dp/B079FDTG7T)__*

## Zwave / Zigbee Devices
* __[Ikea TRÅDFRI LED Bulbs](http://www.ikea.com/us/en/catalog/products/20318267/)__
* __[Ikea TRÅDFRI Remote](http://www.ikea.com/us/en/catalog/products/20303317/)__
* __[Mono Price Z-wave Door Tilt Sensor ](https://www.monoprice.com/product?p_id=11987)__
* __[GE Z-Wave Plus Hinge Pin Door Sensors ](https://www.amazon.com/GE-Wireless-Attaches-Existing-32563/dp/B01KQDIUAW/)__
* __[Aeotec Z-wave Range Extender ](https://www.amazon.com/Aeotec-Range-Extender-Z-Wave-repeater/dp/B01M6CKJXC)__
* __[Dome Miniature, Z-Wave Plus Door/Window Sensor](https://www.amazon.com/Dome-Home-Automation-Miniature-DMWD1/dp/B01JGMZNNG)__
* __[Go Control Thermostat](https://www.irisbylowes.com/products/gocontrol-programmable-thermostat/)__

## Hardwired Devices
* __[Cyberpower CP1500PFCLCD UPS ](https://www.amazon.com/CyberPower-CP1500PFCLCD-Sinewave-Outlets-Mini-Tower/dp/B00429N19W)__ used to detect power outages and keep network and HA running in a power outage.
* __[Ubiquiti Unifi Ap-AC Long Range - Wireless Access Point](https://www.amazon.com/Ubiquiti-Unifi-Ap-AC-Long-Range/dp/B015PRCBBI)__ used for presence detection
* __[Ikea TRÅDFRI Gateway](http://www.ikea.com/us/en/catalog/products/00337813/)__*

*Block these from external network access and they will still work on your local network with Home Assistant.

# Front End Screen Shots:

## Home
<p align="center">
  <img src="https://raw.githubusercontent.com/SilvrrGIT/HomeAssistant/master/www/home.png">
</p>

## Device Status
<p align="center">
  <img src="https://raw.githubusercontent.com/SilvrrGIT/HomeAssistant/master/www/devicestatus.png">
</p>

## Home Assistant Status
<p align="center">
  <img src="https://raw.githubusercontent.com/SilvrrGIT/HomeAssistant/master/www/ha.png">
</p>

## Connected Devices
<p align="center">
  <img src="https://raw.githubusercontent.com/SilvrrGIT/HomeAssistant/master/www/connecteddevices.png">
</p>

## Automations
<p align="center">
  <img src="https://raw.githubusercontent.com/SilvrrGIT/HomeAssistant/master/www/automations.png">
</p>

## Switches
<p align="center">
  <img src="https://raw.githubusercontent.com/SilvrrGIT/HomeAssistant/master/www/switches.png">
</p>

## Weather
<p align="center">
  <img src="https://raw.githubusercontent.com/SilvrrGIT/HomeAssistant/master/www/weather.png">
</p>

# Questions?

The best way to get help on Home Assistant is the [Home Assistant Forum](https://community.home-assistant.io/).  If you have a specific question about my configuration send me a Private Message on the HA forum, my username over there is [Silvrr](https://community.home-assistant.io/u/silvrr/).  If you have found something incorrect, please submit an issue here on Github and ill get it fixed.
