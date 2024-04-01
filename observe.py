import virgo
import datetime
from time import sleep
# Define observation parameters
obs = {
    'dev_args': 'rtl,bias=1',
    'rf_gain': 30,
    'if_gain': 25,
    'bb_gain': 18,
    'frequency': 1420e6,
    'bandwidth': 2.4e6,
    'channels': 2048,
    't_sample': 1,
    'duration': 240,
    'loc': '',
    'ra_dec': '',
    'az_alt': ''
}

while(True):
        
        currentDT = datetime.datetime.now()
        obsDT = currentDT.strftime("%Y-%m-%d %H:%M:%S")
        obsDTfile = currentDT.strftime("%Y%m%d%H%M%S")
# Begin data acquisition
        virgo.observe(obs_parameters=obs, obs_file='/home/pi/Desktop/radio_telescope/Observatuion-dats/'+str(obsDTfile)+'.dat')
        sleep(600)


