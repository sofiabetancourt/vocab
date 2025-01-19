#This is to study for vocab tests
#To run it just click on the green button above

import random

def menu():
    level = -1 
    while level != 0:  
        print("Choose a level:")
        print("Level 1: Easy  || Level 2: Intermediate || Level 3: Hard  || Level 4: All words || Level 5: Sentences ")
        level = int(input("Enter the level number: "))
        
        if level == 1:
            level_1()
            
        elif level == 2:
            level_2()
            
        elif level == 3:
            level_3()
            
        elif level == 4:
            level_4()
            
        elif level == 5:
            level_5()
            
def quiz(vocab_words):
    
    score = 0
    
    words = list(vocab_words.keys())
    random.shuffle(words)
    
    
    while words:
        word = words.pop()
        user_input = input(f"Write '{word}' in Korean: ")
        
        if user_input == vocab_words[word]:
            print("Correct!")
            score+=1
        else:
            print("Incorrect")
    
            
    print(f"Your final score is {score}/{len(vocab_words)}.")        
        
def level_1():
    
    vocab_1 = {
        "foot/feet": "발", "travel": "여행", "coat": "코트", "panda": "판다",
        "to be cold/feel cold (weather)": "춥다", "to be easy": "쉽다", "to wear": "입다", "bear": "곰",
        "season": "계절", "pencil": "연필" , "ball-point pen": "볼펜", "grapes": "포도",
        "photo/picture": "사진", "river": "강", "Busan": "부산", "road": "길",
        "Jeju Island": "제주도", "ship/boat": "배", "train": "기차", "new": "새",
        "speech/language": "말", "writings": "글", "mind": "마음", "jazz": "재즈",
        "semester/term": "학기", "legs": "다리", "baby": "아기", "police/policeman" : "경찰" , "athlete" : "선수",
        "temperature" : "온도", "air conditioner" : "에어콘" , "ribs" : "갈비",  "jogging" : "조깅" ,
        "music" : "음악",  "classical music" : "클래식"}
    
    quiz(vocab_1)
    
    
def level_2():
    
   vocab_2 = {
    "repeatedly": "자꾸", "to be close": "가깝다", "to be hot/to feel hot (weather)": "덥다",
    "to be cold, icy (at touch)": "차갑다", "to be hot (at touch)": "뜨겁다", "to be cute": "귀엽다",
    "to be difficult": "어렵다", "to be spicy/hot": "맵다", "to be thankful/grateful": "고맙다",
    "to be heavy": "무겁다", "to be light": "가볍다", "to be scary": "무섭다",
    "to be longed for/to miss <someone>": "그립다", "to be enjoyable/pleasant": "즐겁다",
    "to be dirty": "더럽다", "to grill/bake/toast": "굽다", "to be fine/pretty": "곱다",
    "to help": "돕다", "to be narrow": "좁다", "to appear, to happen, to occur, to take place": "생기다",
    "to burn": "태우다", "outdoor": "야외", "activity": "활동", "inspection/test": "검사",
    "long time": "오래", "driving": "운전", "bicycle": "자전거", "airplane": "비행기",
    "cold/flu": "감기", "other": "다른", "to borrow": "빌리다", "to walk": "걷다",
    "to ask": "묻다", "to hear": "듣다", "to be late": "늦다", "lie": "거짓말",
    "reply": "답장", "title": "제목", "memory": "기억", "of course": "그럼요",
    "nightgown/pajama": "잠옷", "to get wet": "젖다", "monster": "괴물", "prince": "왕자님",
    "course": "과목", "to be burnt": "타다", "grade; (school) record": "성적",
    "gym/sports complex": "체육관", "regards": "안부", "to transmit": "전하다",
    "to jog": "조깅하다", "directly": "바로" , "to know" : "알다", "cellphone" : "휴대폰"}
   
   quiz(vocab_2)

    
def level_3():
   
   vocab_3 = {
    "to remember": "생각이 나다", "intersection": "네거리", "crossroads": "사거리", "ok/sure/certainly": "알겠습니다",
    "to be beautiful": "아름답다", "to earn money": "돈을 벌다", "to bloom": "꽃이 피다",
    "to be careful": "조심하다", "to drive": "운전하다", "slowly": "천천히",
    "to ask (a favor)": "부탁하다", "to catch a cold": "감기에 걸리다", "ginseng tea": "인삼차",
    "ginger tea": "생강차", "to lose weight": "살을 빼다", "to take a picture": "사진을 찍다",
    "to repeat after someone": "따라하다", "to swim": "수영하다",
    "to be great": "대단하다", "to remember (memory)": "기억하다",
    "to change, to exchange": "바꾸다", "to change (socks, shoes)": "갈아신다", "to change (clothes)": "갈아입다",
    "to transform": "변하다", "express": "표현하다", "to teach": "가르치다", "cold noodle dish": "냉면",
    "to say hello to": "안부를 전하다", "beef": "소고기",
    "to gather/collect/save": "모으다", "to be noisy": "시끄럽다" }
   
   quiz(vocab_3)

    
