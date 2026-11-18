import numpy as np
from midiutil import MIDIFile
exec(open('/home/ayum/projects/pendulum/p.py').read().split('out=')[0])
sc=[0,2,3,5,7,8,10]
def deg(a,lo,n=14): # angle -> scale degree
    return int(((a+np.pi)%(2*np.pi))/(2*np.pi)*n)
def note(d,base): return base+12*(d//7)+sc[d%7]
m=MIDIFile(3);m.addTempo(0,0,132)
for tr,(prog) in enumerate([11,48,32]): m.addProgramChange(tr,tr,0,prog)
dt=0.005
for voice,(a0,tr,base) in enumerate([(2.0,0,57),(2.0001,1,57)]):
    s=np.array([a0,a0,0,0.]);t=0;last=None
    for i in range(64):
        for _ in range(100):
            k1=f(s);k2=f(s+dt/2*k1);k3=f(s+dt/2*k2);k4=f(s+dt*k3);s=s+dt/6*(k1+2*k2+2*k3+k4)
        n=note(deg(s[1],0),base)
        m.addNote(tr,tr,n,i*0.5+ (voice*0.25),0.5 if tr==0 else 1.0,80 if tr==0 else 60)
# bass pedal A and E, slow
for b in range(16): m.addNote(2,2,[33,40,33,38][b%4],b*2,2,70)
m.writeFile(open('pm.mid','wb'))
