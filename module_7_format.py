
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451


print('В команде Мастера кода участников: %s ! ' % team1_num)
print("Итого сегодня в командах участников: %s и %s !" % (team1_num, team2_num))
print('Команда Волшебники данных решила задач: {}'.format(score_2) + ' !')
print('Волшебники данных решили задачи за {}'.format(team1_time) + ' с !')
print(f'Команды решили {score_1} и {score_2} задач.')

def challenge_result():
    if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
        result = 'Победа команды Мастера кода!'
        print(result)
    elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
        result = 'Победа команды Волшебники Данных!'
        print(result)
    else:
        result = 'Ничья!'
        print(result)

tasks_total = score_1 + score_2

time_avg = (team1_time + team2_time) / tasks_total

print(tasks_total)
print(time_avg)


