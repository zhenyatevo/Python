import random
secret = random.randint(1,99)
guess = 0
tries = 0
print("Эй, на палубе! Я Ужасный пират Робертс, и у меня есть секрет!")
print("Это число от 1 до 99. Я дам тебе 6 попыток.")
while( guess != secret and tries < 6):
    guess = int(input("Твой вариант? "))
    if guess < secret:
        print("Это слишком мало, презренный пес!")
    elif guess > secret:
        print("Это слишком много, сухопутная крыса!")

    tries = tries + 1

if guess == secret:
    print("Хватит! ТЫ угадал секрет!")
else:
    print("Попытки кончились!")
    print("Это число ", secret)
    
# в угадывании полезен принцип бинарного поиска
