import re


# calculate numbers of score 0
def score_0(list_of_score_number):
    list_of_score_number[0] = list_of_score_number[0] + 1
    return list_of_score_number


# calculate numbers of score 1
def score_1(list_of_score_number):
    list_of_score_number[1] = list_of_score_number[1] + 1
    return list_of_score_number


# calculate numbers of score 2
def score_2(list_of_score_number):
    list_of_score_number[2] = list_of_score_number[2] + 1
    return list_of_score_number


# calculate numbers of score 3
def score_3(list_of_score_number):
    list_of_score_number[3] = list_of_score_number[3] + 1
    return list_of_score_number


# calculate numbers of score 4
def score_4(list_of_score_number):
    list_of_score_number[4] = list_of_score_number[4] + 1
    return list_of_score_number


# calculate numbers of scores
def scoring(list_of_score_number, num_score):
    scores = {
        0: score_0,
        1: score_1,
        2: score_2,
        3: score_3,
        4: score_4
    }

    method = scores.get(num_score, 0)
    if method:
        return method(list_of_score_number)


file_score = open("C:/Users/ziyi/Desktop" + '/score.txt', 'w', encoding='utf-8')

file_passwd = open("C:/Users/ziyi/Desktop" + "/score1.txt", encoding='utf-8')

list_of_score_numbers = 0

list_of_score_numbers = [0, 0, 0, 0, 0]

for num in range(0, 300000):
    line = file_passwd.readline()
    file_score.write(line)
    score = re.findall(r'\t(.+)', line)
    list_of_score_numbers = scoring(list_of_score_numbers, int(str(score[0])))

file_score.write('\n\nNumber of tasted passwords' + '\t' + str(300000) + '\n\n')
file_score.write('Score range\t0 to 4\n')
file_score.write('Score' + '\t' + 'Number of passwords' + '\n')
file_score.write('0' + '\t\t' + str(list_of_score_numbers[0]) + '\n')
file_score.write('1' + '\t\t' + str(list_of_score_numbers[1]) + '\n')
file_score.write('2' + '\t\t' + str(list_of_score_numbers[2]) + '\n')
file_score.write('3' + '\t\t' + str(list_of_score_numbers[3]) + '\n')
file_score.write('4' + '\t\t' + str(list_of_score_numbers[4]) + '\n')
