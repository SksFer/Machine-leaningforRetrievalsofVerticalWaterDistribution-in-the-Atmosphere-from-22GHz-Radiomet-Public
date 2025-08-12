import numpy as np
import os
import sys


data = np.genfromtxt("data.txt", delimiter=',')
pres = data[:,0]
h2o = data[:,1]
temp = data[:,2]

output = "/path/atributes/"

rows = 67
tot = len(pres) // rows

for i in range(tot):
    start_idx = i * rows
    end_idx = start_idx + rows

    pres_chunk = pres[start_idx:end_idx]
    h2o_chunk = h2o[start_idx:end_idx]
    temp_chunk = temp[start_idx:end_idx]

    output_file = os.path.join(output, f"{i+1}.txt")
    print(f"creating file {i+1} of {tot}")

    with open(output_file, 'w') as f:
        original_stdout = sys.stdout
        sys.stdout = f
        try:
            for n in np.arange(1,2):
                print('{:.10e}, {:.10e}, {:.10e}'.format(pres_chunk[n], h2o_chunk[n], temp_chunk[n]))
            for n in np.arange(6,7):
                print('{:.10e}, {:.10e}, {:.10e}'.format(pres_chunk[n], h2o_chunk[n], temp_chunk[n]))
            for n in np.arange(12,13):
                print('{:.10e}, {:.10e}, {:.10e}'.format(pres_chunk[n], h2o_chunk[n], temp_chunk[n]))
            for n in np.arange(20,21):
                print('{:.10e}, {:.10e}, {:.10e}'.format(pres_chunk[n], h2o_chunk[n], temp_chunk[n]))
            for n in np.arange(26,27):
                print('{:.10e}, {:.10e}, {:.10e}'.format(pres_chunk[n], h2o_chunk[n], temp_chunk[n]))
            for n in np.arange(31,32):
                print('{:.10e}, {:.10e}, {:.10e}'.format(pres_chunk[n], h2o_chunk[n], temp_chunk[n]))
            for n in np.arange(33,34):
                print('{:.10e}, {:.10e}, {:.10e}'.format(pres_chunk[n], h2o_chunk[n], temp_chunk[n]))
            for n in np.arange(37,38):
                print('{:.10e}, {:.10e}, {:.10e}'.format(pres_chunk[n], h2o_chunk[n], temp_chunk[n]))
            for n in np.arange(39,40):
                print('{:.10e}, {:.10e}, {:.10e}'.format(pres_chunk[n], h2o_chunk[n], temp_chunk[n]))
            for n in np.arange(41,42):
                print('{:.10e}, {:.10e}, {:.10e}'.format(pres_chunk[n], h2o_chunk[n], temp_chunk[n]))
            for n in np.arange(43,44):
                print('{:.10e}, {:.10e}, {:.10e}'.format(pres_chunk[n], h2o_chunk[n], temp_chunk[n]))
            for n in np.arange(45,46):
                print('{:.10e}, {:.10e}, {:.10e}'.format(pres_chunk[n], h2o_chunk[n], temp_chunk[n]))
            for n in np.arange(47,48):
                print('{:.10e}, {:.10e}, {:.10e}'.format(pres_chunk[n], h2o_chunk[n], temp_chunk[n]))
            for n in np.arange(49,50):
                print('{:.10e}, {:.10e}, {:.10e}'.format(pres_chunk[n], h2o_chunk[n], temp_chunk[n]))
            for n in np.arange(51,52):
                print('{:.10e}, {:.10e}, {:.10e}'.format(pres_chunk[n], h2o_chunk[n], temp_chunk[n]))
            for n in np.arange(53,54):
                print('{:.10e}, {:.10e}, {:.10e}'.format(pres_chunk[n], h2o_chunk[n], temp_chunk[n]))
            for n in np.arange(55,56):
                print('{:.10e}, {:.10e}, {:.10e}'.format(pres_chunk[n], h2o_chunk[n], temp_chunk[n]))
            for n in np.arange(59,60):
                print('{:.10e}, {:.10e}, {:.10e}'.format(pres_chunk[n], h2o_chunk[n], temp_chunk[n]))
            for n in np.arange(62,63):
                print('{:.10e}, {:.10e}, {:.10e}'.format(pres_chunk[n], h2o_chunk[n], temp_chunk[n]))
            for n in np.arange(64,65):
                print('{:.10e}, {:.10e}, {:.10e}'.format(pres_chunk[n], h2o_chunk[n], temp_chunk[n]))
        finally:
            sys.stdout = original_stdout

print("Process finalized")
