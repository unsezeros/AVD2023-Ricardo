#!/usr/bin/env python3
#LIBRARIES,VARIABLES,NLP,SYSTEM
import os
import subprocess
import spacy
import json
import re
from collections import Counter
from jjcli import *
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
os.system('cls' if os.name == 'nt' else 'clear')
subprocess.call(['Remove_output.bat'])
try:
    os.mkdir("output")
except Exception:
    pass
try:
    os.mkdir("output\cross-compare")
except Exception:
    pass
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
print("Loading Spacy!")
nlp = spacy.load('pt_core_news_lg')
print("Spacy Loaded!")
bookcount=0
scrapenumb=15
with open("config.json", "w") as outfile:
    outfile.write(json.dumps({"scrapenumb":scrapenumb}, indent=1))
charnames=""
#PROGRAM START ##############################################################################################
for book in lista:
    bookname = book.split('.')[0][6:]
    os.mkdir(f"output\{bookname}")
    with open(f"output\{bookname}\main_output.csv", "w", newline="", encoding="UTF-8") as file:
            file.writelines('BOOKNUM,BOOK,ITEMTYPE,ITEM,COUNT\n')
    with open(f"output\{bookname}\lemma_output.csv", "w", newline="", encoding="UTF-8") as file:
            file.writelines('BOOKNUM,BOOK,ITEMTYPE,ITEM,COUNT\n')
    with open(f"output\{bookname}\sentiment_output.csv", "w", newline="", encoding="UTF-8") as file:
            file.writelines('BOOKNUM,BOOK,CHAPT,ITEM,COUNT,RELATIVECOUNT\n')
    bookcount+=1
    placelist=[]
    perslist=[]
    orglist=[]
    misclist=[]
    print(f"Analysing {tcolors.PURP}{book}{tcolors.WHITE}")
    with open(book, encoding='UTF-8') as f:
        booktext = f.read()
    doc = nlp(booktext)
    #//region[rgba(25, 255, 0, 0.2)]
    #Procurar as localizações e listar
    for item in doc.ents:
        #Clean data
        if str(item)=="—":
            pass
        elif str(item)=="-":
            pass
        elif str(item)=="–":
            pass
        else:
            if item.label_ == "LOC":
                item = str(item).strip()
                placelist.append(item)
                placelist.sort()
    for _ in range(0,len(placelist)):
        locais = Counter(placelist).most_common(scrapenumb)
    #//endregion
    
    #//region[rgba(210, 105, 30, 0.2)]
    #Procurar as organizações e listar
    for item in doc.ents:
        #Clean data
        if str(item)=="—":
            pass
        elif str(item)=="-":
            pass
        elif str(item)=="–":
            pass
        else:
            if item.label_ == "ORG":
                item = str(item).strip()
                orglist.append(item)
                orglist.sort()
    for _ in range(0,len(orglist)):
        org = Counter(orglist).most_common(scrapenumb)
    #//endregion
    
    #//region[rgba(210, 105, 320, 0.2)]
    #Procurar as Miscelâneos e listar
    for item in doc.ents:
        #Clean data
        if str(item)=="—":
            pass
        elif str(item)=="-":
            pass
        elif str(item)=="–":
            pass
        else:
            if item.label_ == "MISC":
                item = str(item).strip()
                misclist.append(item)
                misclist.sort()
    for _ in range(0,len(misclist)):
        misc = Counter(misclist).most_common(scrapenumb)
    #//endregion

    #//region[rgba(52, 152, 300, 0.2)]
    #Procurar os nomes e listar
    for item in doc.ents:
        #Clean data
        if str(item)=="—":
            pass
        elif str(item)=="-":
            pass
        elif str(item)=="–":
            pass
        else:
            if item.label_ == "PER":
                item = str(item).strip()
                perslist.append(item)
                perslist.sort()
    #Limpeza automática de nomes (Provided a Char file is present)
    try:
        with open(f"obras\{bookname}_Char.txt", "r", encoding="UTF-8") as file:
            charnames = str(file.read())
            charnames = re.split("\n", charnames)
        print("Character names file found!")
        name_clean_counter=0
        for _ in charnames:
            for __ in perslist:
                # print("$",__)
                # print(charnames.index(_))
                if __ in charnames[name_clean_counter]:
                    # __ = charnames[name_clean_counter]
                    pos = perslist.index(__)
                    perslist.pop(pos)
                    # print(perslist)
                    perslist.insert(pos,_)
                    # print(perslist)
                else:
                    # print(f"{tcolors.PURP}Wont compile{tcolors.WHITE}")
                    pass
            name_clean_counter+=1
        # print(perslist)
        # input("#")                   
    except Exception:
        print("Character names file missing or not present!")
    for _ in range(0,len(perslist)):
        pessoas = Counter(perslist).most_common(scrapenumb)
    #//endregion

    #//region[rgba(241, 1, 15, 0.15)]
    #LEMMA EXTRACTION
    occorlist = []
    for word in doc:
        if word.pos_ == "VERB":
            occorlist.append(word.lemma_)
            occorlist.sort()
    lemma_verb_total=len(occorlist)
    for _ in range(0,len(occorlist)):
        lemma_verb = Counter(occorlist).most_common(scrapenumb)
    occorlist = []
    for word in doc:
        if word.pos_ == "ADJ":
            occorlist.append(word.lemma_)
            occorlist.sort()
    lemma_adj_total=len(occorlist)
    for _ in range(0,len(occorlist)):
        lemma_adj = Counter(occorlist).most_common(scrapenumb)
    occorlist = []
    for word in doc:
        if word.pos_ == "ADV":
            occorlist.append(word.lemma_)
            occorlist.sort()
    lemma_adv_total=len(occorlist)
    for _ in range(0,len(occorlist)):
        lemma_adv = Counter(occorlist).most_common(scrapenumb)
    occorlist = []
    for word in doc:
        if word.pos_ == "INTJ":
            occorlist.append(word.lemma_)
            occorlist.sort()
    lemma_intj_total=len(occorlist)
    for _ in range(0,len(occorlist)):
        lemma_intj = Counter(occorlist).most_common(scrapenumb)
    occorlist = []
    for word in doc:
        if word.pos_ == "NOUN":
            occorlist.append(word.lemma_)
            occorlist.sort()
    lemma_noun_total=len(occorlist)
    for _ in range(0,len(occorlist)):
        lemma_noun = Counter(occorlist).most_common(scrapenumb)
    occorlist = []
    for word in doc:
        if word.pos_ == "NUM":
            occorlist.append(word.lemma_)
            occorlist.sort()
    lemma_num_total=len(occorlist)
    for _ in range(0,len(occorlist)):
        lemma_num = Counter(occorlist).most_common(scrapenumb)
    occorlist = []
    for word in doc:
        if word.pos_ == "PUNCT":
            occorlist.append(word.lemma_)
            occorlist.sort()
    lemma_punct_total=len(occorlist)
    for _ in range(0,len(occorlist)):
        lemma_punct = Counter(occorlist).most_common(scrapenumb)
    #//endregion

    #//region[rgba(255, 255, 0, 0.25)]
    #DATES
    dates = re.findall("\d{4}",booktext)
    dates = Counter(dates).most_common(scrapenumb)
    #//endregion

    #//region[rgba(250, 255, 0, 0.4)]
    print("Analysing sentiment!")
    sent_list=[]
    gtotalcompound=0.0
    gtotalnegativewords=0.0
    gtotalneutralwords=0.0
    gtotalpositivewords=0.0
    chaptnum=1
    analyzer = SentimentIntensityAnalyzer()
    vs = analyzer.polarity_scores(booktext)
    text = re.split("## ",booktext)
    for chapt in text[1:]:
        vs = analyzer.polarity_scores(chapt)
        totalnegativewords=vs["neg"]
        totalneutralwords=vs["neu"]
        totalpositivewords=vs["pos"]
        totalcompound=vs["compound"]
        sent_list.append(f"{bookcount},{book},{chaptnum},negative,{int(totalnegativewords*len(booktext.split()))},{totalnegativewords}\n")
        sent_list.append(f"{bookcount},{book},{chaptnum},neutral,{int(totalneutralwords*len(booktext.split()))},{totalneutralwords}\n")
        sent_list.append(f"{bookcount},{book},{chaptnum},positive,{int(totalnegativewords*len(booktext.split()))},{totalpositivewords}\n")
        sent_list.append(f"{bookcount},{book},{chaptnum},compound,,{totalcompound}\n")
        chaptnum+=1
        gtotalcompound=gtotalcompound+totalcompound
        gtotalnegativewords=gtotalnegativewords+totalnegativewords
        gtotalneutralwords=gtotalneutralwords+totalneutralwords
        gtotalpositivewords=gtotalpositivewords+totalpositivewords
    chaptnum=chaptnum-1
    gtotalcompound=(gtotalcompound/chaptnum)
    gtotalnegativewords=(gtotalnegativewords/chaptnum)
    gtotalneutralwords=(gtotalneutralwords/chaptnum)
    gtotalpositivewords=(gtotalpositivewords/chaptnum)
    #//endregion

    #//region[rgba(241, 196, 15, 0.2)]
    print("Printing results!\n")
    #Writing POI into CSV file
    with open(f"output\{bookname}\main_output.csv", "a", newline="", encoding="UTF-8") as file:
        for data in locais:
            file.write(f"{bookcount},{book},locais,{data[0]},{data[1]}\n")
        for data in pessoas:
            file.write(f"{bookcount},{book},pessoas,{data[0]},{data[1]}\n")
        for data in org:
            file.write(f"{bookcount},{book},organizações,{data[0]},{data[1]}\n")
        for data in misc:
            file.write(f"{bookcount},{book},misc,{data[0]},{data[1]}\n")
        for data in dates:
            file.write(f"{bookcount},{book},datas,{data[0]},{data[1]}\n")
    #Writing lemma into CSV file        
    with open(f"output\{bookname}\lemma_output.csv", "a", newline="", encoding="UTF-8") as file:
        file.write(f"{bookcount},{book},AdjectiveTotal,,{lemma_adj_total}\n")
        file.write(f"{bookcount},{book},AdverbTotal,,{lemma_adv_total}\n")
        file.write(f"{bookcount},{book},InterjectionTotal,,{lemma_intj_total}\n")
        file.write(f"{bookcount},{book},NounTotal,,{lemma_noun_total}\n")
        file.write(f"{bookcount},{book},NumberTotal,,{lemma_num_total}\n")
        file.write(f"{bookcount},{book},PunctuationTotal,,{lemma_punct_total}\n")
        file.write(f"{bookcount},{book},VerbTotal,,{lemma_verb_total}\n")
        
        for data in lemma_adj:
            file.write(f"{bookcount},{book},Adjective,{data[0]},{data[1]}\n")
        for data in lemma_adv:
            file.write(f"{bookcount},{book},Adverb,{data[0]},{data[1]}\n")
        for data in lemma_intj:
            file.write(f"{bookcount},{book},Interjection,{data[0]},{data[1]}\n")
        for data in lemma_noun:
            file.write(f"{bookcount},{book},Noun,{data[0]},{data[1]}\n")
        for data in lemma_num:
            file.write(f"{bookcount},{book},Numbers,{data[0]},{data[1]}\n")
        for data in lemma_punct:
            if data[0] == ",":
                file.write(f'{bookcount},{book},Punctuation,"{data[0]}",{data[1]}\n')
            elif data[0] == '"':
                file.write(f"{bookcount},{book},Punctuation,'{data[0]}',{data[1]}\n")
            else:
                file.write(f"{bookcount},{book},Punctuation,{data[0]},{data[1]}\n")
        for data in lemma_verb:
            file.write(f"{bookcount},{book},Verb,{data[0]},{data[1]}\n")
    #Writing sentiment into CSV file        
    with open(f"output\{bookname}\sentiment_output.csv", "a", newline="", encoding="UTF-8") as file:
        file.write(f"{bookcount},{book},global,negative,{int(gtotalnegativewords*len(booktext.split()))},{gtotalnegativewords}\n")
        file.write(f"{bookcount},{book},global,neutral,{int(gtotalneutralwords*len(booktext.split()))},{gtotalneutralwords}\n")
        file.write(f"{bookcount},{book},global,positive,{int(gtotalnegativewords*len(booktext.split()))},{gtotalpositivewords}\n")
        file.write(f"{bookcount},{book},global,compound,,{gtotalcompound}\n")
        for item in sent_list:
            file.write(item)
    #//endregion


#Run the Graph Maker program
subprocess.run(["python", "Graph_Maker_Plot.py"])
subprocess.run(["python", "Graph_Maker_Bars.py"])
subprocess.run(["python", "Graph_Maker_Radar.py"])