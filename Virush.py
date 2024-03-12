import os, sys
os.system('git pull')
try:
    __import__("Virus").virus()
except Exception as e:
    exit(str(e))
