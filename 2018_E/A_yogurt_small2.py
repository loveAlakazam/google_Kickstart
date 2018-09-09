# small-data-set만 correct받음...
# https://code.google.com/codejam/contest/4394486/dashboard#s=p0
# -*- coding: utf-8 -*-
import os
import sys
#practice_dir=os.path.dirname("C:/Users/USER/Desktop/CodeJam/2018_KICK_E/yogurt/")
def after_day(expires):
    for i in range(len(expires)):
        if expires[i]==0:#유통기간이 지났다.(그대로 둔다)
            expires[i]=0
        elif expires[i]==-1:#루시가 이미 먹었다.(그대로 둔다)
            expires[i]=-1
        else:#아직 먹지 않고, 유통기한이 남은 요거
            expires[i]-=1 #하루가 지났으니까 1을 뺀다.
    return expires

def shortest_expire(expires):
    #expires의 원소들중 -1, 0이 아닌 값들을 추출한다.
    not_eaten_expired=[x for x in expires if (x!=0 and x!=-1)]
    if len(not_eaten_expired)==0: #모든 원소가 0과 -1이라서 이외의 가장작은 수를 찾을수 없는 경우
        return None
    else:
        return min(not_eaten_expired)

def largestDrinkDay(N,K, expires):
    #루시가 요거트를 먹은 전체횟수
    #요거트를 먹으면 expries[i] =-1 이다.

    #N==K 인 경우에는 하루에 N개 모두 먹은거나 다름없다.
    if N==K:
        return N
    
    for days in range(N):#N일
        i=0 #현재요거트 번호 (초기화)
        count=0 #루시가 요거트를 먹는횟수 카운트(아래 while반복문 카운트이기도하다)
        shortest= shortest_expire(expires)
        if shortest!=None:
            while i<N and count<K:#i는 현재 요거트이며(i=0~N-1), K는 루시가 하루에 요거트를 먹는 최대량
                if (expires[i]!=0 and expires[i]!=-1): #먹을 수 있는 요거트
                    #유통기한이 가장짧은 것부터 먹는다.
                    if expires[i]==shortest:
                        expires[i]=-1 #먹는다.
                        count+=1 #요거트 먹는 횟수 증가
                i+=1 #다음요거트로 넘어감.
            
            #하루가 지났다.
            expires=after_day(expires)
    
        
    eat_count=expires.count(-1) #루시가 먹은 건 expires[i]=-1이므로 expires가 -1인 원소의 개수이다.
    return eat_count

    
def main():
    #입력파일
    #practice_file= os.path.join(practice_dir,'A-small-practice.in')
    #file_read=open(practice_file)
    file_read=open('A-large-practice.in','r')

    #출력파일
    file_result=open('A_answer_large.txt','w')
    cases= int(file_read.readline()) #testcase

    '''
    N: 전체 요거트 개수
    K: 하루에 루시가 최대로 먹을 수 있는 요거트 개수
    '''
    for t in range(cases):
        #N, K를 추출
        
        s= file_read.readline()
        N,K=[int(x) for x in s.split(' ')]

        #N개의 요거트 유통기한 데이터를 추출(i번째 요거트의 유통기한 Ai와 같은 데이터가 저장)
        expires=[int(x) for x in file_read.readline().split(' ')]
        result=largestDrinkDay(N,K, expires)
        print('#',t,': ',result)
        file_result.write('Case #{}: {}\n'.format(t+1,result))
        

if __name__=='__main__':
    main()
