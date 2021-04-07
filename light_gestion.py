# I am using yeelight for my self but you have other provider with other librairies
import yeelight
from yeelight import *
from yeelight import discover_bulbs
import Artemis.artemis_voice as av
import Artemis.file_gestion as fg

table = "Lights"
transitions = [
    RGBTransition(255, 0, 255, duration=2000)
]

flow = Flow(
    count=1,  # 1.
    transitions=transitions
)
#def store_lights_values:

#def get_lights_values:


def identify_bulbs():
    bulbs = discover_bulbs()
    for b in bulbs:
        bulb = Bulb(b['ip'])
        bulb.start_flow(flow)
        light_name = av.ask_for("Quel est le nom de l'ampoule qui vient de varier de couleur ?")
        fg.write_json(table, "name", light_name)
        fg.write_json_details(table, light_name, "ip", bulb['ip'])


def light_command(ipbulb):
    bulb = yeelight.Bulb(ipbulb)
    bulb.toggle()


def light_on(ipbulb):
    bulb = yeelight.Bulb(ipbulb)
    bulb.turn_on()


def light_off(ipbulb):
    bulb = yeelight.Bulb(ipbulb)
    bulb.turn_off()
