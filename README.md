# checkpoint-extract-flux

A Simple wrapper script to use with [extract-unet-flux](https://github.com/captainzero93/extract-unet-safetensor).

By default just place this script in a directory where you download checkpoints.
Run this script with `python.exe extract-flux.py`. The script will loop through
the directory and begin extracting any .safetensors files with UNetExtractor.py

## Settings

Edit the script and modify the global variables to your preferences.

```
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
```

Be aware that if `auto_delete` is set to *False*, the next time it is run it will extract that checkpoint again. 
If on a Unix-like system, be sure to change the paths to forward slashes **/**. On Windows use **\\**
since an escape sequence is required for a literal backslash.  