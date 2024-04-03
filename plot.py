import virgo
import os
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
files = os.listdir('/home/pi/Desktop/radio_telescope/Observatuion-dats')
for file_name in files:
    print(file_name)
    if file_name.endswith('.dat'):
        new_file_name = os.path.splitext(file_name)[0]
        virgo.plot(obs_parameters=obs, n=20, m=35, f_rest=1420.4057517667e6,
           vlsr=False, meta=False, avg_ylim=(-5,15), cal_ylim=(-20,260), cal_file='calibration.dat',
           obs_file='/home/pi/Desktop/radio_telescope/Observatuion-dats/'+file_name, 
           dB=True, spectra_csv='/home/pi/Desktop/radio_telescope/spectraCSV/'+new_file_name+'.csv', plot_file='/home/pi/Desktop/radio_telescope/plots/'+file_name+'plot.png')
    
print('done')
