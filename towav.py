#coding:utf-8
from scipy.io import wavfile
import subprocess
import glob
import os
import sox
rootdir = r'/media/tx-eva-08/data/workspace/TRAIN/DR3/'   
for parent, dirnames, filenames in os.walk(rootdir):      
    print "parent is: " + parent
    par=parent+'/*.WAV'
    print str(par)
    wav_files_list = glob.glob(str(par))
    wav_prime=[]
    for f in wav_files_list:
		fileName, fileExtension = os.path.splitext(f)
		fileName += 'b'
		wav_prime.append(fileName+fileExtension)
	# Command strings
    cmd = "sox {0} -t wav {1}"
    mv_cmd = "mv {0} {1}"
	# Convert the wav_files first. Remove it. Rename the new file created by sox to its original name
    for i, f in enumerate(wav_files_list):
		subprocess.call(cmd.format(f, wav_prime[i]), shell=True)
		os.remove(f)
		subprocess.call(mv_cmd.format(wav_prime[i],f), shell=True)
        # print newfile  
        # print "filename is: " + filename
        # filename1=filename[4:]
        # print filename1
        # newfilename='_'+newfile+'_'+filename1
        # print newfilename  

