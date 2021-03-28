from struct import unpack
from datetime import timedelta
# from ..PayloadParserBase import PayloadParserBase
# from stuff import *

# class PayloadParser(PayloadParserBase):
class PayloadParser():
    """
    Simple python class to parse the payloads of the iaq-sensor and forwards
    them to the Miromico InfluxDB instance.
    """

    modes = {
        0: "Custom mode",
        1: "Fast",
        2: "Medium",
        3: "BatterySaving",
    }

    types = {
        "msgTypeNoVoc": {"num": 1, "length": 11}
    }

    def __init__(self, config):
        super(PayloadParser, self).__init__(config)
        self._msg = {}
        self._tags = {}
        self._switcher = {
            PayloadParser.types["msgTypeNoVoc"]["num"]: self.parse_four_sensors
        }

    def test_type_mode(self, data):
        types = [type["num"] for key, type in PayloadParser.types.items()]
        try:
            if not data[0] in types:
                print("Unknown message type")
                return False
            if not data[1] in PayloadParser.modes.keys():
                print("Unknown mode")
                return False
            return True
        except:
            return False

    def parse_four_sensors(self, data):
        self._tags["Mode"] = data[1]
        self._tags["ModeString"] = PayloadParser.modes[data[1]]
        self._msg["CO2"] = (data[2] << 8) + data[3] # in ppm
        self._msg["Pressure"] = (data[4] << 16) + (data[5] << 8) + data[6] # in Pa
        self._msg["Temperature"] = int((data[7] << 8) + data[8])/100 # in °C
        self._msg["Humidity"] = int((data[9] << 8) + data[10])/100 # in %
        # self._msg["VOC"] = int((data[10] << 8) + data[12])/100 # in %
        pp(self._msg)
        pp(self._tags)
        
    def parse_payload(self, dev_eui, data, time, port=None):
        super().parse_payload(dev_eui, data, time, port)
        if self.test_type_mode(data):
            self._switcher[data[0]](data)
            self._add_dataline('data', self._msg, tags=self._tags)
            pp(self._msg)
            pp(self._tags)

v = {'cmd': 'gw', 'seqno': 373087, 'EUI': '10CE45FFFE005848', 'ts': 1616521547224, 'fcnt': 5249, 'port': 15, 'freq': 868100000, 'toa': 61, 'dr': 'SF7 BW125 4/5', 'ack': False, 'gws': [{'rssi': -52, 'snr': 10, 'ts': 1616521547224, 'time': '2021-03-23T17:45:47.217371Z', 'gweui': '9C65F9FFFF386789', 'ant': 0, 'lat': 47.3772429, 'lon': 8.531449499999999}], 'bat': 254, 'data': '0101034d017d4c093b0a56'}
pp([v['EUI'], v['data'],v['ts'], v['port']])
import struct
c = {}
print('hexarray ist: ')
# print(hexArray)
b = bytearray.fromhex(v['data'])
pp(b)

# [c['distance'],c['battery'],c['voltage'], c['new']] = struct.unpack('16f', b)
P = PayloadParser
# P.__init__()
data = b
c["Mode"] = data[1]
c["ModeString"] = PayloadParser.modes[data[1]]
c["CO2"] = (data[2] << 8) + data[3] # in ppm
c["Pressure"] = (data[4] << 16) + (data[5] << 8) + data[6] # in Pa
c["Temperature"] = int((data[7] << 8) + data[8])/100 # in °C
c["Humidity"] = int((data[9] << 8) + data[10])/100 # in %
c["VOC"] = int((data[10] << 8) + data[12])/100 # in %
pp(c)
pp(c)

# PayloadParser(v)
