# What is it

It's a script which is using `speedtest-cli` to get the Download and Upload speed, saving it into a .json and makes a download and upload plot as .png

### API:

- Root Arg: `-r <Path>`, `--root <Path>` (Required)
    - Uses the defined Path as root directory of a folder to save the data, like the download.png and upload.png plot with the .json as reference point for the next run

### Usage:
- Install all required packages in `requirements.txt` using the `pip install -r requirements.txt` command
- Run the script with `python "/path/to/script.py" --root "/path/to/any/data_storage/folder"`