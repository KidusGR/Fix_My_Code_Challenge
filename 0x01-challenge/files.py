#!/usr/bin/python3

import os

mainRoot = "/home/kidus/Documents/Projects/Fix_My_Code_Challenge/0x01-challenge"
dir = "./blog"
'''
for root, dirs, files in os.walk(dir):
	for name in files:
		print(mainRoot+root[1:]+name)
		'''
def list_files(dir):                                                                                                  
    r = []                                                                                                            
    subdirs = [x[0] for x in os.walk(dir)]                                                                            
    for subdir in subdirs:                                                                                            
        files = os.walk(subdir).__next__()[2]                                                                             
        if (len(files) > 0):                                                                                          
            for file in files:                                                                                        
                r.append(os.path.join(subdir, file))
                                                                                       
    return r   

for file in list_files(dir):
	os.system(f"chmod +x {file}")
	
