import os
import subprocess

# Simple wrapper script for https://github.com/captainzero93/extract-unet-safetensor
# Place this script in a directory for downloading checkpoints and set the options below.
# Running will loop through all .safetensors and run UNetExtractor.py. By default the unet
# and non-unet .safetensors files will be written to .\output\ 

# Directory containing the .safetensors files to extract (will extract any in this directory)
directory = "."
# Output path for unet .safetensors files
unet_output = ".\\output\\"
# Output path for non-unet .safetensors files
non_unet_output = ".\\output\\"
# Path and executable of UNetExtractor.py
extractor = "..\\extract-unet-safetensor\\UNetExtractor.py"
# Valid options for UNetExtractor: flux, sdxl, sd15
model_type = "flux"
# Percentage to limit GPU usage
gpu_limit = "100"
# Automatically delete the input .safetensors file if extractor command completed successfully
auto_delete = False
# Have UNetExtractor output verbose
verbose = False


# Loop through all files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".safetensors"):
        base_filename = os.path.splitext(filename)[0]
        
        command = [
            "python", extractor, filename,
            f"{unet_output}{base_filename}_{model_type}_unet.safetensors",
            f"{non_unet_output}{base_filename}_{model_type}_non_unet.safetensors",
            "--model_type", model_type, "--gpu_limit", gpu_limit
        ]
        
        if verbose:
            command.append("--verbose")
        
        # Run
        result = subprocess.run(command)
        
        if auto_delete and result.returncode == 0:
            os.remove(filename)
            print(f"\nAutomatically deleted {directory}{filename} after successful run.\n")
