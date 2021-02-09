# buildozer android logcat debug deploy run
buildozer android debug deploy run

adb pull /storage/emulated/0/kivy/EliasList/AndMyInfoFile.txt /home/Logs/

adb push /usr/src/Python/EliasList/main.py  /storage/emulated/0/kivy/EliasList/

