from gwpy.timeseries import TimeSeries
from gwpy.plot import Plot
from scipy.signal import find_peaks
import numpy as np
import matplotlib.pyplot as plt


print("-------------------------------------------\n")
print("       Hello welocome in Gravitas,\n")
print("  program that looks for gravitation waves")
print("-------------------------------------------\n")




start_time = input("What is the start time:")
end_time = input("What is the end time:")




def fetch_and_plot_data(detector, start_time, end_time, threshold=1e-21):
    data = TimeSeries.fetch_open_data(detector, start_time, end_time, cache=True)
    
    filtered_data = data.bandpass(50, 400)
    
    peaks, _ = find_peaks(filtered_data.value, height=threshold)
    

    plt.figure(figsize=(12, 6))  
    plt.plot(filtered_data.times, filtered_data.value, label='Filtered Data')
    
    plt.plot(filtered_data.times.value[peaks], filtered_data.value[peaks], "x", label='Detected Peaks', color='orange')
    
    plt.title(f'{detector} strain data from {start_time} to {end_time}')
    plt.xlabel('Čas (UTC)')
    plt.ylabel('Amplituda gravitační vlny [strain]')
    plt.grid(True) 
    plt.legend()
    
    plt.show()

start_time = 'September 14, 2015, 09:50:45 UTC'
end_time = 'September 14, 2015, 09:51:05 UTC'
fetch_and_plot_data('L1', start_time, end_time)
