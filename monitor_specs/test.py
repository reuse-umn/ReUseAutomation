import subprocess
import re
import os

data=str(subprocess.check_output(['hwinfo', '--monitor'])).split("\\n\\n")
for mon in data:
    print(mon)
    print(re.findall('Unique ID: ([\w.]+)', mon)[0])
