# Wanted to use it but tinytuya require an internet connexion plus id's and bla bla bla ...
# I put it on side for the moment

import tinytuya as tiny
import Artemis.file_gestion as fg

table = "Switches"


def find_switches():
    print(tiny.deviceScan())


def store_switch_init():
    fg.write_json(table, "name", "fontaine")
    fg.write_json_details(table, "fontaine", "ip", "192.168.0.12")


def turn_on(name):
    ip = fg.ip_address(table, name)
    device_ip = tiny.BulbDevice(ip)
    device_ip.turn_on()


def turn_off(name):
    ip = fg.ip_address(table, name)
    device_ip = tiny.BulbDevice(dev_id="180062414c11ae14f7f9", address=ip)
    device_ip.turn_off()
