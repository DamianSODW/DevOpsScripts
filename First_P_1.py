import sys
import os
import subprocess

# System data
print("Byte order is: " + sys.byteorder)
print("Python size is: " + str(sys.getsizeof(1)))
print(str(sys.version_info))
print("System platform is: " + sys.platform)

# OS data
print(os.getcwd())  # current working directory
os.chdir("/home/kadzehana/python")  # change current directory
print(os.getcwd())
os.chdir("/home/kadzehana/python/DevOpsScripts")
os.chdir("../")
print(os.getcwd())

print(os.environ.get('USER'))  # Output value of environment variable
os.environ['LOGLEVEL'] = 'DEBUG'
print(os.environ.get('LOGLEVEL'))  # Insert value in env. variable
os.environ.pop('LOGLEVEL')  # Extract value from env. variable and delete it
print(os.environ.get('LOGLEVEL'))

print(os.getlogin())  # Take terminal user`s name

# Subprocesses

complprocess = subprocess.run(['ls', '-la'], capture_output=True,
                              universal_newlines=True)  # Run linux command and take it`s ComletedProcess object
print(complprocess.stdout)

cp = subprocess.run(['ls', '/doesnotexist'], capture_output=True, universal_newlines=True)  # Wrong command
print(cp.stderr)

cp = subprocess.run(['ls', '/doesnotexist'],
                    capture_output=True,
                    universal_newlines=True)#  check=True - make the exeption
