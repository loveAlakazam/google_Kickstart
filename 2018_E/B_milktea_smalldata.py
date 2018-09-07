# https://code.google.com/codejam/contest/4394486/dashboard#s=p1
def find_lowest_complain(N,M,P, friends_prefer, forbidden_list):
    #1. 옵션개수(P)에 대한 만들 수 있는 밀크티 가짓수를 만든다.
    # 옵션이 P개라면 만들 수있는 바이너리스트링 경우의수는 2**P이다.
    # 정수 0~2**P-1를 바이너리로 하고, 타입을 str로 변경한다.
    cases=[]
    for i in range(2**P):#0~2**P-1
        s= str(bin(i))[2:] #앞의 '0b'제외
        #글자수가 P개인 바이너스트링으로 바꾸기..
        if len(s)<P:
            for i in range(P-len(s)):#차이만큼 '0'추가
                s='0'+s
        cases.append(s)
    
    #2. P개에대한 모든 밀크티 경우의 수에서 forbidden_list에 해당하는
    # 바이너리 스트링은 제외시킨다.
    for i in forbidden_list:
        for j in cases:
            if i==j:
                cases.remove(j)

    #3. 나머지 바이너리 스트링으로 친구가 원하는 바이너리스트링과 비교하여
    # 각 바이너리 스트링으로 친구불평개수를 카운트하고 불평개수리스트에 담는다.
    # 각 바이너리 스트링에서 친구 불평개수를 저장하는 리스트: complains_list
    complains_list=[]
    for i in cases:#i는 shakti가 주문한거..(forbidden 밀크티 제외)
        complain_count=0 #초기화, count_complains리스트에 추가됨..
        for j in friends_prefer:
            #글자수가 P(옵션개수)으로 동일하므로 P개의 글자가 서로 같은지 확인.
            for c in range(P):
                if i[c]!=j[c]: #c번째 글자에서 서로 다르면 불평개수 증가
                    complain_count+=1
        #한메뉴에대한 N명의 친구들의 컴플레인 총합을 컴플레인리스트에 추가
        complains_list.append(complain_count)
    
    #4. 친구 불평개수가 가장 적은 것을 결과로 리턴한다.
    return min(complains_list)
    
def main():
    #읽기모드로 practice파일을 연다
    file_read=open('B-small-practice.in','r')
    
    #쓰기모드로 b_result_small.txt를 생성 및 연다
    file_write=open('b_result_small.txt','w')
    
    #test case읽기 & 타입전환(str->int)
    case= int(file_read.readline()) 

    for t in range(case):
        
        #N:친구수, M:판매불가 티개수, P:옵션개수
        s = file_read.readline()
        N,M,P= [ int(x) for x in s.split(' ')]
        
        #친구들이 원하는 밀크티 바이너리 리스트
        friends_prefer=[]

        #친구수(N)만큼 친구가 원하는 밀크티 바이너리 스트링을 리스트에 추가.
        #'\n'문자를 제거해야됨.
        for i in range(N):
            friends_prefer.append(file_read.readline().strip())

        #print('friends_prefer: ',friends_prefer)

        #판매불가 티 바이너리 리스트
        forbidden_list=[]

        #판매불가 티개수(M)만큼 판매불가 밀크티 바이너리 스트링을 리스트에 추가
        #'\n'문자를 제거해야됨.
        for i in range(M):
            forbidden_list.append(file_read.readline().strip())

        #print('forbidden_list: ',forbidden_list)
        #최소 컴플레인 개수 구하기
        result=find_lowest_complain(N,M,P, friends_prefer, forbidden_list)

        #출력파일에 결과출력
        print('#',t+1,': ',result)
        file_write.write('Case #{}: {}\n'.format(t+1,result))
        
        
if __name__=='__main__':
    main()
