import numpy as np
import os
import sys

input_dir = "/path/atributes/"
output_dir = "/path/amc/"

input_files = [f for f in os.listdir(input_dir) if f.endswith('.txt')]

rows = 20 #capas

for file_idx, input_file in enumerate(input_files, start=1):
    input_file_path = os.path.join(input_dir, input_file)
    am_data = np.loadtxt(input_file_path, delimiter=', ')

    pressure = am_data[:,0]
    h2o = am_data[:,1]
    temp = am_data[:,2]

    num_spectra = len(am_data) // rows
    for i in range(num_spectra):
        start_idx = i * rows
        end_idx = start_idx + rows

        pressure_chunk = pressure[start_idx:end_idx]
        h2o_chunk = h2o[start_idx:end_idx]
        temp_chunk = temp[start_idx:end_idx]

        output_file = os.path.join(output_dir, f"{file_idx}.amc")
        print(f"Creating file: {file_idx} of {len(input_files)}")

        with open(output_file, 'w') as f:
            original_stdout = sys.stdout
            sys.stdout = f

            try:
                print("?")
                print("? Usage:")
                print("?   am this_file f_min f_max df zenith_angle trop_h2o_scale_factor")
                print("? Example:")
                print("?   am this_file 20 GHz  26 GHz  60 KHz  0 deg  1.0")
                print("?")
                print("f %1 %2  %3 %4 %5 %6")
                print("output f GHz  Tb K Trj K")
                print("za %7 %8")
                print("tol 1e-4")
                print("")
                print("Nscale troposphere h2o %9")
                print("")
                print("T0 2.7 K")

                layer0 = 0
                layer_transition1 = 2
                layer_transition2 = 6
                layers = 20
                step = 1

                position0 = np.arange(layer0, layer_transition1, step)

                for n in position0:
                    print('')
                    print('layer mesosphere')
                    print('Pbase {:.10e} mbar'.format(pressure_chunk[n]))
                    print('Tbase {:.10e} K'.format(temp_chunk[n]))
                    print('column dry_air vmr')
                    print('column h2o vmr {:.10e}'.format(h2o_chunk[n]))

                position1 = np.arange(layer_transition1, layer_transition2, step)

                for n in position1:
                    print('')
                    print('layer stratosphere')
                    print('Pbase {:.10e} mbar'.format(pressure_chunk[n]))
                    print('Tbase {:.10e} K'.format(temp_chunk[n]))
                    print('lineshape Voigt-Kielkopf')
                    print('column dry_air vmr')
                    print('column h2o vmr {:.10e}'.format(h2o_chunk[n]))

                position2 = np.arange(layer_transition2, layers, step)

                for n in position2:
                    print('')
                    print('layer troposphere')
                    print('Pbase {:.10e} mbar'.format(pressure_chunk[n]))
                    print('Tbase {:.10e} K'.format(temp_chunk[n]))
                    print('column dry_air vmr')
                    print('column h2o vmr {:.10e}'.format(h2o_chunk[n]))
            finally:
                sys.stdout = original_stdout

print("Processing complete.")
