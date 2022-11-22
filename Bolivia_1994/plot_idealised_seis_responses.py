import numpy as np
import matplotlib.pyplot as plt
from load_synth_stn import load_synthetic_station
from copy import  copy

acc, corio, GRAV, PGRAV, sumarr = load_synthetic_station('YUNZ')
time = copy(acc[:,0])



fig, ax = plt.subplots(5, sharex=True)

i=0
for d in [acc, corio, GRAV, PGRAV]:
    ax[i].plot(d[:,0], d[:,1], 'k')
    i+= 1



ax[0].plot(acc[:,0], sum)


# BP Filter:
from wetools import bp_filter
bp_fmin = 0.005
bp_fmax = 0.03

tacc, acc = bp_filter(t=time,d=acc[:,1],fmin=bp_fmin,fmax=bp_fmax)
tsum, sum = bp_filter(t=time,d=sum,fmin=bp_fmin,fmax=bp_fmax)

ax[-1].plot(tacc, acc, 'k')
ax[-1].plot(tsum, sum, 'r')

plt.show()




