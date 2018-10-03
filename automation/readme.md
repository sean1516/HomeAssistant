### Bedtime_Notifications.yaml Automations:
These notifications are triggered after 10:00 PM and I plug my phone in (generally I am in bed when this happens).  These send an iOS app notification with an action option to turn the device off.  These are primarily a power saving items.
* __[Notify Me if the garage door is open and I am in bed ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/bedtime_notifications.yaml#L1)__
* __[Notify Me if the Home Theater PC is left on and I am in bed ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/bedtime_notifications.yaml#L26)__
* __[Notify Me if the Desktop PC is left on and I am in bed ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/bedtime_notifications.yaml#L65)__
* __[Notify Me if the Living Room Lamps are left on and I am in bed ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/bedtime_notifications.yaml#L103)__

<p align="center"> <img src="https://github.com/SilvrrGIT/HomeAssistant/blob/master/ScreenShots/iosnotification.jpg"><img src="https://github.com/SilvrrGIT/HomeAssistant/blob/master/ScreenShots/ios%20action.jpg">
</p>

### Cert Update.yaml Automation:	
This notification is used to notify me if my Lets Encrypt certificate does not auto renew at the beginning of the month.  	
* __[Notify Me if Lets Encrypt Cert Did Not Update ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/certupdate.yaml)__

### Device Offline.yaml Automations:
This notification is used to notify me if on of my home automation devices goes offline.  Generally this is someone flipping a switch which cuts the power or a network connectivity issue.
* __[Notify Me if a Home Automation Device is offline ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/deviceoffline.yaml)__
* __[Notify Me if a Yeelight is offline ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/deviceoffline.yaml#L28)__

### Door Security.yaml Automations:
These automations are used to notify me when a door is opened when no one is home or the garage door is left open when we leave.
* __[Notify Me if the interior garage door is opened and I am away ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/door_security.yaml#L2)__
* __[Notify Me if the exterior garage door is opened and I am away ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/door_security.yaml#L33)__
* __[Notify Me if the front door is opened and I am away ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/door_security.yaml#L58)__
* __[Notify Me if the back door is opened and I am away ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/door_security.yaml#L115)__
* __[Notify Me if the garage door is left open when I leave ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/door_security.yaml#L83)__

### Downloader.yaml Automations:
* __[Notify Me if a downloader download fails ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/downloader.yaml#L1)__
* __[Notify Me if a downloader download completes ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/downloader.yaml#L17)__

### Feed the dog.yaml Automations:
These automations are used to turn a light on to signify the dog needs to be fed.  A amazon dash button is used to signify the dog has been fed which either turns off the notification light or turn off the automation. 
* __[Turn on Notification Light AM ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/feed_the_dog.yaml#L1)__
* __[Turn on Notification Light PM ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/feed_the_dog.yaml#L18)__

### Garage Light.yaml Automations:
Simple automations to turn on a light when the interior garage door opens.  If the light is left on for 5 mintues it automatically turns off. 
* __[Interior Garage Door Open Light On ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/garage_light.yaml#L7)__
* __[Turn Off Garage Light After 5 Minutes](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/garage_light.yaml#L19)__

### Leaving_Notifications.yaml Automations:
These notifications are triggered when I leave my home zone and no one is home.  These send a iOS app notification with an action option to turn the device off. These are primarily a power saving item and are the same framework as the bedtime notification as above. 
* __[Notify Me if the Home Theater PC is left on and no one is home ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/leaving_notifications.yaml#L1)__
* __[Notify Me if the Desktop PC is left on and no one is home ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/leaving_notifications.yaml#L47)__
* __[Notify Me if the Living Room Lamps are left on and no one is home ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/leaving_notifications.yaml#L92)__
* __[Notify Me if the Media Center is left on and no one is home ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/leaving_notifications.yaml#L145)__  This is an effort to automate my 'dumb'TV and amplifier based on power usage.  Knowing the power being drawing I can assume which device is left on as they have unique power usage. 

### Living Room Lamps.yaml Automations:
These lamps are the main light source when you walk in through the garage (our primary point of entry).  
* __[Turn on the living room lamps at sunset ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/living_room_lamps.yaml#L1)__
* __[Turn on the living room lamps when somone comes home and its dark out ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/living_room_lamps.yaml#L16)__
* __[Turn off the living room lamps at midnight ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/living_room_lamps.yaml#L39)__

### Low_Battery_Adams_iPhone.yaml Automations:
This is to notify me to charge my phone when I am at work.  Generally I forget to charge my phone and it is either low or dead for the train ride home.    
* __[Charge my phone notification at 50 and 30% battery ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/low_battery_adam_phone.yaml)__

### Maintenance Reminders.yaml Automations:
A series of automations that trigger monthly or weekly to help me remember to perform maintenance tasks around the house.  Reminders are sent via e-mail so they stick in my inbox until complete.  
* __[Trash Day Reminder ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/maintenance_reminders.yaml#L1)__
* __[Furnace Filter Reminder ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/maintenance_reminders.yaml#L21)__
* __[Dog Flea/Tick/Heartworm Reminder](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/maintenance_reminders.yaml#L37)__
* __[Water Softener Reminder ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/maintenance_reminders.yaml#L53)__

### Media Center.yaml Automation:
* __[Turn on TV and Amplifier when HTPC turns on](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/media_center.yaml#L1)__

### Nest.yaml Automations:
I found it easier to automate my nest myself rather than using the nest features.  
* __[Set Thermostat to Away when everyone leaves for work ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/nest.yaml#L1)__
* __[Turn off Away mode at 4:00 PM (pre heat/cool the house before arriving home) ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/nest.yaml#L48)__
* __[Turn off Away mode if someone arrives home ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/nest.yaml#L76)__
* __[If HVAC fan hasn't run for an hour, run it for 10 minutes ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/nest.yaml#L102)__

### Notification bulb.yaml Automations
* __[Set the notification bulb to the color selected ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/notification_bulb.yaml#L1)__
* __[Set the notification bulb to a white color that matches the other lamps in the room ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/notification_bulb.yaml#L21)__

### Outside Lights.yaml Automations
Some simple automations to turn my outside house lights on at sunset and off at sunrise.  They are initially set to 20% brightness but are set to full brightness if a door is opened, until it is closed.
* __[Turn on the outside lights at sunset ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/outside_Lights.yaml#L1)__
* __[Turn off the outside lights at sunrise ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/outside_Lights.yaml#L18)__
* __[Open front doors Increase Brightness ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/outside_Lights.yaml#L36)__
* __[Open back door Increase Brightness ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/outside_Lights.yaml#L71)__

### PC_Security.yaml Automations:
* __[Notify me if the Desktop PC is turned on while away ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/pc_security.yaml#L1)__
* __[Notify me if there is a failed login attempt to the HA front end ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/pc_security.yaml#L23)__
* __[Notify me if there is a sucessful login attempt to the HA front end ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/pc_security.yaml#L41)__
* __[Notify me of a new device added to my Wifi network ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/pc_security.yaml#L64)__

### UPS.yaml Automations:
* __[Notify me if there is a power outage ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/ups.yaml#L1)__
* __[Notify me when power is restored ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/ups.yaml#L30)__

### Vacation Mode.yaml Automations:
This is a single switch to turn on/off a number of automations and devices when we will be away from the house for an extended period of time. 
* __[Turn On Vacation Mode with Vacation Mode Switch ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/vacation_mode.yaml#L1)__
* __[Turn Off Vacation Mode with Vacation Mode Switch  ](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/vacation_mode.yaml#L43)__
