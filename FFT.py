import matplotlib.pyplot as plt
from scipy.io import wavfile
import glob
import os
def graph_spectrogram(wav_file,f):
    rate, data = get_wav_info(wav_file)
    nfft = 256  # Length of the windowing segments
    fs = 256    # Sampling frequency
    pxx, freqs, bins, im = plt.specgram(data, nfft,fs)
    plt.axis('off')
    filename=wav_file
    file=filename[48:]
    path2='/media/tx-eva-08/data/workspace/dr3/'+f+'/'+file
    path3='/media/tx-eva-08/data/workspace/dr3/'+f+'/'
    if os.path.exists(path3):
        return True
    os.mkdir(path3)
    print file
    print "path2:::"+path2
    plt.savefig(path2+'.png',
                dpi=100, # Dots per inch
                frameon='false',
                aspect='normal',
                bbox_inches='tight',
                pad_inches=0) # Spectrogram saved as a .png 
    print "saved ........."
def get_wav_info(wav_file):
    rate, data = wavfile.read(wav_file)
    return rate, data

if __name__ == '__main__': # Main function
    rootdir = r'/media/tx-eva-08/data/workspace/TRAIN/DR3/'
    for parent, dirnames, filenames in os.walk(rootdir):
        # for filename in filenames:  
        print "parent is: " + parent
        newfile=parent[42:]
        print newfile  
        par=parent+'/*.WAV'
        print str(par)
        wav_files_list = glob.glob(str(par))
        for f in wav_files_list:
            print 'fff'+f
            fi=f[48:]
            graph_spectrogram(f,newfile)
    # for filename in glob.glob(os.path.join(path, '*.WAV')):
    #     print "file"+filename
    #     #wav_file = 'SA2.WAV' # Filename of the wav file
    #     graph_spectrogram(filename)