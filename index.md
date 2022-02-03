## File Manager

A simple file browser powered by [Python](https://www.python.org/downloads/) and [Flask](https://flask.palletsprojects.com/en/2.0.x/) built aiming efficiency + multiplatform support

## Instal Instructions

### Arch Linux

run the commands below, line by line

```bash
sudo pacman -Syyuu --noconfirm
sudo pacman -S git python python-pip --noconfirm
cd ~
git clone https://github.com/hirusha-adi/File-Manager.git
cd File-Manager
pip3 install -r requirements.txt
python3 files.py # to start the file manager
# CTRL + Z
# bg
# disown -h
```
### Ubuntu/Debian

run the commands below, line by line

```bash
sudo apt install && sudo apt upgrade -y
sudo apt install git python3 python3-pip -y
cd ~
git clone https://github.com/hirusha-adi/File-Manager.git
cd File-Manager
pip3 install -r requirements.txt
python3 files.py # to start the file manager
# CTRL + Z
# bg
# disown -h
```

### Windows

1. Download and install Python3. Make sure to 'Add to PATH' when install python3

![image1](https://www.tutorials24x7.com/uploads/2019-12-26/files/3-tutorials24x7-python-windows-install.png)

2. Download the code as a .zip file from this Github Reposotory

![image2](https://cdn.discordapp.com/attachments/935515175073763398/937186561299197952/unknown.png)

(this above image might not be the same)

3. Extract the downloaded `.zip` file
4. open `cmd` in that folder
5. run `pip install -r requirements.txt`
6. run `python server.py` to start the file manager



