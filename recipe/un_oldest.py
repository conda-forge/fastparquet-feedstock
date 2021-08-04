lines=open("setup.py").readlines()
open("setup.py", "w").writelines([l for l in lines if "oldest-supported-numpy" not in l])
