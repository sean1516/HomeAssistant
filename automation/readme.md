## Automations
<p align="center">
  <img src="https://raw.githubusercontent.com/SilvrrGIT/HomeAssistant/master/www/automations.png">
</p>

### Bedroom Fan.yaml Automations:
__[File Link](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/bedroom_fan.yaml)__
Automations to turn on/off the ceiling fan in our bedroom.  Its a vaulted ceiling and in the summer a lot of hot air gets trapped up there and in the winter the same thing happens to a less notable extent.
* When the HVAC turns on, turn on the fan to circulate the air
* When the HVAC turns off, turn off the fan

### Bedtime_Notifications.yaml Automations:
__[File Link](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/bedtime_notifications.yaml)__

These notifications are triggered after 8:00 PM when I plug my phone in (generally I am in bed when this happens).  These send an iOS app notification with an action option to turn the device off.  These are primarily a power saving items.
* Notify Me if the garage door is open and I am in bed 
* Notify Me if the Desktop PC is left on and I am in bed 
* Notify Me if the Living Room Lamps are left on and I am in bed

<p align="center"> <img src="https://github.com/SilvrrGIT/HomeAssistant/blob/master/www/iosnotification.jpg"><img src="https://github.com/SilvrrGIT/HomeAssistant/blob/master/www/ios%20action.jpg">
</p>

### Cert Update.yaml Automation:
__[File Link](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/certupdate.yaml)__

This notification is used to notify me if my Lets Encrypt certificate does not auto renew after the days remaining in the certificate validity goes below 28 days.  It should auto renew at 30 days.  	

### CTA.yaml Automation:
__[File Link](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/cta.yaml)__

These automations update my CTA bus tracker sensors when on.  They are by default off.  I only use the CTA data when leaving work on a weekday so no need to be polling it all day and on the weekends.   

### Device Offline.yaml Automations:
__[File Link](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/deviceoffline.yaml)__

This notification is used to notify me if on of my home automation devices goes offline.  Generally this is someone flipping a switch which cuts the power or a network connectivity issue.
* Notify Me if a Home Automation Device is offline
* Notify Me if a Yeelight is offline

### Door Security.yaml Automations:
__[File Link](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/door_security.yaml)__

These automations are used to notify me when a door is opened when no one is home or the garage door is left open when we leave.
* Notify Me if the interior garage door is opened and I am away
* Notify Me if the exterior garage door is opened and I am away
* Notify Me if the front door is opened and I am away
* Notify Me if the back door is opened and I am away
* Notify Me if the garage door is left open when I leave
* Notify Me when the doorbell is pressed and flash a light in the house

### Downloader.yaml Automations:
__[File Link](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/certupdate.yaml)__

* Notify Me if a downloader download fails
* Notify Me if a downloader download completes

### Feed the dog.yaml Automations:
__[File Link](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/feed_the_dog.yaml)__

These automations are used to turn a light on to signify the dog needs to be fed.  A amazon dash button is used to signify the dog has been fed by turning off the light. 
* Turn on Notification Light AM
* Turn on Notification Light PM
* Turn off the Notification Light When the button is pressed in the morning
* Turn off the Notification Light When the button is pressed in the evening
* Reset everything for the new day

### Garage Light.yaml Automations:
__[File Link](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/garage_light.yaml)__

Simple automations to turn on an overhead light in the garage when the interior garage door opens.  If the light is left on for 5 mintues it automatically turns off. 
* Turn on the light when the garage door opens
* Turn Off Garage Light After 5 Minutes

### Github.yaml Automations:
__[File Link](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/github.yaml)__

Simple automations to let me know if there is a new home assistant version or if there are changes to my github stats. I get notifications of....
* New Homeassistant Versions
* New Github Stars
* New Github Forks
* New Github Subscribers
* Github Issues

### Holiday_Birthday.yaml Automations:
__[File Link](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/holiday_birthday.yaml)__

