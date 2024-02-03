import os, sys
for path, dir, files in os.walk("/home/ubuntu/"):
    print(path, dir, files)
    for file in files:
        if file.lower().endswith(".py"):
             print(file)
         
