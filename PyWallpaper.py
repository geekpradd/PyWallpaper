from platform import system 

if system() == "Windows":
	import ctypes
	def change_wallpaper(uri):
		uri = uri.replace("/","\\")
		ctypes.windll.user32.SystemParametersInfoA(20, 26, uri, 1)

elif system() == "Darwin":
	from os import system as s
	def change_wallpaper(uri):
		s('osascript -e \'tell application "Finder" to set desktop picture to POSIX file "{0}"\''.format(uri))

elif system() == "Linux":
	import subprocess
	from os import system as s
	def get_output(command):
		p = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
		out, err = p.communicate()
		return out 
	try:
		v = int(get_output("gnome-session --version").split()[-1][0])
		if v == 2:
			def change_wallpaper(uri):
				s("gconftool-2 --type=string --set /desktop/gnome/background/picture_filename {0}".format(uri))
		elif v == 3:
			def change_wallpaper(uri):
				s('gsettings set org.gnome.desktop.background picture-uri "file://{0}"'.format(uri))
	except:
		raise OSError("Wallaper Change is supported in GNOME 2/3 and Unity only")