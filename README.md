
<p align="center">
  <img src="https://raw.githubusercontent.com/SilvrrGIT/HomeAssistant/master/ScreenShots/HomeAssistant.png">
</p>

These are the [Home Assistant](https://home-assistant.io/) configuration files used in my Home Assistant (HA) setup. I relied on repositories of other HA users quite a bit when I was getting started for ideas and example code.  Hopefully this repository will help someone else who is getting started. 

If you are just gettting started with Home Assistant I highly reccomend checking out this [YouTube Series](https://www.youtube.com/playlist?list=PLgtGAtCt_hGTc_GAEmMhQ_XVs80mZoBIG).  It helped me a lot in the beginning and I still frequently reference some videos today.  I also strongly reccomend you read the [Home Assistant Docs](https://home-assistant.io/docs/).  So many questions asked on the  [Home Assistant Forum](https://community.home-assistant.io/) could be solved by reading the docs. I have tried to include links in my files to the associated guidance documents for easy reference.  

# Hardware Running HA:
* __[Dell Optiplex 9010 Small Form Factor (SFF)](http://i.dell.com/sites/doccontent/shared-content/data-sheets/en/Documents/Dell_OptiPlex_9010_spec_sheet.pdf)__
This desktop has a i5 3470T (low power CPU) swapped in.  The machine is running  __[VMWare ESXi](https://www.vmware.com/products/esxi-and-esx.html)__ which allows me to run mutiple virtual machines on the same physical hardware.  I run my router/firewall off the same machine.  

* __[Aeotec Z-Stick Gen 5 ](https://www.amazon.com/Aeotec-Z-Stick-Z-Wave-create-gateway/dp/B00X0AWA6E/)__

* __[Raspberry Pi Zero W ](https://www.raspberrypi.org/products/raspberry-pi-zero-w/)__ 
This is a remote Home Assistant instance using the __[Hassbian Install Method ](https://home-assistant.io/docs/installation/hassbian/installation/)__ and running version __0.54.0__.  This is used for remote temperature and motion detection.  This Pi also serves as the control for my 433 MHz switches.  This instance is connected to my main instance using MQTT statestream.

# Installation Process:
I'm currently running [Home Assistant](https://home-assistant.io) version __0.60.0__. My preferred installation method is an [Ubuntu Server](https://www.ubuntu.com/server) instance and following the [Python Virtual Enviroment](https://home-assistant.io/docs/installation/virtualenv/) installation instructions for Home Assistant.  For anyone running a Raspberry Pi, I highly reccomend using the __[Hassbian Install Method. ](https://home-assistant.io/docs/installation/hassbian/installation/)__

I setup my Mosquitto MQTT Broker using the instructions in [this video](https://www.youtube.com/watch?v=AsDHEDbyLfg&t)

# Security:
I think this is an often overlooked part of any internet connected project.  I am far from a security expert, however, these are the steps I have taken to add some level of security to my Home Assistant instance. 
- Anything that doesn't need an internet connection is blocked from any inbound and outbound traffic.
- I seperate my traffic into different subnets and by default these subnets cannot talk to one another.  For example my devices on Wifi only have access to the internet or my Local Area Networ (LAN) if I allow it.  
- Using the tools in [PFSense](https://www.pfsense.org/) I block a large amount of traffic from ever reaching my network using PFblockerNG and a combonation of published lists, and custom rules.
- All the traffic connecting to my Home Assistant instance is logged and e-mailed to me regularly.  I only access my instance from a few devices to it is pretty easy to spot traffic that is not 'normal'.
- Failed login attempts to the Home Assistant Front end generate a [notification](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/pc_security.yaml#L23) to me with the source IP.  
- My Home Assistant Traffic is encrypted with [Let's Encrypt](https://letsencrypt.org/).  I used [this guide](https://www.splitbrain.org/blog/2017-08/10-homeassistant_duckdns_letsencrypt) to get it setup.

# Editing the Configuration Files:
What works for me is creating a Samba share that I can then edit on any computer in my house.  

For setting up Samba see this video: [Samba Setup](https://www.youtube.com/watch?v=iQwWEsuRWUw&t=5s)

After you have the Samba share setup, I like to use [Atom](https://atom.io/) to edit my files.  It works on both Windows and Linux, has a great interface and some nice features. [NotePad++](https://notepad-plus-plus.org/) is also easy to use and is a bit more lightweight than Atom (no Linux support though)

# Connected Devices:

### Cloud Controlled Devices:
* __[Amazon Echo Dot](https://www.amazon.com/All-New-Amazon-Echo-Dot-Add-Alexa-To-Any-Room/dp/B01DFKC2SO)__
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
* __[433Mhz Rf Transmitter and Receiver](https://www.amazon.com/SMAKN%C2%AE-433Mhz-Transmitter-Receiver-Arduino/dp/B00M2CUALS/ref=as_li_ss_tl?s=electronics&ie=UTF8&qid=1464322826&sr=1-1&keywords=433+rf&linkCode=sl1&tag=brau01-20&linkId=5c11978c5ddf767c9b4b2228ab61fed4)__
* __[Etekcity Wireless Remote Control Electrical Outlet Switches](https://www.amazon.com/Etekcity-Wireless-Electrical-Household-Appliances/dp/B00DQELHBS)__
* __[DHT22 Temperature And Humidity Sensor](https://www.amazon.com/Gikfun-Temperature-Humidity-Arduino-EK1196/dp/B00Z5Y5UEM/ref=sr_1_6?s=electronics&ie=UTF8&qid=1498790057&sr=1-6&keywords=DHT22)__
* __[Mono Price Z-wave Door Tilt Sensor ](https://www.monoprice.com/product?p_id=11987)__
* __[Cyberpower CP1500PFCLCD UPS ](https://www.amazon.com/CyberPower-CP1500PFCLCD-Sinewave-Outlets-Mini-Tower/dp/B00429N19W)__ used to detect power outages and keep network and HA running in a power outage.
* __[Synology DiskStation DS216J ](https://www.amazon.com/Synology-DiskStation-3-5-Inches-1xGigabit-DS216J/dp/B01BNPT1EG)__* used as a NAS (ovbiously) and as the NUT server. 
* __[OpenGarage Door Controller ](https://www.amazon.com/OpenGarage-WiFi-enabled-Garage-Door-Opener/dp/B01M4RL0CL)__*
* __[Aeotec Z-wave Range Extender ](https://www.amazon.com/Aeotec-Range-Extender-Z-Wave-repeater/dp/B01M6CKJXC)__

*Block these from external network access and they will still work on your local network with Home Assistant.

# Automations:

### Bedtime_Notifications.yaml Automations:
These notifications are triggered after 10:00 PM and I plug my phone in (generally I am in bed when this happens).  These send a iOS app notification with an action option to turn the device off.  These are primarily a power saving item.
* __[Notify Me if the garage door is open and I am in bed ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/bedtime_notifications.yaml#L1)__
* __[Notify Me if the Home Theater PC is left on and I am in bed ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/bedtime_notifications.yaml#L26)__
* __[Notify Me if the Desktop PC is left on and I am in bed ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/bedtime_notifications.yaml#L65)__
* __[Notify Me if the Living Room Lamps are left on and I am in bed ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/bedtime_notifications.yaml#L103)__

<p align="center"> <img src="https://github.com/SilvrrGIT/HomeAssistant/blob/master/ScreenShots/iosnotification.jpg"><img src="https://github.com/SilvrrGIT/HomeAssistant/blob/master/ScreenShots/ios%20action.jpg">
</p> 

### Device Offline.yaml Automations:
This notification is used to notify me if on of my home automation devices goes offline.  Generally this is someone flipping a switch which cuts the power or a network connectivy issue.
* __[Notify Me if a Home Automation Device is offline ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/deviceoffline.yaml)__

### Door Security.yaml Automations:
These automations are used to notify me when a door is opened when no one is home or the garage door is left open when we leave.
* __[Notify Me if the interior garage door is opened and I am away ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/door_security.yaml#L2)__
* __[Notify Me if the exterior garage door is opened and I am away ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/door_security.yaml#L33)__
* __[Notify Me if the front door is opened and I am away ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/door_security.yaml#L58)__
* __[Notify Me if the garage door is left open when I leave ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/door_security.yaml#L83)__

### Feed the dog.yaml Automations:
These automations are used to turn a light on to signify the dog needs to be fed.  A amazon dash button is used to signify the dog has been fed which either turns off the notification light or turn off the automation. 
* __[Turn on Notification Light AM ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/feed_the_dog.yaml#L1)__
* __[Turn on Notification Light PM ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/feed_the_dog.yaml#L18)__
* __[Turn off The AM Automation and Notification Light AM ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/feed_the_dog.yaml#L35)__
* __[Turn off The PM Automation and Notification Light PM ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/feed_the_dog.yaml#L56)__
* __[Reset all the Automations at 1:00 AM ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/feed_the_dog.yaml#L77)__

### IP Change.yaml
* __[Notify me with the new IP if my home IP address Changes ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/ip_change.yaml)__

### Leaving_Notifications.yaml Automations:
These notifications are triggered when I leave my home zone and no one is home.  These send a iOS app notification with an action option to turn the device off. These are primarily a power saving item and are the same framework as the bedtime notification as above. 
* __[Notify Me if the Home Theater PC is left on and no one is home ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/leaving_notifications.yaml#L1)__
* __[Notify Me if the Desktop PC is left on and no one is home ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/leaving_notifications.yaml#L47)__
* __[Notify Me if the Living Room Lamps are left on and no one is home ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/leaving_notifications.yaml#L92)__

### Living Room Lamps.yaml Automations:
These lamps are the main light source when you walk in through the garage (our primary point of entry).  
* __[Turn on the living room lamps at sunset ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/living_room_lamps.yaml#L1)__
* __[Turn on the living room lamps when somone comes home and its dark out ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/living_room_lamps.yaml#L16)__
* __[Turn off the living room lamps at midnight ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/living_room_lamps.yaml#L39)__

### Low_Battery_Adams_iPhone Automations:
This is to notify me to charge my phone when I am at work.  Generally I forget to charge my phone and it is either low or dead for the train ride home.    
* __[Charge my phone notification at 50 and 30% battery ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/low_battery_adam_phone.yaml)__

### Nest.yaml Automations:
I found it easier to automate my nest myself rather than using the nest features.  
* __[Set Thermostat to Away when everyone leaves for work ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/nest.yaml#L1)__
* __[Turn off Away mode at 4:00 PM (pre heat/cool the house before arriving home) ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/nest.yaml#L48)__
* __[Turn off Away mode if someone arrives home ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/nest.yaml#L76)__
* __[If HVAC fan hasn't run for an hour, run it for 10 minutes ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/nest.yaml#L102)__

### Notification bulb.yaml
* __[Set the nofication bulb to the color selected ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/notification_bulb.yaml#L1)__
* __[Set the notfication bulb to a white color that matches the other lamps in the room ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/notification_bulb.yaml#L21)__

### Outside Lights.yaml
* __[Turn on the outside lights at sunset ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/outside_Lights.yaml#L1)__
* __[Turn off the outside lights at sunrise ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/outside_Lights.yaml#L18)__

### PC_Security.yaml Automations:
* __[Notify me if the Desktop PC is turned on while away ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/pc_security.yaml#L1)__
* __[Notify me if there is a failed login attempt to the HA front end ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/pc_security.yaml#L23)__
* __[Notify me of a new device added to my Wifi network ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/pc_security.yaml#L42)__

### UPS.yaml Automations:
* __[Notify me if there is a power outage ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/ups.yaml#L1)__
* __[Notify me when power is restored ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/ups.yaml#L30)__

### Vacation Mode.yaml Automations:
* __[Turn On Vacation Mode with Vacation Mode Switch ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/vacation_mode.yaml#L1)__
* __[Turn Off Vacation Mode with Vacation Mode Switch  ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/vacation_mode.yaml#L43)__

# Control Panel / Front End Screen Shots:

## Rooms
<p align="center">
  <img src="https://raw.githubusercontent.com/SilvrrGIT/HomeAssistant/master/ScreenShots/Rooms.PNG">
</p>

## Device Status
<p align="center">
  <img src="https://raw.githubusercontent.com/SilvrrGIT/HomeAssistant/master/ScreenShots/DeviceStatus.PNG">
</p>

## Home Assistant Status
<p align="center">
  <img src="https://raw.githubusercontent.com/SilvrrGIT/HomeAssistant/master/ScreenShots/HA.PNG">
</p>

## Automations
<p align="center">
  <img src="https://raw.githubusercontent.com/SilvrrGIT/HomeAssistant/master/ScreenShots/Automations.PNG">
</p>

## Switches
<p align="center">
  <img src="https://raw.githubusercontent.com/SilvrrGIT/HomeAssistant/master/ScreenShots/Switches.PNG">
</p>

## Weather
<p align="center">
  <img src="https://raw.githubusercontent.com/SilvrrGIT/HomeAssistant/master/ScreenShots/Weather.PNG">
</p>

# Questions?

The best way to get help on Home Assistant is the [Home Assistant Forum](https://community.home-assistant.io/).  If you have a specific question about my configuration send me a Private Message on the HA forum, my username over there is [Silvrr](https://community.home-assistant.io/u/silvrr/).  If you have found something incorrect, please submit an issue here on Github and ill get it fixed.

### My Device Reviews on the Home Assistant Forum:
* __[Xiaomi Yeelights](https://community.home-assistant.io/t/yeelight-led-bulbs-rgb-and-white-bulbs/14620)__
* __[Edimax Wi-Fi Smart Plugs (SP-2101W)](https://community.home-assistant.io/t/edimax-wi-fi-smart-switch-plug-sp-2101w/9036)__
