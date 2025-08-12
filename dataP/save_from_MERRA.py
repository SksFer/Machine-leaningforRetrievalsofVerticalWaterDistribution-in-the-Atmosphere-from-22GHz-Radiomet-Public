import numpy as np
import xarray as xr

file_path = '/path/MERRA2_dec.nc'
ds = xr.open_dataset(file_path)

layers = range(5,72) #67
time_indices = range(0,1)
lat_indices = range(35,326,2) # 146 tot
lon_indices = range(0,576,4) #144 tot

with open('output.txt', 'w') as file:
    for time_index in time_indices:
        for lat_index in lat_indices:
            for lon_index in lon_indices:
                for layer in layers:
                    pl_value = ds.PL.isel(time=time_index, lev=layer, lat=lat_index, lon=lon_index).values/100
                    qv_value = ds.QV.isel(time=time_index, lev=layer, lat=lat_index, lon=lon_index).values
                    t_value   = ds.T.isel(time=time_index, lev=layer, lat=lat_index, lon=lon_index).values
                    delp_value = ds.DELP.isel(time=time_index, lev=layer, lat=lat_index, lon=lon_index).values/100

                    #QV a H2O
                    qv_value = (qv_value)/(1.0 - qv_value)
                    h2o_value = (28.964/18.015)*qv_value

                    #Interpolacion PL
                    pl_value = pl_value + 0.5*delp_value

                    #Interpolacion temperatura
                    t_value = (t_value[:-1] + t_value[1:]) / 2
                    t_value = np.append(t_value, t_value[-1])


                    file.write(f"{pl_value}, {h2o_value}, {t_value}, {delp_value}\n")

                    print(f"{pl_value} [mbar], {h2o_value} [vmr], {t_value} [K], {delp_value} [mbar]")
