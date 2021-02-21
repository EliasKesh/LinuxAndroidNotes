# buildozer android logcat debug deploy run
buildozer android debug deploy run


adb push ./main.py  /storage/emulated/0/kivy/EliasList/

adb shell rm /storage/emulated/0/AndMyInfoFile.txt

adb pull /storage/emulated/0/kivy/EliasList/AndMyInfoFile.txt /home/Logs/

adb pull /storage/emulated/0/AndMyInfoFile.txt /home/Logs/