def level_4():
    
    vocab_4 = {
    "foot/feet": "발", "travel": "여행", "coat": "코트", "panda": "판다",
    "to be cold/feel cold (weather)": "춥다", "to be easy": "쉽다", "to wear": "입다", "bear": "곰",
    "season": "계절", "pencil": "연필", "ball-point pen": "볼펜", "grapes": "포도",
    "photo/picture": "사진", "river": "강", "Busan": "부산", "road": "길",
    "Jeju Island": "제주도", "ship/boat": "배", "train": "기차", "new": "새",
    "speech/language": "말", "writings": "글", "mind": "마음", "jazz": "재즈",
    "semester/term": "학기", "legs": "다리", "baby": "아기", "police/policeman": "경찰", "athlete": "선수",
    "temperature": "온도", "air conditioner": "에어콘", "ribs": "갈비", "jogging": "조깅",
    "music": "음악", "classical music": "클래식",
    "repeatedly": "자꾸", "to be close": "가깝다", "to be hot/to feel hot (weather)": "덥다",
    "to be cold, icy (at touch)": "차갑다", "to be hot (at touch)": "뜨겁다", "to be cute": "귀엽다",
    "to be difficult": "어렵다", "to be spicy/hot": "맵다", "to be thankful/grateful": "고맙다",
    "to be heavy": "무겁다", "to be light": "가볍다", "to be scary": "무섭다",
    "to be longed for/to miss <someone>": "그립다", "to be enjoyable/pleasant": "즐겁다",
    "to be dirty": "더럽다", "to grill/bake/toast": "굽다", "to be fine/pretty": "곱다",
    "to help": "돕다", "to be narrow": "좁다", "to appear, to happen, to occur, to take place": "생기다",
    "to burn": "태우다", "outdoor": "야외", "activity": "활동", "inspection/test": "검사",
    "long time": "오래", "driving": "운전", "bicycle": "자전거", "airplane": "비행기",
    "cold/flu": "감기", "other": "다른", "to borrow": "빌리다", "to walk": "걷다",
    "to ask": "묻다", "to hear": "듣다", "to be late": "늦다", "lie": "거짓말",
    "reply": "답장", "title": "제목", "memory": "기억", "of course": "그럼요",
    "nightgown/pajama": "잠옷", "to get wet": "젖다", "monster": "괴물", "prince": "왕자님",
    "course": "과목", "to be burnt": "타다", "grade; (school) record": "성적",
    "gym/sports complex": "체육관", "regards": "안부", "to transmit": "전하다",
    "to jog": "조깅하다", "directly": "바로", "to know": "알다", "cellphone": "휴대폰",
    "to remember": "생각이 나다", "intersection": "네거리", "crossroads": "사거리", "ok/sure/certainly": "알겠습니다",
    "to be beautiful": "아름답다", "to earn money": "돈을 벌다", "to bloom": "꽃이 피다",
    "to be careful": "조심하다", "to drive": "운전하다", "slowly": "천천히",
    "to ask (a favor)": "부탁하다", "to catch a cold": "감기에 걸리다", "ginseng tea": "인삼차",
    "ginger tea": "생강차", "to lose weight": "살을 빼다", "to take a picture": "사진을 찍다",
    "to repeat after someone": "따라하다", "to swim": "수영하다",
    "to be great": "대단하다", "to remember (memory)": "기억하다",
    "to change, to exchange": "바꾸다", "to change (socks, shoes)": "갈아신다", "to change (clothes)": "갈아입다",
    "to transform": "변하다", "express": "표현하다", "to teach": "가르치다", "cold noodle dish": "냉면",
    "to say hello to": "안부를 전하다", "beef": "소고기",
    "to gather/collect/save": "모으다", "to be noisy": "시끄럽다"}
     
    quiz(vocab_4)

    
def level_5():
    
    vocab_5 = {
    "I only go home on weekends to see my family": "주말에만 식구들 보러 집에 가요",
    "It only takes five minutes to walk to school, but I'm late for class every day": "걸어서 학교까지 5분밖에 안 걸리지만 매일 수업에 늦어요",
    "My house is not very far": "우리 집은 별로 안 멀어요",
    "I exchange Canadian money for Korean money": "캐나다 돈을 한국 돈으로 바꿔요",
    "Please write your name with a ballpoint pen": "볼펜으로 이름을 쓰세요",
    "Juice or tea is good for a cold": "감기에는 주스나 차가 좋아요",
    "Ted went to Busan to hang out with his friends": "테드는 부산에 친구들이랑 놀러 갔어요",
    "Korean is easy right?": "한국말 쉽지요?"}
    
    quiz(vocab_5)
    
menu()
    
































#This is a random comment