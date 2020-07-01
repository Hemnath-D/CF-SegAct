# CF-SegAct
CF-SegAct separates the accepted Codeforces problem solutions in a given folder(solutions directory) into a destination folder. The filenames of the solutions should start with the problem code. Example filenames: 336C.cpp, 336DTest.cpp, 335 Test.py


1. Clone the repository
2. Install the dependencies using ```pip3 install -r requirements.txt```
3. Edit config.py and set your codeforces handle, solutions directory, destination directory, and the time interval between execution of the script(in seconds).
4. Run the file segact.py
5. Follow the instructions in the following article to autorun the script: https://tecadmin.net/setup-autorun-python-script-using-systemd/
