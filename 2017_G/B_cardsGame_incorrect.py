def xor_total(n,redNumber,blueNumber):
    #n=cardsNum-1
    #xor_case는 서로 다른 카드가 xor연산 한 모든 결과들을 나타낸다..
    xor_case=[]
    
    #연산결과의 리스트를 만든다.
    for r in range(len(redNumber)):
        for b in range(len(blueNumber)):
            if r !=b:
                xor_case.append(redNumber[r]^blueNumber[b])

    #연산결과의 리스트에서 cardNumber-1개를 뽑아서 최소의 합을 만든다.
    min_total=0
    for i in range(n):#최소의 원소를 고르는 횟수(cardsNum-1)
        min_total+= min(xor_case)
        xor_case.remove(min(xor_case))
        
    return min_total

def main():
    #읽기 모드로 B-small-practice.in 파일을 연다.
    read_file=open("B-small-practice.in","r")

    #쓰기모드로 결과파일을 미리 만들어놓는다.
    '''
        파일이 존재하지 않으면 파일을 생성하여, write()함수가 있다면
        생성시킨 파일안에 내용 기재.
        그러나 기존에 파일이 존재한다면, 기존의 내요을 지우고 새로쓴다
    '''
    result_file=open('result_b.txt','w')
    
    case=int(read_file.readline()) #100, str->int로 type변경
    #print('testCase: ', case)
    
    """
    cardsNum= read_file.readline()
    print('cardsNum: ',cardsNum)
    print('cardsNum type: ', type(cardsNum)) #<class 'str'>

    red1=read_file.readline()
    print('red1: ', red1) # 872031131 582064085 853700360 ...
    print('red1 type: ',type(red1)) #<class 'str'>

    #' '스페이스바를 기준으로 원소를구분하여, 문자열을 리스트로 변환
    #str은 split()을 이용하여 공백(' ')으로 나눠진 원소로하는 리스트로 변환
    reds=[ int(x) for x in red1.split()]

    print(reds)
    print(type(reds[1])) #<class 'int'>
    ========================================================================
    '''
    ex)
    문자열 10 11 12 를 원소가 int형인 리스트로 바꾸려면...
    red1="10 11 12" #type: str
    red1.split() => ['10', '11', '12'] #리스트로 바꼈지만, 원소는 str
    for i in range(len(red1)):
        red1[i]=int(red1[i])

    이것은
    red1=[ int(x) for x in red1.split()] 와 같다....
    '''    
    

    """
    
    for t in range(case): #0~99
        #박스에 있는 카드의 개수이다. str->int로 타입변환
        cardsNum= int(read_file.readline())
        print('cardsNum: ',cardsNum)
        
        #빨간색 숫자를 나타내는 리스트이다.
        redNumber=read_file.readline()
        redNumber=[int(x) for x in redNumber.split()]
        print('redNumber:',redNumber)
        
        #파란색 숫자를 나타내는 리스트이다.
        blueNumber=read_file.readline()
        blueNumber=[int(x) for x in blueNumber.split()]
        print('blueNumber:',blueNumber)

        '''
        카드가 n개가 있다면, 1장의카드에는 빨간숫자, 파란숫자가 존재하므로
        임의로 선택한 한장의 카드의 빨간숫자가 xor연산을 할 수 있는
        다른카드의 개수는 n-1개이다.
        '''
        result=xor_total(cardsNum-1, redNumber,blueNumber)
        print(t+1,': ',result)
        result_file.write('Case #{}: {}\n'.format(t+1,result))

    
if __name__=='__main__':
    main()

    



