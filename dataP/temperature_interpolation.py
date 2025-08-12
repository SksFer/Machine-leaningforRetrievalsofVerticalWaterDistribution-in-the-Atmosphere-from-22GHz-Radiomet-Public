import numpy as np

file_path = "/path/output_merra.txt"

data = np.loadtxt(file_path, delimiter=',')
PL = data[:, 0]
QV = data[:, 1]
T = data[:, 2]
DELP = data[:, 3]

PL_borders = PL

T_borders = (T[:-1] + T[1:]) / 2
T_borders = np.append(T_borders, T[-1])

QV_values = QV


output_file_path = "/path/output.txt"
with open(output_file_path, 'w') as f:
    #f.write("PL_borders,QV_values,T_borders,levels\n")
    for i in range(len(PL)):
        f.write(f"{PL_borders[i]},{QV_values[i]},{T_borders[i]}\n")
        print(f"Row {i+1} of {len(PL)}")

print(f"Saved {output_file_path}")
