d = dict()

def scrab(word):
    w=0
    d={'e':1,'a':1,'i':1,'o':1,'n':1,'r':1,'t':1,'l':1,'s':1,'u':2,'d':2,'g':2,'b':3,'c':3,'m':3,'p':3,'f':4,'h':4,'v':4,'w':4,'y':4,'k':5,'j':8,'x':8,'q':10,'z':10,'\n':0}
    l=len(word)
    w=sum([d[i] for i in word])
    return w/l







 
    
    




