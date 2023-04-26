import codecs
import os
import sys
from shutil import copyfile


def check_guided_alignment(SLcorpus,TLcorpus,weightsFile,forwardalignment):
    copyfile(SLcorpus,"slcorpustemp.txt")
    copyfile(TLcorpus,"tlcorpustemp.txt")
    copyfile(weightsFile,"weightsFiletemp.txt")
    copyfile(forwardalignment,"forwardalignmenttemp.txt")
    
    slcorpus=codecs.open("slcorpustemp.txt","r",encoding="utf-8")
    tlcorpus=codecs.open("tlcorpustemp.txt","r",encoding="utf-8")
    weightsfile=codecs.open("weightsFiletemp.txt","r",encoding="utf-8")
    alignforward=codecs.open("forwardalignmenttemp.txt","r",encoding="utf-8")


    slcorpusmod=codecs.open(SLcorpus,"w",encoding="utf-8")
    tlcorpusmod=codecs.open(TLcorpus,"w",encoding="utf-8")
    weightsFilemod=codecs.open(weightsFile,"w",encoding="utf-8")
    alignforwardmod=codecs.open(forwardalignment,"w",encoding="utf-8")
    
    
    
    
    cont=0
    while 1:
        cont+=1
        liniaSL=slcorpus.readline().rstrip()
        if not liniaSL:
            break
        liniaTL=tlcorpus.readline().rstrip()
        liniaweights=weightsfile.readline().rstrip()
        liniaalignforward=alignforward.readline().rstrip()

        tokensSL=liniaSL.split(" ")
        tokensTL=liniaTL.split(" ")
        tokensAlignForward=liniaalignforward.split(" ")
        
        towrite=True
        for token in tokensAlignForward:
            camps=token.split("-")
            if not len(camps)==2:
                print("ERROR",cont)
                towrite=False
        
        if towrite:
            slcorpusmod.write(liniaSL+"\n")
            tlcorpusmod.write(liniaTL+"\n")
            weightsFilemod.write(liniaweights+"\n")
            alignforwardmod.write(liniaalignforward+"\n")
    
    os.remove("slcorpustemp.txt")
    os.remove("tlcorpustemp.txt")
    #os.remove("weightsFiletemp.txt")
    os.remove("forwardalignmenttemp.txt")
    
if __name__ == "__main__":
    SLcorpus=sys.argv[1]
    TLcorpus=sys.argv[2]
    forwardalignment=sys.argv[3]
    reversealignment=sys.argv[4]
    check_guided_alignment(SLcorpus,TLcorpus,forwardalignment,reversealignment)
