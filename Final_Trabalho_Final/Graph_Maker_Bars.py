#!/usr/bin/env python3
#LIBRARIES,VARIABLES,NLP,SYSTEM
import os
import matplotlib.pyplot as plt
import re
from jjcli import *
os.system('cls' if os.name == 'nt' else 'clear')
os.chdir(r'C:\Users\ricas\Desktop\Drive\S2\AVD\Trabalho_Final')
class tcolors:
    pref = "\033["
    DEFAULT = f"{pref}0m"
    RED = f"{pref}91m"
    PURP = f"{pref}38;5;99m"
    YELL = f"{pref}93m"
    GREEN = f"{pref}92m"
    BLUE = f"{pref}36m" 
    BGREEN = f"{pref}38;5;46m"
    BLACK = f"{pref}30m"
    PINK =f"{pref}35m"
    WHITE = f"{pref}37m"
lista=glob("obras/*.md", recursive=True)
#//region[rgba(241, 1, 15, 0.15)]
for book in lista:
    ytitle=''
    itemtype1=''
    itemtype2=''
    itemtype3=''
    itemtype4=''
    count1=[]
    count2=[]
    count3=[]
    count4=[]
    item_for_label1=[]
    item_for_label2=[]
    item_for_label3=[]
    item_for_label4=[]
    bookname = book.split('.')[0][6:]
    with open(f"output\{bookname}\main_output.csv", "r", newline="", encoding="UTF-8") as file:
        maininfo=file.readlines()
    for item in maininfo:
        if maininfo.index(item)<1: #Have this value be pulled from the main python (avoid having to get a system to track the changes maybe?)
            pass
        #LOCAIS
        if maininfo.index(item)>=1 and maininfo.index(item)<=10:
            item=re.split(",",item)
            itemtype1=item[2]
            count1.append(int(item[4].strip()))
            item_for_label1.append(f'{item[3][:13].strip()}')
        #PESSOAS
        elif maininfo.index(item)>=11 and maininfo.index(item)<=20:
            item=re.split(",",item)
            itemtype2=item[2]
            count2.append(int(item[4].strip()))
            item_for_label2.append(f'{item[3][:13].strip()}')
        #ORGANIZAÇÔES
        elif maininfo.index(item)>=21 and maininfo.index(item)<=30:
            item=re.split(",",item)
            itemtype3=item[2]
            count3.append(int(item[4].strip()))
            item_for_label3.append(f'{item[3][:13].strip()}')
        #DATES
        elif maininfo.index(item)>=41 and maininfo.index(item)<=50:
            item=re.split(",",item)
            itemtype4=item[2]
            count4.append(int(item[4].strip()))
            item_for_label4.append(f'{item[3][:13].strip()}')
            
    #DEBUG
    # print(itemtype1)
    # print(item_for_label1)
    # print(count1)
    
    # print(itemtype2)
    # print(item_for_label2)
    # print(count2)
    
    # print(itemtype3)
    # print(item_for_label3)
    # print(count3)
    
    # print(itemtype4)
    # print(item_for_label4)
    # print(count4)
    #//endregion

    #//region[rgba(241, 196, 15, 0.2)]
    #Matplotlib
    # plt.style.use('dark_background')
    xcoord1=item_for_label1
    xcoord2=item_for_label2
    xcoord3=item_for_label3
    xcoord4=item_for_label4
    font1 = {'family':'serif','color':'darkred','size':20}
    font2 = {'family':'serif','color':'darkred','size':15}
    fig, axs = plt.subplots(2, 2)
    axs[0, 0].bar(xcoord1, count1, color="#7bbee2", label =f'{itemtype1}')
    axs[0, 0].set_xticklabels(item_for_label1,rotation = 10)

    axs[0, 1].bar(xcoord2, count2, color="#F6ef75", label =f'{itemtype2}')
    axs[0, 1].set_xticklabels(item_for_label2,rotation = 10)

    axs[1, 0].bar(xcoord3, count3, color="#A7f675", label =f'{itemtype3}')
    axs[1, 0].set_xticklabels(item_for_label3,rotation = 10)
    
    axs[1, 1].bar(xcoord4, count4, color="#F87f66", label =f'{itemtype4}')
    axs[1, 1].set_xticklabels(item_for_label4,rotation = 10)
    
    for ax in axs.flat:
        ax.set(xlabel='Ocorrência', ylabel='Nº OcorrÊncias')
        ax.grid()
        ax.legend(loc='upper right', ncols=4)
        # ax.set_xlim(0.3,9.7) #Spread the bars a little BREAKS IT
        plt.draw()

    fig.suptitle(f'Items extraídos do livro "{bookname}"',fontsize=20)
    fig.subplots_adjust(bottom=0.105, left=0.055, top = 0.925, right=0.9)
    if len(xcoord1)<=20:
        plt.gcf().set_size_inches(16, 7)      #Smaller x-values
    else:
        plt.gcf().set_size_inches(23, 7)      #Larger x-values
    # plt.show()
    plt.savefig(f"output\{bookname}\main_graph.svg", format='svg', dpi=199) #Vector pic
    plt.savefig(f"output\{bookname}\main_graph.eps", format='eps') #Editable format
    #//endregion