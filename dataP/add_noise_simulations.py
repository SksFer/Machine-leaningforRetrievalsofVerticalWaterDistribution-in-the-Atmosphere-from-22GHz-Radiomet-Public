import os
import numpy as np

def noise(tsky, trx=75., snr=200.):
    tsys = trx + tsky
    tnoise = tsys / snr
    tcal = tsky + tnoise * np.random.standard_normal(tsky.shape)
    return tcal

input_folder = '/path/espectros/'
output_folder = '/path/espectros_noise/'

for filename in os.listdir(input_folder):
    if filename.endswith('.txt'):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        data = np.loadtxt(input_path)

        data[:, 1] = noise(data[:, 1])

        np.savetxt(output_path, data, fmt='%f')

    print(f"File {filename} complete.")
