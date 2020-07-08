
import random

import osc
import ui
import sys
from PyQt5 import QtCore, QtWidgets
from bpm import SignalGenerator, AudioAnalyzer
from recorder import *
from pythonosc import dispatcher
from pythonosc import osc_server
#import oscp



#if __name__ == "__main__":
    # Setup UI
#    app=OscClient("https://aff2dc9bacb2.ngrok.io",7701)
    # window = QtWidgets.QMainWindow()

    # # Start beat tracking
    # beat_detector = BeatDetector(window)

    # # Display window
    # window.show()
    # code = app.exec_()

    # # Clean up
    # beat_detector.close()
    # sys.exit(code)
# from oscpy.client import OSCClient

# osc = OSCClient("https://aff2dc9bacb2.ngrok.io", 7071)
# for i in range(10):
#     osc.send_message(b'/ping', [i])
#def start_osc_server(args, sim, control):
"""Start a background thread running an OSC server listening for messages on an UDP socket."""
def print_handler(address, *args):
    print(f"{address}: {args}")


def default_handler(address, *args):
    print(f"DEFAULT {address}: {args}")

    # Initialize the OSC message dispatch system.
dispatch = dispatcher.Dispatcher()
    # dispatch.map("/sim/*", sim.message)
    # dispatch.map("/control/*", control.message)
dispatch.map("/beat", print_handler)
dispatch.map("/bar/", print_handler)
dispatch.map("/prog{:d}",print_handler)
dispatch.set_default_handler(default_handler)
print('Waiting')
    # Start and run the server.
server = osc_server.ThreadingOSCUDPServer(("localhost", 5005), dispatch)
#server.close()
# server_thread = threading.Thread(target=server.serve_forever)
# server_thread.daemon = True
# server_thread.start()
print("Serving on {}".format(server.server_address))
server.serve_forever()