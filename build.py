import commands

import os

import time

import shutil

import sys


BUILD_DIR = {"admin-dpc", "mclient", "pilauncher"}
GAME = "piball"

try :
	TAG = sys.argv[1]
except :
	TAG = "common"

build_type = "debug"


for dir in BUILD_DIR :
	print "+"*50
	print "build", dir
	print commands.getoutput("cd " + dir + " ; " + "gradle assembleDebug")
	print "-"*50


print commands.getoutput("cd "+GAME+" ; ./gradlew android:assembleDebug")


BUILD_ARCHIVE = "build_archive"
if not os.path.exists(BUILD_ARCHIVE):
	os.mkdir(BUILD_ARCHIVE)

PATH_CURRENT_TIME_DIR = BUILD_ARCHIVE + "/" + time.strftime("%Y%m%d-%H%M%S-" + TAG)

os.mkdir(PATH_CURRENT_TIME_DIR)

for dir in BUILD_DIR :
	print commands.getoutput("cp -v " + dir + "/app/build/outputs/apk/{0}/*{1}.apk ".format(build_type, build_type) + PATH_CURRENT_TIME_DIR + "/" + dir + ".apk")

print commands.getoutput("cp -v "+ GAME + "/android/build/outputs/apk/android-{0}.apk ".format(build_type) + PATH_CURRENT_TIME_DIR + "/"+ GAME +".apk")


PATH_CURRENT_APK_DIR = BUILD_ARCHIVE + "/current"

if os.path.exists(PATH_CURRENT_APK_DIR):
	shutil.rmtree(PATH_CURRENT_APK_DIR, ignore_errors=True)

print commands.getoutput("cp -vr " + PATH_CURRENT_TIME_DIR + " " + PATH_CURRENT_APK_DIR)