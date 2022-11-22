import numpy as np
import obspy
from obspy.core.stream import Stream
from obspy.core.inventory import read_inventory
import matplotlib.pyplot as plt
from copy import copy
from wetools import obspy_gen_mpl, gauss_STF_convolve, normalise, gen_gaussian,pad_by_time, bp_filter, STF_convolve, normalise_by_area, bp_filter_ty
from load_synth_stn import load_synthetic_station
# TO DO:
#  - Prefilter the real data before removing the signal response
#  - Bandpass filter the synthetic data

# Major issues:
#  - Amplitudes off by a factor of 10  -- what amplitude do I use for the STF?
#  - Currently only plotting the acceleration for the synthetics - need real receiver response (inc grav, rotation etc)










