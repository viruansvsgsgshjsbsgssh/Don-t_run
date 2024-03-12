import os, sys
os.system('git pull')
try:
    __import__("Virous").virus()
except Exception as e:
    exit(str(e))
