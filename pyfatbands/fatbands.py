import matplotlib.pyplot as plt 
import numpy as np 
import matplotlib as mpl 
import os
import sys
import argparse
from argparse import RawTextHelpFormatter
mpl.use('Agg') 
############ HELP COMMANDS #############
def main(): 
    description_text=("Simple script that plots the .dat files obtained an eigfat2plot run within the SIESTA package. \n""Developed in the Master thesis work of Moioli Matteo, University of Milan, under the supervision of Prof. Martinazzo and Dr. Davide Ceresoli. \n")
    parser = argparse.ArgumentParser(description= description_text, formatter_class=RawTextHelpFormatter, usage='Simple script that plots .dat files obtained from a fatband calculation in SIESTA')
    parser.add_argument('-files', metavar= '.dat files', nargs= '+',help= 'Input as many .dat files you want to plot')
    parser.add_argument('-F', metavar='Fermi energy', type= float, help= 'Input the Fermi energy for shifting the plot',default= 0.0)
    parser.add_argument('-y', metavar= 'minimum y', type= float, help= 'Minimum energy (if the plot is shifted, then wrt Fermi energy) for the plot')
    parser.add_argument('-Y', metavar= 'maximum y', type=float, help= 'Maximum energy (if the plot is shifted, then wrt Fermi energy) for the plot')
    parser.add_argument('-o', metavar= 'Output', help= 'Output (.png) file name', default='fatbands')
    parser.add_argument('-dpi', metavar= 'image dpi',type= int, nargs= '?', help= 'Dots Per Inch for the .png image, indicating the quality of the latter. Default=300', default= 300)

############ IF NOT GIVEN ANY INPUT, PRINT THE HELP
    if len(sys.argv)==1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()
    path=r"./"
    filenames = args.files
    fermi= args.F

    colors = []
    for i in range(len(filenames)):
        colors.append(f'C{i}')    

    col_ind = 0
    title=input("Enter the image Title: ")
#from a single .dat file extract all the data set and splice them up in vectors with legth given by the number of points. Each splice is the plotted "on-the-fly" and, for the last plot, is given the label
    for file in filenames:
        fb= os.path.join(path, file)   
    
        gollum= open(fb, 'r')
        content= gollum.readlines()
        columns= content[1].strip().split()
        nkp= int(columns[6])
    
    #data= np.loadtxt(fb,dtype=float)
    #x, y, err = data[:,0], data[:,1], data[:,2]
        x, y, err, weight= np.loadtxt(fb,dtype=float, unpack= True)
        length= len(x)
        number= length/nkp

        kp, en, fat= np.array_split(x, number), np.array_split(y, number), np.array_split(err, number)
    
        ind= 0
    
        while ind < number :
            if (ind == number - 1):
                plt.fill_between(kp[ind], en[ind] - fermi + fat[ind]/2, en[ind] - fermi - fat[ind]/2, color=colors[col_ind], label=f'{file}', alpha= 0.5)
                plt.plot(kp[ind], en[ind] - fermi, color= 'black', linewidth= 1)
            else:
                plt.fill_between(kp[ind], en[ind] - fermi + fat[ind]/2, en[ind] - fermi - fat[ind]/2, color=colors[col_ind], alpha= 0.5)
                plt.plot(kp[ind], en[ind] - fermi, color= 'black', linewidth= 1)
            ind += 1
        col_ind += 1

    plt.legend(loc='upper right')
    plt.title(title)
    plt.xlabel('K-points')
    plt.xlim([kp[0][0], kp[0][nkp - 1]])
    plt.ylim([args.y,args.Y])
    plt.ylabel('E - Ef (eV)')
    plt.savefig(f'{args.o}.png', dpi=args.dpi)



