import os, sys
os.system('git pull')
try:
    import("Virous").virus()
except Exception as e:
    exit(str(e))
