import sys
import random
class baseballgame_2():
    def newNumber(self):
        newNumber = random.sample(range(1, 10), 4)
        return newNumber

    def checkValue(newNumber):


        # 초기화
        cnt = 0
        guess = []
        strikecnt = 0

        strikecnt = 0
        ballcnt = 0
        guess = []
        for i in range(3):
            num = int(input("{}, 1~9까지 숫자를 입력하세요:".format(i)))
            guess.append(num)

            print(guess)

        for i in range(3):
            if guess[i] == newNumber[i]:
                strikecnt = strikecnt + 1
            elif guess[i] in newNumber:
                ballcnt += 1
        # print("strike = {}, ball = {}".format(strikecnt, ballcnt))

        cnt += 1


    # # 랜덤으로 정답 생성
    # answer = random.sample(range(1,10),3)
    # print("정답은=", answer)



    # # 게임진행
    # while strikecnt <3:
    #     strikecnt = 0
    #     ballcnt = 0
    #     guess = []
    #     for i in range(3):
    #         num = int(input("{}, 1~9까지 숫자를 입력하세요:".format(i)))
    #         guess.append(num)
    #
    #         print(guess)
    #
    #     for i in range(3):
    #         if guess[i] == answer[i]:
    #             strikecnt = strikecnt + 1
    #         elif guess[i] in answer:
    #             ballcnt +=1
    #     print("strike = {}, ball = {}".format(strikecnt, ballcnt))
    #
    #     cnt +=1
    #
    #
    # print("{}번 만에 정답".format(cnt))
