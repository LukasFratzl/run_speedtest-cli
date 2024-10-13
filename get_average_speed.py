import speedtest
import json
import os
from pathlib import Path
from sys import argv
import matplotlib.pyplot as plt

ROOT_ARG_SYN = ['-r', '--root']

ROOT_DIR = '/No/Valid/Path/'
JSON_DOWNLOAD_NAME = 'Downloads'
JSON_UPLOAD_NAME = 'Uploads'


def normalize_path(path_str):
    path_str = os.path.normpath(path_str)
    path_str = os.path.normcase(path_str)
    return path_str

if __name__ == '__main__':
    args = argv[1:]
    if len(args) % 2 == 1:
        print('You called an arg but miss the value .. ')
    for argi in range(len(args)):
        # Needs to be just every periodic arg to check
        if argi % 2 == 0:
            arg_lower = args[argi].lower()
            for arg in ROOT_ARG_SYN:
                if arg_lower == arg:
                    path = args[argi + 1].replace('\'', '').replace('"', '')
                    if os.path.isdir(path):
                        ROOT_DIR = path

    ROOT_DIR = normalize_path(ROOT_DIR)

    print('Using root dir ->', ROOT_DIR)

    if not os.path.isdir(ROOT_DIR):
        print('No Valid Root Directory ... Please check your root path argument..., sometimes you may need to add "" or \'\' like "/Path/"')
        err = 'err'
        int(err)

    data_file_path = normalize_path(Path.joinpath(Path(ROOT_DIR), 'internet_speed_history.json'))

    if Path(data_file_path).is_file():
        with open(data_file_path, 'r') as f:
            data = json.load(f)
    else:
        data = {JSON_DOWNLOAD_NAME: [], JSON_UPLOAD_NAME: []}

    st = speedtest.Speedtest()

    download = st.download()
    download_MBits = download / 1024.0 / 1024.0
    print('Download Speed:', download_MBits, 'MBits')

    upload = st.upload()
    upload_MBits = upload / 1024.0 / 1024.0
    print('Upload Speed:', upload_MBits, 'MBits')

    if JSON_DOWNLOAD_NAME not in data:
        data[JSON_DOWNLOAD_NAME] = [download_MBits]
    else:
        data[JSON_DOWNLOAD_NAME].append(download_MBits)

    if JSON_UPLOAD_NAME not in data:
        data[JSON_UPLOAD_NAME] = [upload_MBits]
    else:
        data[JSON_UPLOAD_NAME].append(upload_MBits)

    with open(data_file_path, 'w') as f:
        json.dump(data, f)

    download_plot_file_path = normalize_path(Path.joinpath(Path(ROOT_DIR), 'download_history.png'))
    plt.style.use('dark_background')
    plt.plot(data[JSON_DOWNLOAD_NAME])
    plt.savefig(download_plot_file_path)
    plt.close()

    upload_plot_file_path = normalize_path(Path.joinpath(Path(ROOT_DIR), 'upload_history.png'))
    plt.style.use('dark_background')
    plt.plot(data[JSON_UPLOAD_NAME])
    plt.savefig(upload_plot_file_path)
    plt.close()