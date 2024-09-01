def solution(bandage, health, attacks):
    answer = 0
    t = bandage[0]
    x = bandage[1]
    y = bandage[2]
    max_health = health
    cont = 0
    flag = 0
    for i in range(1, attacks[-1][0] + 1):
        cont += 1
        if attacks[flag][0] == i:
            health -= attacks[flag][1]
            if health <= 0:
                return -1
            cont = 0
            flag += 1
        else:
            health += x
            if cont == t:
                health += y
                cont = 0
            if health > max_health:
                health = max_health
    answer = health
    return answer