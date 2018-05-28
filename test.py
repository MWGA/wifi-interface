import constants
from scapy.all import *
import utils
from socket import *

# s = socket(AF_PACKET, SOCK_RAW)
# s.bind((constants.DEVICE_NAME, 0))
# s.listen(1)

rates_header = Dot11Elt(ID="Rates", info=constants.RATES)

assoc_response_packet = RadioTap(len=18, present='Flags+Rate+Channel+dBm_AntSignal+Antenna',
                                 notdecoded='\x00\x6c' + struct.pack("<h", 2457) + '\xc0\x00\xc0\x01\x00\x00') \
                        / Dot11(subtype=0x01, addr2=constants.BEACON_ADDR2, addr3=constants.BEACON_ADDR2, addr1=constants.BEACON_ADDR2) \
                        / Dot11AssoResp(status=0, AID=utils.next_aid(10)) \
                        / rates_header

#s.send( bytes_hex(assoc_response_packet.original) )
sendp(assoc_response_packet, iface=constants.DEVICE_NAME, verbose=3, retry=0)