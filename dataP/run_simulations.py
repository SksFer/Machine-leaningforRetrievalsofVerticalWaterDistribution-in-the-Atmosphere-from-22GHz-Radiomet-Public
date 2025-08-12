import os
import subprocess

input_directory = "/path/amc/"
output_directory = "/path/espectros/"

os.makedirs(output_directory, exist_ok=True)

amc_files = [f for f in os.listdir(input_directory) if f.endswith('.amc')]

for amc_file in amc_files:
    amc_file_path = os.path.join(input_directory, amc_file)

    output_file_path = os.path.join(output_directory, os.path.splitext(amc_file)[0] + '.txt')

    command = f"am {amc_file_path} 20 GHz 26 GHz 0.5 MHz 0 deg 0.9 >> {output_file_path}"

    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Successfully processed {amc_file}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to process {amc_file}: {e}")
