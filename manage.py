'''
Management file to manage operations on project/app.
Author:             Iron-Legion@GCOEJ
Date:               01 NOVEMBER 2021
'''

import sys
import os

arglist = sys.argv

try:
	# Help options
	if arglist[1] == "--help" or arglist[1] == "-h":
		print("\n--------------------Help Options--------------------\n")
		print("create OR -c:\tCreates project.")

	elif arglist[1] == "-c" or arglist[1] == "create":
		# Clone repository from github and remove .git dir.
		# os.system("git clone https://github.com/New-Byte/Android_Template.git")
		os.system("attrib -h .git")
		os.rename(".git","git")
		os.system("rmdir /Q /S git")

		# Write README.md
		f = open("./README.md","w")
		f.write("# " + arglist[2] + "\n" + "Project Description")
		f.close()

		# Rename root folder
		os.system("ren " +"template " + arglist[2])

		# Add gitignore file
		f = open(arglist[2]+"/android/.gitignore","w")
		f.write("*.iml\n.gradle\n/local.properties\n/.idea/caches\n/.idea/libraries\n/.idea/modules.xml\n/.idea/workspace.xml\n/.idea/navEditor.xml\n/.idea/assetWizardSettings.xml\n.DS_Store\n/build\n/captures\n.externalNativeBuild\n.cxx")
		f.close()

		# Rename folders to hidden folders
		os.rename(arglist[2]+"/android/gradle1", arglist[2]+"/android/.gradle")
		os.rename(arglist[2]+"/android/idea", arglist[2]+"/android/.idea")

		# Search for meraBharat in each file and replace it with app_name (arglist[2])

		path = arglist[2]+"/android"

		# Read all files in android dir.
		filelist = []
		prev_path = arglist[2]
		for root, dirs, files in os.walk(path, topdown=True):
			# Change any dir with name MeraBharat and rename it with appname
			for dir0 in dirs:
				dir_path = os.path.join(root, dir0)
				if "MeraBharat" in dir_path:
					os.rename(dir_path, prev_path + os.sep + arglist[2])
				elif "MeraBharat".lower() in dir_path:
					os.rename(dir_path, prev_path + os.sep + arglist[2].lower())
				elif "MeraBharat".upper() in dir_path:
					os.rename(dir_path, prev_path + os.sep + arglist[2].upper())
				prev_path = dir_path

			# read path to each file
			for file in files:
				#filelist.append(os.path.join(root,file))
				x = os.path.join(root,file)
				#print("File: " + x)
				try:
					f = open(r+"'"+x+"'","r")
					f_data = f.readlines()
					f.close()
				except:
					continue
				flag = 0
				# Check if MeraBharat is present in file
				for y in range(len(f_data)):
					if "MeraBharat" in f_data[y]:
						flag = 1
						# Replace MeraBharat with app_name
						f_data[y] = f_data[y].replace("MeraBharat", arglist[2])
					elif "meraBharat".lower() in f_data[y]:
						flag = 1
						f_data[y] = f_data[y].replace("MeraBharat".lower(), arglist[2].lower())
					elif "meraBharat".upper() in f_data[y]:
						flag = 1
						f_data[y] = f_data[y].replace("MeraBharat".upper(), arglist[2].upper())
				# Update file
				if flag:
					f = open(r+"'"+x+"'","w")
					f.writelines(f_data)
					f.close()

		# Update java dir
		for root, dirs, files in os.walk(path+"/app/src/main/java", topdown=True):
			for file in files:
				x = os.path.join(root,file)
				try:
					f = open(r+"'"+x+"'","r")
					f_data = f.readlines()
					f.close()
				except:
					continue
				flag = 0
				# Check if MeraBharat is present in file
				for y in range(len(f_data)):
					if "MeraBharat" in f_data[y]:
						flag = 1
						# Replace MeraBharat with app_name
						f_data[y] = f_data[y].replace("MeraBharat", arglist[2])
					elif "meraBharat".lower() in f_data[y]:
						flag = 1
						f_data[y] = f_data[y].replace("MeraBharat".lower(), arglist[2].lower())
					elif "meraBharat".upper() in f_data[y]:
						flag = 1
						f_data[y] = f_data[y].replace("MeraBharat".upper(), arglist[2].upper())
				# Update file
				if flag:
					f = open(r+"'"+x+"'","w")
					f.writelines(f_data)
					f.close()
					
		app_nm = arglist[2]

	elif arglist[1] == "--apk" or arglist[1] == "createapk":
		ls = os.listdir('./')
		app_nm = [x for x in ls if os.path.isdir(x)][0]
		try:
			new_nm = arglist[2]
		except:
			new_nm = app_nm + "v1"
		print("Creating logs....")
		f = open(app_nm+"/apk/logs.txt","w")
		f.write("Building App " + app_nm + ".....\n\n")
		f.close()
		exit_stat = os.system(os.path.join(app_nm+"\\android","gradlew")+" assembleDebug >> " + app_nm + "/apk/logs.txt")
		if exit_stat:
			f = open(app_nm+"/apk/logs.txt","a")
			f.write("\n######OPERATION FAILED#######\n")
			f.close()
			exit()
		else:
			f.write("\n######OPERATION IS SUCCESSFUL#######\n")
			f.close()
			# Copy apk to apk dir
			exit_stat1 = os.system("copy " + app_nm+"/android/build/outputs/apk/debug/app-debug.apk " + app_nm + "/apk/"+new_nm+".apk") 
			if exit_stat1:
				print("FAILED TO BUILD APK...\nCHECK LOGS"+"("+ app_nm+"/apk/logs.txt) FOR MORE INFO....")
			else:
				print("BUILD WAS SUCCESSFUL...\nAPK CREATED AT " + app_nm+"/apk/")

except:
	print("============================================")
	print("\nmanage.py expects at least 1 argument,\n0 were given.\n\nE.g.: python manage.py --help\n")
	print("============================================")
