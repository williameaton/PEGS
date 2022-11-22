import numpy as np
import matplotlib.pyplot as plt
from cmt import CMTSource



# Load SCARDEC STFs:
avg = np.loadtxt(fname="./STFs/scardec_avg", skiprows=2)
optimal = np.loadtxt(fname="./STFs/scardec_opt", skiprows=2)

# GCMT:
cmt = CMTSource.from_CMTSOLUTION_file("./STFs/BOLIVIA_GCMT")
time = np.linspace(-10, 80, 1000)
alpha = 1.628

# use 1e-7 to convert from dyne-cm to Nm
M0_cmt = cmt.M0*1e-7
gcmt =  M0_cmt * alpha/((np.pi**0.5) * cmt.half_duration) * np.exp(- (alpha*(time-cmt.time_shift)/cmt.half_duration)**2)



M0_opt = np.trapz(y=optimal[:,1], x=optimal[:,0])
M0_avg = np.trapz(y=avg[:,1], x=avg[:,0])


# Plot STF:
fig, ax = plt.subplots()
fs = 16
ax.plot(optimal[:,0], optimal[:,1])
ax.plot(avg[:,0], avg[:,1])
ax.plot(time, gcmt)


ax.legend(['SCARDEC Opt.', 'SCARDEC Avg.', 'SPECFEM GCMT'])
ax.set_xlabel('Time [s]', fontsize=fs)
ax.set_ylabel('Moment rate [Nm/s]', fontsize=fs)

text_str = ""
names = ["M0_cmt", "M0_opt", "M0_avg"]
MOs = [M0_cmt, M0_opt, M0_avg]
for i in range(3):
    text_str += f"{names[i]}: {np.format_float_scientific(MOs[i], precision=2,exp_digits=2)}"
    if i < 2:
        text_str += "\n"
ax.text(55, 1e20,text_str, bbox={'facecolor':'w','pad':5})


plt.savefig(fname="./STFs/STF.png", dpi='figure', format='png')
plt.show()