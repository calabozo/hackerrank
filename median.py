# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 12:26:12 2016

@author: jose
"""

def main():
    n = raw_input()
    v = [int(x) for x in raw_input().strip().split(" ")]
    print getMedian(v)


    
def getMedian(v):
    m=v[int(len(v)/2)]
    vs_1=[]
    vs_2=[]
    vs_3=[]
    for i in xrange(0,len(v)):
        if v[i]<m:
            vs_1.append(v[i])
        elif v[i]==m:
            vs_2.append(v[i])
        else:
            vs_3.append(v[i])    
    vs_1.extend(vs_2)
    vs_1.extend(vs_3)
    
    if m==vs_1[int(len(vs_1)/2)]:
        return m
    else:
        return getMedian(vs_1)
    

if __name__ == "__main__":
    main()