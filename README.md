
<p align="center">
  <img src="https://github.com/home-assistant/home-assistant-assets/blob/master/loading-screen.gif">
</p>

<p align="center">
 <img src="https://img.shields.io/github/last-commit/SilvrrGIT/HomeAssistant.svg?style=plasticr">
</p>

These are the [Home Assistant](https://home-assistant.io/) configuration files used in my Home Assistant (HA) setup. I relied on repositories of other HA users quite a bit when I was getting started for ideas and example code.  Hopefully this repository will help someone else who is getting started. 

If you are just getting started with Home Assistant I highly recommend checking out this [YouTube Series](https://www.youtube.com/playlist?list=PLgtGAtCt_hGTc_GAEmMhQ_XVs80mZoBIG).  It helped me a lot in the beginning and I still frequently reference some videos today.  I also strongly recommend you read the [Home Assistant Docs](https://home-assistant.io/docs/).  So many questions asked on the  [Home Assistant Forum](https://community.home-assistant.io/) could be solved by reading the docs. I have tried to include links in my files to the associated guidance documents for easy reference.  

# Hardware Running HA:
* __[Raspberry Pi 3 Model B+ ](https://www.amazon.com/dp/B07BDR5PDW/ref=psdc_1048424_t2_B07BFH96M3)__ 

* __[Aeotec Z-Stick Gen 5 ](https://www.amazon.com/Aeotec-Z-Stick-Z-Wave-create-gateway/dp/B00X0AWA6E/)__

# Installation Process:
I'm currently running [Home Assistant](https://home-assistant.io) version __0.67.1__. My preferred installation method is the [Hassbian Install Method. ](https://home-assistant.io/docs/installation/hassbian/installation/)

# Network & Home Assistant Instance Security:
I think this is an often overlooked part of any internet connected project.  I am far from a security expert, however, these are the steps I have taken to add some level of security to my Home Assistant instance.
- Simple protections like enabling a [password](https://github.com/SilvrrGIT/HomeAssistant/blob/master/configuration.yaml#L34) and limiting the number of incorrect [login attempts](https://github.com/SilvrrGIT/HomeAssistant/blob/master/configuration.yaml#L39).
- Anything that doesn't need an internet connection is blocked from any inbound or outbound traffic at the router level.
- I separate my traffic into different subnets and by default these subnets cannot talk to one another.  For example my devices on Wifi only have access to the internet or my Local Area Network (LAN) if I allow it.  
- Using the tools in [PFSense](https://www.pfsense.org/) I block a large amount of traffic from ever reaching my network using PFblockerNG and a combination of published lists, and custom rules.
- All the traffic connecting to my Home Assistant instance is logged and e-mailed to me regularly.  I only access my instance from a few devices to it is pretty easy to spot traffic that is not 'normal'.
- Failed login attempts to the Home Assistant Front end generate a [notification](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/pc_security.yaml#L23) to me with the source IP.  
- My Home Assistant Traffic is encrypted with [Let's Encrypt](https://letsencrypt.org/).  I used [this guide](https://www.splitbrain.org/blog/2017-08/10-homeassistant_duckdns_letsencrypt) to get it setup.

# Editing the Configuration Files:
What works for me is creating a Samba share that I can then edit on any computer in my house.  

For setting up Samba see this video: [Samba Setup](https://www.youtube.com/watch?v=iQwWEsuRWUw&t=5s)

After you have the Samba share setup, I like to use [Atom](https://atom.io/) to edit my files.  It works on both Windows and Linux, has a great interface and some nice features. [NotePad++](https://notepad-plus-plus.org/) is also easy to use and is a bit more lightweight than Atom (no Linux support though)

# Connected Devices:

### Cloud Controlled Devices:
* __[Amazon Echo Dot](https://www.amazon.com/All-New-Amazon-Echo-Dot-Add-Alexa-To-Any-Room/dp/B01DFKC2SO)__ Used for voice commands to turn devices on/off using the [Emulated Hue Component](https://home-assistant.io/components/emulated_hue/)
* __[Nest Thermostat](https://nest.com/thermostat/meet-nest-thermostat/)__
* __[iCloud Presence Detection / iPhone 8 Plus](https://www.apple.com/shop/buy-iphone/iphone-8)__

### Local Network Devices:
* __[Xiaomi Yeelight RGBW E27 Smart LED Bulbs](http://www.gearbest.com/smart-lighting/pp_361555.html)__ *
* __[Xiaomi Yeelight E27 Smart LED Bulbs](http://www.gearbest.com/smart-light-bulb/pp_278478.html)__ *
* __[Ikea TRÅDFRI Gateway](http://www.ikea.com/us/en/catalog/products/00337813/)__
* __[Ikea TRÅDFRI LED Bulbs](http://www.ikea.com/us/en/catalog/products/20318267/)__
* __[Ikea TRÅDFRI Remote](http://www.ikea.com/us/en/catalog/products/20303317/)__
* __[Edimax Wi-Fi Smart Plugs (SP-2101W)](https://www.amazon.com/Edimax-Wi-Fi-Energy-Management-SP-2101W/dp/B00N4OBJAO/)__ *
* __[Broadlink RM Mini 3](https://www.amazon.com/BroadLink-Control-Universal-Remote-RMMINI3-EN/dp/B01FK2SDOC/ref=sr_1_2?ie=UTF8&qid=1499475366&sr=8-2&keywords=broadlink+mini3)__*
* __[GE Z-Wave Plus Hinge Pin Door Sensors ](https://www.amazon.com/GE-Wireless-Attaches-Existing-32563/dp/B01KQDIUAW/)__
* __[Amazon Dash Button ](https://www.amazon.com/Dash-Buttons/b?ie=UTF8&node=10667898011)__* Used as button to turn on/off feed the dog automations
* __[Mono Price Z-wave Door Tilt Sensor ](https://www.monoprice.com/product?p_id=11987)__
* __[Cyberpower CP1500PFCLCD UPS ](https://www.amazon.com/CyberPower-CP1500PFCLCD-Sinewave-Outlets-Mini-Tower/dp/B00429N19W)__ used to detect power outages and keep network and HA running in a power outage.
* __[Synology DiskStation DS216J ](https://www.amazon.com/Synology-DiskStation-3-5-Inches-1xGigabit-DS216J/dp/B01BNPT1EG)__* used as a NAS (obviously) and as the NUT server. 
* __[OpenGarage Door Controller ](https://www.amazon.com/OpenGarage-WiFi-enabled-Garage-Door-Opener/dp/B01M4RL0CL)__*
* __[Aeotec Z-wave Range Extender ](https://www.amazon.com/Aeotec-Range-Extender-Z-Wave-repeater/dp/B01M6CKJXC)__
* __[Dome Miniature, Z-Wave Plus Door/Window Sensor](https://www.amazon.com/Dome-Home-Automation-Miniature-DMWD1/dp/B01JGMZNNG)__
* __[Ubiquiti Unifi Ap-AC Long Range - Wireless Access Point](https://www.amazon.com/Ubiquiti-Unifi-Ap-AC-Long-Range/dp/B015PRCBBI)__ used for presence detection

*Block these from external network access and they will still work on your local network with Home Assistant.

# Automations:
A detailed description of each of my automations and a link to the yaml file is located [HERE](https://github.com/SilvrrGIT/HomeAssistant/tree/master/automation#bedtime_notificationsyaml-automations)

# Control Panel / Front End Screen Shots:

## Home
<p align="center">
  <img src="https://raw.githubusercontent.com/SilvrrGIT/HomeAssistant/master/ScreenShots/home.png">
</p>

## Device Status
<p align="center">
  <img src="https://raw.githubusercontent.com/SilvrrGIT/HomeAssistant/master/ScreenShots/devicestatus.png">
</p>

## Home Assistant Status
<p align="center">
  <img src="https://raw.githubusercontent.com/SilvrrGIT/HomeAssistant/master/ScreenShots/ha.png">
</p>

## Automations
<p align="center">
  <img src="https://raw.githubusercontent.com/SilvrrGIT/HomeAssistant/master/ScreenShots/automations.png">
</p>

## Switches
<p align="center">
  <img src="https://raw.githubusercontent.com/SilvrrGIT/HomeAssistant/master/ScreenShots/switches.png">
</p>

## Weather
<p align="center">
  <img src="https://raw.githubusercontent.com/SilvrrGIT/HomeAssistant/master/ScreenShots/weather.png">
</p>

## Other
<p align="center">
  <img src="https://raw.githubusercontent.com/SilvrrGIT/HomeAssistant/master/ScreenShots/Other.PNG">
</p>

# Questions?

The best way to get help on Home Assistant is the [Home Assistant Forum](https://community.home-assistant.io/).  If you have a specific question about my configuration send me a Private Message on the HA forum, my username over there is [Silvrr](https://community.home-assistant.io/u/silvrr/).  If you have found something incorrect, please submit an issue here on Github and ill get it fixed.

### My Device Reviews on the Home Assistant Forum:
* __[Xiaomi Yeelights](https://community.home-assistant.io/t/yeelight-led-bulbs-rgb-and-white-bulbs/14620)__
* __[Edimax Wi-Fi Smart Plugs (SP-2101W)](https://community.home-assistant.io/t/edimax-wi-fi-smart-switch-plug-sp-2101w/9036)__
