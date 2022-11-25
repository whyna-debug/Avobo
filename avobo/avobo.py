# Created by Wahyuna
# https://github.com/wahyunaa/avobo

import random
import os
import items
import r

if True:
    gt_items = items.r_items
    vXf = items.vFo
    bomb = items.bomb
    bn,vxF = True,0
    
    items,iNm = [],[]
    for seltms in range(10):
        nF = random.randint(0,len(gt_items)-1)
        items.append(gt_items[nF])
        gt_items.pop(nF)
    vF_x = random.randint(1,9)
    items[vF_x] = bomb
    iNrX = items
    def lc():
        # Choice
        tX,vXfm = "",3
        for nVo in range(1,10):
            tX += vXf[nVo]
            if nVo == vXfm:
                tX += "\n"
                vXfm += 3
        return tX
    print(r.yl)
    def system_cls():
        os.system("clear")
    system_cls()
    print("Choose a number\n")
    # Finds the index of an item
    def sr(Ln):
        nR = "0"
        fVz = True
        for x in range(1,10):
            if  fVz:
                if iNrX[x] == Ln:
                    nR = x
                    fVz = False
        if nR == "0":
            nR = "\"{}\" Not found".format(Ln)
        return nR
    #print(sr("🍒"))

    # Start
    while bn:
        if vxF == 0:
            print(lc(),"\n")
            vxF += 1
    
        nm = input("Choose: ")
        nm = nm.strip()
        nm = "".join(filter(str.isdigit, nm))
        system_cls()
        if not nm  == "":
            if nm.isnumeric() and int(nm) > 0 and int(nm) < 10:
                nm = int(nm)
                if nm in iNm:
                    system_cls()
                    print("number 2 has been chosen!\nplease choose another number\n".format(nm))
                    print(lc(),"\n")
                    continue
                else:
                    print("You have chosen number {}\n". format (nm))
                    vXf[nm] = iNrX[nm]
                    iNm.append(nm)
                    iNrX[nm] = "i"
                    fo = ""
                    if vXf[nm] == bomb and iNrX.count("i") <= 8:
                        fo = "You lose!\nNumber {} is a {}".format(nm, bomb)
                        bn = False
                    elif iNrX.count("i") == 8 and not vXf.__contains__(bomb): 
                        fo = "You win!\nNumber {} is a {}".format(vF_x,bomb)
                        bn = False
                    print(lc())
                    print(fo)
            else:
                system_cls()
                print("Choose a number from 1 to 9\n")
                print(lc(),"\n")
        else:
            print("Enter the number you want to choose!\n\n{}\n".format(lc()))
    input("\n\n")
