import numpy as np
networks = {'LPAZ': 'GT',
           'NNA' : 'II',
           'YUNZ': 'XE'
          }


def load_synthetic_station(syn_dir, station, channel = 'Z'):
    # Load the synthetics:
    network = networks[station]
    stn_str = f'{syn_dir}/{station}.{network}'

    acc = np.loadtxt(f"{stn_str}.MX{channel}A.sem.ascii")
    corio = np.loadtxt(f"{stn_str}.MX{channel}C.CORIO.sem.ascii")
    GRAV = np.loadtxt(f"{stn_str}.MX{channel}C.GRAV.sem.ascii")
    PGRAV = np.loadtxt(f"{stn_str}.MX{channel}C.PGRAV.sem.ascii")

    sum_arr = acc[:,1] + 2*corio[:,1] + GRAV[:,1] + PGRAV[:,1]

    return acc, corio, GRAV, PGRAV, sum_arr
