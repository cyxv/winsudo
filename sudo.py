import ctypes, subprocess, sys

def admincheck():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
        
if admincheck():
    subprocess.run(' '.join(sys.argv[1:]))
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, ' '.join(sys.argv), None, 1)