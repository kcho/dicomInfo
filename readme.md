#dicomInfo.py

usage: dicomInfo.py [-h] [-dir DIRECTORY] [-n] [-i] [-s] [-b] [-d] [-a]

dicomInfo.py : Returns information extracted from dicom within the directory
====================
eg) dicomInfo.py
eg) dicomInfo.py --dir /Users/kevin/NOR04_CKI

optional arguments:
    -h, --help            show this help message and exit
    -dir DIRECTORY, --directory DIRECTORY
                        Data directory location, default = pwd

    -n, --name            Get patient name
    -i, --id              Get patient ID
    -s, --sex             Get patient sex
    -b, --dob             Get patient DOB
    -d, --date            Get scan date
    -a, --all             Print all information

