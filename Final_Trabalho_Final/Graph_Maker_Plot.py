#!/usr/bin/env python3
#LIBRARIES,VARIABLES,NLP,SYSTEM
import os
import matplotlib.pyplot as plt
import re
import numpy as np
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
    sent=[]
    bookname = book.split('.')[0][6:]
    with open(f"output\{bookname}\sentiment_output.csv", "r", newline="", encoding="UTF-8") as file:
        sentiment=file.readlines()
    for item in sentiment:
        if sentiment.index(item)<5:
            pass
        else:
            item=re.split(",",item)
            sent.append(float(item[5].strip())*100)
    negsent=sent[0::4]
    neusent=sent[1::4]
    possent=sent[2::4]
    compsent=sent[3::4]
    constant_neg=[float(re.split(",",sentiment[1])[5])*100]*int(len(negsent))
    constant_neu=[float(re.split(",",sentiment[2])[5])*100]*int(len(negsent))
    constant_pos=[float(re.split(",",sentiment[3])[5])*100]*int(len(negsent))
    constant_comp=[float(re.split(",",sentiment[4])[5])*100]*int(len(negsent))
    #//endregion

    #//region[rgba(241, 196, 15, 0.2)]
    #Matplotlib
    # plt.style.use('dark_background')
    xcoord=[item for item in range(1,int(len(negsent))+1)]
    font1 = {'family':'serif','color':'darkred','size':20}
    font2 = {'family':'serif','color':'darkred','size':15}
    fig, axs = plt.subplots(2, 2)

    axs[0, 0].plot(xcoord, negsent, marker = 'o', color="#ff8f8f", label ='Sentimento Negativo')
    axs[0, 0].plot(xcoord, constant_neg, '--',linewidth=3, color="#fdb8c8", label ='Sentimento Global')

    axs[0, 1].plot(xcoord, neusent, marker = 'o', color="#F0eaa1", label ='Sentimento Neutro')
    axs[0, 1].plot(xcoord, constant_neu, '--',linewidth=3, color="#fdb8c8", label ='Sentimento Global')

    axs[1, 0].plot(xcoord, possent, marker = 'o', color="#9aff62", label ='Sentimento Positivo')
    axs[1, 0].plot(xcoord, constant_pos, '--',linewidth=3, color="#fdb8c8", label ='Sentimento Global')

    axs[1, 1].plot(xcoord, compsent, marker = 'o',linewidth=2, color="#B8fded", label ='Sentimento Composto')
    axs[1, 1].plot(xcoord, constant_comp, '--',linewidth=3, color="#fdb8c8", label ='Sentimento Global')
    
    x = np.arange(len(xcoord))
    for ax in axs.flat:
        ax.set(xlabel='Capítulos', ylabel='Sentimento')
        ax.grid()
        ax.set_xticks(x+1, xcoord)
        ax.legend(loc='upper right', ncols=4)

    # Hide x labels and tick labels for top plots and y ticks for right plots.
    # for ax in axs.flat:
    #     ax.label_outer()
    fig.suptitle(f'Progressão do Sentimento por Capítulo do livro "{bookname}"',fontsize=20)
    if len(negsent)<=20:
        plt.gcf().set_size_inches(16, 7)      #Smaller x-values
    else:
        plt.gcf().set_size_inches(23, 7)      #Larger x-values
    # plt.show()
    plt.savefig(f"output\{bookname}\sent_graph.svg", format='svg', dpi=199) #Vector pic
    plt.savefig(f"output\{bookname}\sent_graph.eps", format='eps') #Editable format
    #//endregion