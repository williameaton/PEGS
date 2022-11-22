from obspy.clients.fdsn.client import Client
from obspy.core import UTCDateTime

# Create a Client:
client = Client("IRIS")
starttime = UTCDateTime("1994-06-9")
endtime = UTCDateTime("1994-06-10")
inventory = client.get_stations(network="IU",
                                station="ANMO",
                                channel="BH?",
                                starttime=starttime,
                                endtime=endtime,
                                format='xml')

inventory.write("NNA", format="STATIONXML")