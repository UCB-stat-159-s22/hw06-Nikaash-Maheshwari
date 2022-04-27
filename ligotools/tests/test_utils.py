from ligotools import readligo as rl
import numpy as np
import pytest
import matplotlib.mlab as mlab
from scipy.interpolate import interp1d
import os

def test_whiten():
    arr = np.ones(5000)
    Pxx_H1, freqs = mlab.psd(arr, Fs = 4096, NFFT = 16384)
    psd_H1 = interp1d(freqs, Pxx_H1)
    output = whiten(arr,psd_H1,0.000244140625)[1]
    assert output == 0.08703763753077194
    
    
def test_write_wavfile():
    output = write_wavfile("test.wav",4096, np.ones(5000))
    output_type = type(output)
    assert output_type == None
    
def test_reqshift():
    output = reqshift(np.ones(5000),fshift=400,sample_rate=0.01)[0]
    assert output == 0.0
    
def test_write_wavfile_two():
    output = write_wavfile("test.wav",4096, np.ones(5000))
    assert os.path.exists("test.wav")
    os.remove("test.wav")
    
    
    
    