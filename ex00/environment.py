#  the outside temperature 
#  program simulates 
# // 4 simulations for each season



# season parameter 
# display a floating number for temperature for each hour, so 24 slices
# small random variations introduced from one cycle to the nexxt
# season affecrs the simulated temperatures

import random
import time
import sys
import numpy as np

def temp_simulation(min_temp, max_temp):
    temp0 = random.randrange(min_temp, max_temp + 1)
    for i in range (1, 25):
        t0 = time.time()
        temp = random.randrange(temp0 - 2, temp0 + 3)
        if temp < min_temp:
            temp = min_temp
        elif temp > max_temp:
            temp = max_temp
        print("The temperature for hour", i, "is", temp)
        temp0 = temp
        t1 = time.time()


        if t1 - t0 < 1:
            time.sleep(1 - (t1 - t0))


def which_season(season):
    if season == "fall":
        temp_simulation(0, 10)
    elif season == "winter":
        temp_simulation(-10, 0)
    elif season == "spring":
        temp_simulation(10, 20)
    elif season == "summer":
        temp_simulation(20, 30)
    else:
        print("Invalid season")


def main():
    season = sys.argv[1]
    which_season(season)


if __name__ == "__main__":
    main()





# def fall():
#     # 0 - 10 
#     temp0 = random.randrange(0, 11)
#     for i in range (0, 24):
#         t0 = time.time()
#         temp = random.randrange(temp0 - 2, temp0 + 3)
#         if temp < 0:
#             temp = 0
#         elif temp > 10:
#             temp = 10
#         print("The temperature for hour number", i, "is", temp)
#         temp0 = temp
#         t1 = time.time()


#         if t1 - t0 < 1:
#             time.sleep(1 - (t1 - t0))
    

# def winter():
#     # -10 - 0
#     temp0 = random.randrange(-10, 1)
#     for i in range (0, 24):
#         t0 = time.time()
#         temp = random.randrange(temp0 - 2, temp0 + 3)
#         if temp < -10:
#             temp = -10
#         elif temp > 0:
#             temp = 0
#         print("The temperature for hour number", i, "is", temp)
#         temp0 = temp
#         t1 = time.time()


#         if t1 - t0 < 1:
#             time.sleep(1 - (t1 - t0))


# def spring():
#     # 10 - 20
#     temp0 = random.randrange(10, 21)
#     for i in range (0, 24):
#         t0 = time.time()
#         temp = random.randrange(temp0 - 2, temp0 + 3)
#         if temp < 10:
#             temp = 10
#         elif temp > 20:
#             temp = 20
#         print("The temperature for hour number", i, "is", temp)
#         temp0 = temp
#         t1 = time.time()


#         if t1 - t0 < 1:
#             time.sleep(1 - (t1 - t0))


# def summer():
#     # 20 - 30
#     temp0 = random.randrange(20, 31)
#     for i in range (0, 24):
#         t0 = time.time()
#         temp = random.randrange(temp0 - 2, temp0 + 3)
#         if temp < 20:
#             temp = 20
#         elif temp > 30:
#             temp = 30
#         print("The temperature for hour number", i, "is", temp)
#         temp0 = temp
#         t1 = time.time()


#         if t1 - t0 < 1:
#             time.sleep(1 - (t1 - t0))