Notify me if its is a holiday or birthday based on the listed located [here.](https://github.com/SilvrrGIT/HomeAssistant/blob/master/json_data/days.json)

### HomeAssistant.yaml Automations:
__[File Link](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/homeassistant.yaml)__

Some automations for Home Assistant related items.   
* Notify me when Home Assistant starts
* Notify me when Home Assistant is shutting down
* Notify me if an add-on stops working
* Manually update some sensor that will no longer auto update
* Send me a notification if my Home Assistant VM disk gets full
* Notify me if a Zwave device is dead
* Notify me if a battery power sensor battery is getting low
* Notify me if there is a custom component/card update available
* Notify me and restart the nut addon if it stops reporting values

### Leaving Hom.yaml Automations:
__[File Link](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/leaving_home.yaml)__

An automation to turn off light and switches when no one is home.  No sense in these being on with no one home.  

### Leaving_Notifications.yaml Automations:
__[File Link](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/leaving_notifications.yaml)__

These notifications are triggered when I leave my home zone and no one is home.  These send a iOS app notification with an action option to turn the device off. These are primarily a power saving item and are the same framework as the bedtime notification as above. 
* Notify Me if the Desktop PC is left on and no one is home 
* Notify Me if the Living Room Lamps are left on and no one is home 
* Notify Me if the Media Center is left on and no one is home. This is an effort to automate my 'dumb'TV and amplifier based on power usage.  Knowing the power being drawing I can assume which device is left on as they have unique power usage. 

### Living Room Lamps.yaml Automations:
__[File Link](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/living_room_lamps.yaml)__

These lamps are the main light source when you walk in through the garage (our primary point of entry).  
* Turn on the living room lamps at sunset 
* Turn on the living room lamps when somone comes home and its dark out
* Turn off the living room lamps at midnight

### Low_Battery_Adams_iPhone.yaml Automations:
__[File Link](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/low_battery_adam_phone.yaml)__

This is to notify me to charge my phone when I am at work.  Generally I forget to charge my phone and it is either low or dead for the train ride home.    
* Charge my phone notification at 50 and 30% battery

### Maintenance Reminders.yaml Automations:
__[File Link](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/maintenance_reminders.yaml)__

A series of automations that trigger monthly or weekly to help me remember to perform maintenance tasks around the house.  Reminders are sent via e-mail so they stick in my inbox until complete.  
* Trash Day Reminder
* Furnace Filter Reminder
* Dog Flea/Tick/Heartworm Reminder
* Water Softener Reminder
* Remind me to service our whole home humidifier before winter
* Remind me to service our water filter

### Morning Briefing.yaml Automation:
__[File Link](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/morning_briefing.yaml)__

* Send my Wife and I a morning e-mail with the weather for the day and some other tidbits of information. 

### Notification bulb.yaml Automations
__[File Link](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/notification_bulb.yaml)__

* Set the notification bulb to the color selected using an input select
* Set the notification bulb to a white color that matches the other lamps in the room

### Outside Lights.yaml Automations
__[File Link](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/outside_Lights.yaml)__

Some simple automations to turn my outside house lights on at sunset and off at sunrise.  They are initially set to 10% brightness but are set to full brightness if a door is opened, until it is closed.
* Turn on the outside lights at sunset
* Turn off the outside lights at sunrise
* Open front doors Increase Brightness
* Open back door Increase Brightness

### PC_Security.yaml Automations:
__[File Link](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/pc_security.yaml)__

* Notify me if the Desktop PC is turned on while away
* Notify me if there is a failed login attempt to the HA front end
* Notify me of a new device added to my Wifi network

### Snapshot.yaml Automations:
__[File Link](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/snapshot.yaml)__

Make a full hassio snapshot everynight at 3:00 a.m. and upload a copy to my HomeAssistant gmail account.  I keep 15 days on the gmail account and 3 days locally.

### Thermostat.yaml Automations:
__[File Link](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/thermostat.yaml)__

This set of automations is still in its infancy.  I replaced my nest thermostat with a basic Z-wave unit.  Given the presence detection of home assistant and the ability to control the thermostat, I can replace all the nest functions I used and have less reliance on 'the cloud'.

* Set the thermostat to 'away' temperature when everyone has left for the day. (weekdays only)
* Turn the thermostat back to our 'home' temperature at 4:00 to preheat the house so it is warm when my wife arrives home.
* If anyone comes home, turn the temperature back to the 'home' value.
* At bedtime lower the temperature 2 degrees.
* Pre-heat the house for when we wake up.

### UPS.yaml Automations:
__[File Link](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/ups.yaml)__

* Notify me if there is a power outage
* Notify me when power is restored

### Vacation Mode.yaml Automations:
__[File Link](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/vacation_mode.yaml)__

This is a single switch to turn on/off a number of automations and devices when we will be away from the house for an extended period of time. 
* Turn On Vacation Mode with Vacation Mode Switch
* Turn Off Vacation Mode with Vacation Mode Switch

### Watchdog.yaml Automations:
__[File Link](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/watchdog.yaml)__

I wanted to build a watchdog that would tell me if either of my instances goes down.  I also wanted to be able to see more than if they were connected (ie. not just a ping).  To do this the main instance turns on a MQTT switch and the remote instance turns it off, both are on a one minute cycle.  Both instances monitor the switch and notify me if the state doesn't change after 60 seconds.  

The goal of this is to show that not only are the two instances up and running but they are processing incoming data, running automations and it also shows that my MQTT broker is up and running correctly.  

### Weather.yaml Automations:
__[File Link](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/weather.yaml)__

Notify of severe weather.  I work in one county and live in another so I have an automation for both counties. 
* Notify me of severe weather events
* Update the weather sensors used in the front end everday just after midnight
