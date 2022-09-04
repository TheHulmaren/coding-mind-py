'''
"파이썬으로 배우는 코딩마인드"
강의자: 이규민

[최종시험]

시험 시간: 6월 13일 15:30 - 18:00

응시자: 2명

총점: 100점

안내:
    1. 구글링 및 기타 자료검색은 허용됩니다.
        단, 제 3자의 직접적인 도움을 받아선 안되며, 피수험인 간의 의견 교환도 금지됩니다.
        이를 어길 시 0점 처리됩니다.
        
    2. 답안은 되도록 아래의 양식에 맞추어 작성해 주십시오.
    
    3. 문항이 요구하는 바를 정확히 파악하여 풀어야 합니다. 
        문제의 조건을 벗어나거나, 사용이 허가되지 않은 외부 라이브러리를 이용하면 감점 대상입니다.
        
    4. 대부분의 문항에는 부분 점수가 존재합니다.
    
    5. 답안 제출시에는 *.py 형태의 파일을 rbalsdldi9@gmail.com 으로 보냅니다.
        
    6. 문항의 점수와 난도는 반드시 비례하지는 않습니다.
    
'''



'''
1. (부분점수 있음)(10점)

파이썬의 상속 기능을 어떤 상황에 사용하면 편리할지 예시를 두가지 들어보시오.

'''










'''
2. (부분점수 있음)(15점)

정수를 매개변수로 받아 아래와 같이 정수만큼의 층수를 가진 피라미드를 출력하는 함수를 작성하시오.

함수의 이름은 great_pyramid 로 한다.

예 1:
    입력 매개변수: 5
    
    콘솔창 출력:
            ^
           /_\
          /___\
         /_____\
        /_______\
   
     
    
예 2:
    입력 매개변수: 3
    
    콘솔창 출력: 
          ^
         /_\
        /___\
   


'''


def great_pyramid(num):
    for i in range(num):
        if i == 0:
            print(' '*(num-1) + '^')
        else:
            print(' '*(num-1-i)+'/' + '_'*(1+2*(i-1)) + '\\')
            
great_pyramid(5)

great_pyramid(8)





'''
3. (부분점수 있음)(20점)

문자열의 배열을 받아 각 문자열이 등장하는 횟수를 세어서 아래의 예와 같이 dictionary 를 반환하는 함수를 작성하시오.

함수의 이름은 count_words 로 하고, 매개변수로는 문자열의 배열만을 받는다.


예:
    입력 매개변수: ['Apple', 'Banana', 'Avocado', 'Banana', 'Apple']
    
    반환: {'Apple': 2, 'Banana': 2, 'Avocado': 1}

'''


def count_words(words):
    word_set = set(words)
    
    result = dict()
    
    for word in list(word_set):
        result[word] = words.count(word)
        
    return result

print(count_words(['Apple', 'Banana', 'Avocado', 'Banana', 'Apple']))




def count_words_2(words):
    temp = []
    
    result = dict()
    
    for word in words:
        if word in temp:
            result[word] += 1
        else:
            result[word] = 1
            temp.append(word)
            
    return result

print(count_words_2(['Apple', 'Banana', 'Avocado', 'Banana', 'Apple']))




'''
4. (부분점수 있음)(20점)

주어진 문자열이 palindrome 인지를 판별하는 함수를 작성하시오.


예:
    입력 매개변수: 'able was I ere I saw elba'
    
    반환: True


'''







'''
5. (부분점수 있음)(35점)


순차적으로 맞물린 톱니바퀴의 회전을 시뮬레이션하는 기어박스 클래스(GearBox)를 만들고자 한다.

각 톱니바퀴의 가장 상단에 있는 톱니에는 어떤 표시를 해놓는다고 가정한다.


아래의 설계 지시에 따라 클래스를 작성하시오:
    1. __init__(self, title, gears):
        title(string): 기어박스의 이름을 지정해준다.
        gears(list<float>): 각 톱니바퀴의 반지름을 맞물리는 순서대로 입력해준다.
        
    2. spin(self, degree):
        degree(float): 해당 횟수만큼 첫번째 톱니바퀴를 회전시킨다.
                        예를들어, 입력값이 1.5 라면 1.5번 회전시킨다.
                        
                        기존의 회전값이 있으면 입력값 만큼 추가한다.
                        
    3. last_gear(self):
        초기 상태에서 현재까지 누적된 회전수 만큼 회전했을때,
        마지막 톱니바퀴가 몇번 회전하게 되는지를 float 타입으로 반환하시오.
        
    4. all_gear(self):
        초기 상태에서 현재까지 누적된 회전수 만큼 회전했을때,
        각 톱니바퀴가 몇번 회전하게 되는지를 list<float> 타입으로 반환하시오.
        
        
    5. __str__(self):
        초기 상태에서 현재까지 누적된 회전수 만큼 회전했을때,
        각 톱니바퀴의 맨 위에 있던 표식이 최종적으로 어느 지점에 위치하게 되는지를 string 타입으로 반환하시오.
        표식의 위치는 0이상 1미만의 값을 가지며,
        0인 경우 제자리(맨위)라는 뜻이고,
        예를들어 0.5 라면 180도 회전한 위치에 있다는 뜻이다.
        
        예:
            '<KyuminBox -> 0.5:0.7:0.1:0.9>'
        

'''

class GearBox:
    def __init__(self, title, gears):
        self.title = title
        self.gears = gears
        

kyumin = GearBox('KyuminBox', [1,2,5,1,234])














