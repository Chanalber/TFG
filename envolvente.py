#!/usr/bin/env python
# coding: utf-8

# In[34]:


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

df=pd.read_table("table8.txt")
df=pd.DataFrame(df)
df.columns

t=df['# t (s)']#.iloc[0:1000]
mx=df['mx ()']#.iloc[0:1000]

g1=plt.plot(t,mx,color='black')
plt.show(g1)

#código para obtener la envolvente
def hl_envelopes_idx(mx,dmin,dmax): #código para la envolvente
    """
    s : 1d-array, data signal from which to extract high and low envelopes
    dmin, dmax : int, size of chunks, use this if size of data is too big
    """

    # locals min      
    lmin = (np.diff(np.sign(np.diff(mx))) > 0).nonzero()[0] + 1 
    # locals max
    lmax = (np.diff(np.sign(np.diff(mx))) < 0).nonzero()[0] + 1 

    """
    # the following might help in some case by cutting the signal in "half"
    s_mid = np.mean(s) (0 if s centered or more generally mean of signal)
    # pre-sort of locals min based on sign 
    lmin = lmin[s[lmin]<s_mid]
    # pre-sort of local max based on sign 
    lmax = lmax[s[lmax]>s_mid]
    """

    # global max of dmax-chunks of locals max 
    lmin = lmin[[i+np.argmin(mx[lmin[i:i+dmin]]) for i in range(0,len(lmin),dmin)]]
    # global min of dmin-chunks of locals min 
    lmax = lmax[[i+np.argmax(mx[lmax[i:i+dmax]]) for i in range(0,len(lmax),dmax)]]

    return lmin,lmax

fig = plt.figure()
ax = fig.add_subplot(111)

high_idx, low_idx = hl_envelopes_idx(mx,dmin=400,dmax=400)

#plt.plot(t[high_idx], mx[high_idx], 'r', label='low') #envolvente inferior
g2=ax.plot(t[low_idx], mx[low_idx], 'g', label='high') #envolvente superior
ax.xaxis.set_major_formatter(mtick.FormatStrFormatter('%.e')) # para poner el eje x en notación científica

plt.xlabel('t (s)')
plt.ylabel('$<M_{x}>/M_{s}$')
plt.title('Envolvente superior de la magnetización en el eje x')
plt.show(g2)


# In[ ]:




