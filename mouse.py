#coding=utf-8
import math

################
#      6
#  5       7
#
#4     *     0
#
#  3       1
#      2
################

ZERO = '443332222222222222222211100007776666666666666666655544'
ONE = '2' * 30
TWO = '6667770000000011122233333333333330000000000000'
THREE = '66777000000011122222333444400001112222333444444455566'
FOUR = '323232323232323230000000000222222222'
FIVE = '4444444444444222222222222227777000001111222223333444445555'
SIX = '444443434323332323222222222221111100000007777766666655555444444333333'
SEVEN = '000000000000003232332323222322322222222'
EIGHT = '55544443332222111111111122223334444555666677777777776666'
NINE = '66555544443333222211110000777766222223232322232232223222'

digits = [ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE]
unitVector = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]


# to unit
for v in unitVector:
    length = math.sqrt(v[0]**2 + v[1]**2)
    v[0] /= length
    v[1] /= length


def getDistance(word1, word2):
    len1 = len(word1)
    len2 = len(word2)
    size = max(len1, len2) + 1
    dp = []
    for i in xrange(size):
        temp = []
        for j in xrange(size):
            temp.append(0)
        dp.append(temp)
    for i in xrange(size):
        dp[i][0] = i
        dp[0][i] = i
    for i in xrange(1, len1+1):
        for j in xrange(1, len2+1):
            cost = 0
            if word1[i-1] != word2[j-1]:
                cost = 1
            exchangeCost = dp[i-1][j-1] + cost
            insertCost = dp[i][j-1] + 1
            deleteCost = dp[i-1][j] + 1
            dp[i][j] = min(exchangeCost, insertCost, deleteCost)
    return dp[len1][len2]

def getVectorNumber(vector):
    '''先转化成单位向量， 然后和10个标准的单位向量进行比较， 求出角度差最小的那个'''
    vector = [vector[1][0] - vector[0][0], vector[1][1] - vector[0][1]]
    length = math.sqrt(vector[0]**2 + vector[1]**2)
    vector[0] /= length
    vector[1] /= length

    min_dist = 10**8
    min_pos = -1

    for i in range(len(unitVector)):
        v = unitVector[i]
        dist = (v[0] - vector[0]) ** 2 + (v[1] - vector[1]) ** 2
        if min_dist > dist:
            min_dist = dist
            min_pos = i
    return min_pos
    

def verify(dataX, dataY):
    if len(dataX) < 30:
        print 'too small'
        return -1

    leastDistance = 10 ** 6
    min_pos = -1
    min_str = ''
    for i in xrange(10):
        step = float(len(dataX)) / len(digits[i])
        vector_str = ''
        lastX = dataX[0]
        lastY = dataY[0]
        nextPos = 0 + step
        for j in xrange(len(dataX)):
            if j >= nextPos:
                if dataX[j] == lastX:
                    # k = +-INF
                    if dataY[j] > lastY:
                        vector_str += '2'
                    else:
                        vector_str += '6'
                else:
                    vector = [[lastX, lastY], [dataX[j], dataY[j]]]
                    vector_str += str(getVectorNumber(vector))
                    lastX = dataX[j]
                    lastY = dataY[j]
                nextPos += step
        if min_pos == -1:
            min_str = vector_str
            min_pos = i
        else:
            dist = float(getDistance(digits[i], vector_str)) / len(digits[i])
            if dist < leastDistance:
                leastDistance = dist
                min_pos = i
                min_str = vector_str
    return min_pos


if __name__ == '__main__':
    print getVectorNumber([[0,0], [0,6]])
