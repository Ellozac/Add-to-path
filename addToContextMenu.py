import os
import sys
import winreg as reg

cwd = os.getcwd()
python_exe = sys.executable

hidden_terminal = '\\'.join(python_exe.split('\\')[:-1])+"\\pythonw.exe"


key_path = r'Directory\\Background\\shell\\addToPath\\'

key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path)
reg.SetValue(key, '', reg.REG_SZ, '&Add to path')


key1 = reg.CreateKey(key, r"command")
reg.SetValue(key1, '', reg.REG_SZ, python_exe + f' "{cwd}\\main.py"')

# IMPORTANT
# To remove
# open regedit and remove the outer key found at this path
# HKEY_CLASSES_ROOT\Directory\Background\shell\addToPath