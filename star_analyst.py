#%%
from lightkurve import TessTargetPixelFile
import lightkurve as lk
import numpy as np

#insert file destination from where the .tp file is stored
tpf = TessTargetPixelFile(r'')
tpf.plot(frame=42)

lc = tpf.to_lightcurve(aperture_mask=tpf.pipeline_mask)
lc.plot()

flat_lc = lc.flatten()
flat_lc.plot()

period = np.linspace(1, 5, 10000)
bls = lc.to_periodogram(method='bls', period=period, frequency_factor=500)
bls.plot()

planet_x_period = bls.period_at_max_power
planet_x_t0 = bls.transit_time_at_max_power
planet_x_dur = bls.duration_at_max_power

ax = lc.fold(period=planet_x_period, epoch_time=planet_x_t0).scatter()
ax.set_xlim(-1.5, 1.5)
# %%
