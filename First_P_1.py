import sys
import os

# System data
print("Byte order is: " + sys.byteorder)
print("Python size is: " + str(sys.getsizeof(1)))
print(str(sys.version_info))
print("System platform is: " + sys.platform)

# OS data
print(os.getcwd()) #cerrent working directory
