#Using dpdata for reading CP2K output files;including .ener/.out(or log files,need the printing level Medium or above)/~frc.xyz/~pos.xyz

import dpdata
from ase.io import write

#reading the cp2k output data files
data=dpdata.LabeledSystem('./11/',cp2k_output_name='NMC_water-1.out',fmt='cp2kdata/md')



ase_list = data.to_ase_structure() 
write("11.extxyz", ase_list)
