from math import log
import webbrowser, sys, pyperclip, logging

logging.basicConfig(filename='mapit.log',level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.DEBUG)

sys.argv

logging.debug("Start of Program")

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()
    logging

logging.debug("Address set to %s" %(address))

webbrowser.open('https://www.google.com/maps/search/' + address)