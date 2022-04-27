from ligotools import readligo as rl
import numpy as np
import pytest



def test_loaddata():
    data = rl.loaddata("data/H-H1_LOSC_4_V2-1126259446-32.hdf5")
    assert data[0][1] == 2.087638998830647e-19


def test_read_hdf5():
    data = rl.loaddata("data/H-H1_LOSC_4_V2-1126259446-32.hdf5")
    assert data[0][0] == 2.177040281449375e-19
    
def test_dq_channel_to_seglist():
    fn_L1 = 'data/L-L1_LOSC_4_V1-1126259446-32.hdf5'
    strain, time, chan_dict = rl.loaddata(fn_L1, 'H1')
    DQflag = 'CBC_CAT3'
    data = rl.dq_channel_to_seglist(chan_dict[DQflag])
    assert data == [slice(0, 131072, None)]
    
def test_dq2segs():
    fn_L1 = 'data/L-L1_LOSC_4_V1-1126259446-32.hdf5'
    strain, time, chan_dict = rl.loaddata(fn_L1, 'H1')
    DQflag = 'CBC_CAT3' 
    data = rl.dq2segs(chan_dict[DQflag], time[0])
    x = str((rl.dq2segs(chan_dict[DQflag], time[0])))
    y = 'SegmentList( [(1126259446, 1126259478)] )'
    assert x==y
    
    
    
        