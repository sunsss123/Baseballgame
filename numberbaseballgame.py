import random
import math

# 랜덤으로 정답 생성
# answer = random.sample(range(1,10),4)
# print("정답은=", answer)

# 초기화
cnt = 0
guess = [] #입력값을 배열로 저장
strikecnt = 0 #스트라이크 횟수

isPlayer1 = True #플레이어 1이 게임중
isPlayer2 = False #플레이어 2는 참여불가

player1Base = 0 #플레이어1의 베이스위치
player2Base = 0 #플레이어2의 베이스위치

tmpPlayer1Ball = 0 #플레이어1의 누적 볼 수
tmpPlayer2Ball = 0 #플레이어2의 누적 볼 수

cntPlayer1 = 0 #플레이어1의 점수 카운트
cntPlayer2 = 0 #플레이어2의 점수 카운트

# 게임진행
while cntPlayer1 < 3 and cntPlayer2 < 3:
    strikecnt = 0
    ballcnt = 0
    guess = []

    answer = random.sample(range(1, 10), 4)
    #print("정답은=", answer) #원만한 게임진행을 위한 출력문 주석처리

    for i in range(4):
        input_num = int(input("{}, 1~9까지 숫자를 입력하세요:".format(i)))
        guess.append(input_num)

    for i in range(4):
        if guess[i] == answer[i]:
            strikecnt = strikecnt + 1
        elif guess[i] in answer:
            ballcnt += 1

    print("strike = {}, ball = {}".format(strikecnt, ballcnt))

    if isPlayer1 == True: #플레이어1의 게임진행
        if tmpPlayer1Ball + ballcnt > 0 or strikecnt > 0:
            if (tmpPlayer1Ball + ballcnt) / 4 > 0:
                player1Base = player1Base + math.trunc((tmpPlayer1Ball + ballcnt) / 4)
                # print("베이스1 : {}".format(player1Base))
                tmpPlayer1Ball = (tmpPlayer1Ball + ballcnt) % 4
            if strikecnt > 0:
                player1Base = player1Base + strikecnt
                # print("베이스2 : {}".format(player1Base))
            if player1Base >= 4:
                cntPlayer1 = cntPlayer1 + math.trunc(player1Base / 4)
                player1Base = player1Base % 4
                # print("베이스3 : {}".format(player1Base))

        print("Player1 -> 베이스 = {:g}, 스트라이크 = {:g}, 볼 = {:g}, stack_볼 = {:g},  점수 = {:g}".format(player1Base, strikecnt,
                                                                                                 ballcnt,
                                                                                                 tmpPlayer1Ball,
                                                                                                 cntPlayer1))
        isPlayer1 = False #플레이어1 게임 참여불가 상태
        isPlayer2 = True #플레이어2 게임진행

    elif isPlayer2 == True: #플레이어2
        if tmpPlayer2Ball + ballcnt > 0 or strikecnt > 0:
            if (tmpPlayer2Ball + ballcnt) / 4 > 0:
                player2Base = player2Base + math.trunc((tmpPlayer2Ball + ballcnt) / 4)
                # print("베이스1 : {}".format(player1Base))
                tmpPlayer2Ball = (tmpPlayer2Ball + ballcnt) % 4
            if strikecnt > 0:
                player2Base = player2Base + strikecnt
                # print("베이스2 : {}".format(player1Base))
            if player2Base >= 4:
                cntPlayer2 = cntPlayer2 + math.trunc(player2Base / 4)
                player2Base = player2Base % 4
                # print("베이스3 : {}".format(player1Base))

        print("Player2 -> 베이스 = {:g}, 스트라이크 = {:g}, 볼 = {:g}, stack_볼 = {:g},  점수 = {:g}".format(player2Base, strikecnt,
                                                                                                 ballcnt,
                                                                                                 tmpPlayer2Ball,
                                                                                                 cntPlayer2))
        isPlayer1 = True #플레이어1 게임진행
        isPlayer2 = False #플레이어2 게임 참여불가 상태

    if cntPlayer1 == 3:
        print("player1이 승리하였습니다.")
    elif cntPlayer2 == 3:
        print("player2가 승리하였습니다.")

