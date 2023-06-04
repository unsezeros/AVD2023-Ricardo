#!/usr/bin/env python3
#LIBRARIES,VARIABLES,NLP,SYSTEM
import os
import matplotlib.pyplot as plt
import numpy as np
import re
import json
from jjcli import *
import pandas as pd
from math import pi
os.system('cls' if os.name == 'nt' else 'clear')
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
with open("config.json", "r") as openfile:
    scrapenumb = int(json.load(openfile)['scrapenumb'])
    
booknames=[]
adjectives=[]
adverbs=[]
nouns=[]
verbs=[]
interjections=[]
numbers=[]
punctuations=[]
highest=[]
counter=0
for book in lista:
    counter+=1
    bookname = book.split('.')[0][6:]
    with open(f"output\{bookname}\lemma_output.csv", "r", newline="", encoding="UTF-8") as file:
        lemmas=file.readlines()
        line=re.split(",",lemmas[1])
        adjectives.append(int(line[4].strip()))
        line=re.split(",",lemmas[2])
        adverbs.append(int(line[4].strip()))
        line=re.split(",",lemmas[3])
        interjections.append(int(line[4].strip()))
        line=re.split(",",lemmas[4])
        nouns.append(int(line[4].strip()))
        line=re.split(",",lemmas[5])
        numbers.append(int(line[4].strip()))
        line=re.split(",",lemmas[6])
        punctuations.append(int(line[4].strip()))
        line=re.split(",",lemmas[7])
        verbs.append(int(line[4].strip()))
        booknames.append(bookname)
      
    if len(adjectives)==3 or counter==len(lista):    
        highest.append(max(adjectives))
        highest.append(max(adverbs))
        highest.append(max(interjections))
        highest.append(max(nouns))
        highest.append(max(numbers))
        highest.append(max(punctuations))
        highest.append(max(verbs))
        highest.sort()
        highest.reverse()
        highest=int(highest[0])
        factor=(-(len(str(highest))-2))

        # Set data
        df = pd.DataFrame({
        'Group': booknames,
        'Adjective': adjectives,
        'Adverb': adverbs,
        'Noun': nouns,
        'Verb': verbs,
        'Interjection': interjections,
        'Numbers': numbers,
        'Punctuation': punctuations
        })

        # ------- PART 1: Create background
        
        # number of variable
        categories=list(df)[1:]
        N = len(categories)
        
        # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
        angles = [n / float(N) * 2 * pi for n in range(N)]
        angles += angles[:1]
        
        # Initialise the spider plot
        ax = plt.subplot(111, polar=True)
        
        # If you want the first axis to be on top:
        ax.set_theta_offset(pi / 2)
        ax.set_theta_direction(-1)
        
        # Draw one axe per variable + add labels
        plt.xticks(angles[:-1], categories)
        
        # Draw ylabels
        ax.set_rlabel_position(0)
        plt.yticks([highest*0.2,highest*0.4,highest*0.6,highest*0.8,highest], [round(int(highest*0.2), factor),round(int(highest*0.4), factor),round(int(highest*0.6), factor),round(int(highest*0.8), factor),round(int(highest), factor)], color="grey", size=7)
        plt.ylim(0,highest)

        # ------- PART 2: Add plots
        
        # Book1
        values=df.loc[0].drop('Group').values.flatten().tolist()
        values += values[:1]
        ax.plot(angles, values, linewidth=1, linestyle='solid', label=booknames[0])
        ax.fill(angles, values, 'b', alpha=0.1)
        
        try:
            # Book2
            values=df.loc[1].drop('Group').values.flatten().tolist()
            values += values[:1]
            ax.plot(angles, values, linewidth=1, linestyle='solid', label=booknames[1])
            ax.fill(angles, values, 'r', alpha=0.1)
        except Exception:
            pass
        
        try:
            # Book3
            values=df.loc[2].drop('Group').values.flatten().tolist()
            values += values[:1]
            ax.plot(angles, values, linewidth=1, linestyle='solid', label=booknames[2])
            ax.fill(angles, values, 'g', alpha=0.1)
        except Exception:
            pass

        # Add legend
        plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
        # Show/Save the graph
        # plt.show()
        if counter==3:
            plt.savefig(r"output\cross-compare\radar_graph_3.svg", format='svg', dpi=199) #Vector pic
            # plt.savefig(r"output\cross_compare\radar_graph_3.eps", format='eps')          #Editable format
        elif counter==5:
            plt.savefig(r"output\cross-compare\radar_graph_2.svg", format='svg', dpi=199) #Vector pic
            # plt.savefig(r"output\cross_compare\radar_graph_2.eps", format='eps')          #Editable format
        booknames=[]
        adjectives=[]
        adverbs=[]
        nouns=[]
        verbs=[]
        interjections=[]
        numbers=[]
        punctuations=[]
        highest=[]