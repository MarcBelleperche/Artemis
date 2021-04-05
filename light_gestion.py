# I am using yeelight for my self but you have other provider with other librairies
import yeelight

#def store_lights_values:

#def get_lights_values:

def light_command(ipbulb):
    bulb = yeelight.Bulb(ipbulb)
    bulb.toggle()