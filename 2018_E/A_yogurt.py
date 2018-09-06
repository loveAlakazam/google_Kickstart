# https://code.google.com/codejam/contest/4394486/dashboard#s=p0
# -*- coding: utf-8 -*-
import os
import sys
#practice_dir=os.path.dirname("C:/Users/USER/Desktop/CodeJam/2018_KICK_E/yogurt/")
def largestDrinkDay(N,K, expires):
    #루시가 요거트를 먹은 전체횟수
    eat_count=0

    #expires는 N개의 요거트들의 오늘로부터 남은 유통기한 데이터
    while len(expires)>0:
        
        #루시는 하루 최대 K개의 요거트를 먹는다.
        for i in range(K):
            #가장짧은 유통기한을 갖는 데이터를 찾는다.
            shortest=min(expires)
            #가장짧은 유통기한을 갖는 요거트를 먹는다.
            expires.remove(shortest)
            eat_count+=1

        #하루가 지났다.
        #expires의 모든 유통기한이 하루씩 감소
        expires=[e-1 for e in expires if e-1!=0]    

    return eat_count

    
def main():
    #입력파일
    #practice_file= os.path.join(practice_dir,'A-small-practice.in')
    #file_read=open(practice_file)
    file_read=open('A-small-practice.in','r')

    #출력파일
    file_result=open('A_answer.txt','w')
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
        print('\nexpires\n',expires)
        result=largestDrinkDay(N,K, expires)
        file_result.write('Case #{}: {}\n'.format(t+1,result))
        
if __name__=='__main__':
    main()
