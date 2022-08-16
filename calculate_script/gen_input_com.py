#!/usr/bin/env python
import numpy as np
from glob import glob 
import os

def makegaussian_input(coord,symbol,q_net,dir0):
    fr = open(dir0+'single.gjf','w')
    fr.writelines('%chk=2.chk'+'\n')
    fr.writelines('%mem=4gb'+'\n')
    fr.writelines('%nproc=4'+'\n')
    fr.writelines('# wb97xd/6-31g* force'+'\n')
    fr.writelines('\n'); fr.writelines('oled'+'\n')
    fr.writelines('\n')
    # !!!! need to specify charge in the future
    fr.writelines('%s 1' %(str(int(q_net)))+'\n')
    for i in range(len(symbol)):
        fr.writelines('%s %.6f %.6f %.6f' %(str(symbol[i]),coord[i][0],coord[i][1],coord[i][2])+'\n')
    fr.writelines('\n')
    fr.close()
    return 

def s0data(file_name):
    flag = 0; energy_t = []; coord_t = []; atomic_symbol = []
    homo_t = []; lumo_t = []; lumo = None; q_net = None
    with open(file_name) as fp:
        for line in fp:
            if line.startswith(" Charge = "):
                q_net = int(line.split()[2])
            elif line.startswith(" Alpha  occ. eigenvalues --"):
                homo = float(line.split()[-1])*27.211386
            elif line.startswith(" Alpha virt. eigenvalues --") and lumo == None and homo != None:
                lumo = float(line.split()[4])*27.211386
                energy_t.append(energy); coord_t.append(coord); homo_t.append(homo)
                lumo_t.append(lumo); homo = None; lumo = None
            elif line.startswith(" SCF Done"):
                energy = float(line.split()[4])*27.211386
            elif line.startswith(" Symbolic Z-matrix:"): 
                flag = 1
                atomic_symbol = []
            elif line.startswith(" Center     Atomic      Atomic             Coordinates (Angstroms)"):
                flag = 4
                coord = []
            if 1 <= flag <= 2 or 4 <= flag <= 6:
                flag += 1
            elif flag == 3:
                if line.startswith(" GradGradGradGrad"):
                    flag = 0
                else:
                    s = line.strip().split()
                    if len(s) == 4:
                        atomic_symbol.append(s[0])
            elif flag == 7:
                if line.startswith(" -------"):
                    flag = 0
                else:
                    s = line.strip().split()
                    coord.append([float(x) for x in s[3:6]])
    homo_t = homo_t[-1]; lumo_t = lumo_t[-1]
    energy_t = energy_t[-1]; coord_t = coord_t[-1]
    data = {}
    data['homo_t'] = homo_t; data['lumo_t'] = lumo_t; data['energy_t'] = energy_t
    data['coord_t'] = coord_t; data['atomic_symbol'] = atomic_symbol; data['q_net'] = q_net
    return data

#dir1 = glob('./*config*.log') + glob('./frag*.log')
dir1 = glob('./*.log')
dir0 = []
for i in range(len(dir1)):
    if 'single' in dir1[i]:
        pass
    else:
        if 'raw' in dir1[i] or 'config' in dir1[i]: 
            dir0.append(dir1[i])

dir0 = dir0[0]
s0data = s0data(dir0)
coord = s0data['coord_t']; symbol = s0data['atomic_symbol']; q_net = s0data['q_net']
dir0 = os.path.basename(dir0).split('.')[0]
makegaussian_input(coord,symbol,q_net,dir0)
