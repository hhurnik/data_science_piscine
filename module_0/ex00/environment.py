import random
import time
import sys
from math import pi, cos

# simulate hourly temperatures over a 24-hour period
def temp_simulation(min_temp, max_temp):
    mean_temp = (min_temp + max_temp) / 2
    amplitude = (max_temp - min_temp) / 2 
    
    for i in range (1, 25):
            t0 = time.time()
            
            # model the daily temp cycle 
            temp = mean_temp + (amplitude * cos((2 * pi * (i - 15)) / 24))
            noise = random.uniform(-1, 1)
            temp += noise

            if temp < min_temp:
                temp = min_temp
            elif temp > max_temp:
                temp = max_temp

            # round to .25
            temp = round(temp * 4) / 4

            print(temp, flush=True)
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
        print("Invalid season", file=sys.stderr)


def main():
    if len(sys.argv) == 2:
        season = sys.argv[1]
        which_season(season)
    else:
        print("Usage: environment.py <season>")

if __name__ == "__main__":
    main()
