import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: expert_system.py <min_temp> <max_temp>")
        return

    min_temp = float(sys.argv[1])
    max_temp = float(sys.argv[2])

    indoor_temp = None

    # read external temperatures from standard input
    for line in sys.stdin:
        external_temp = float(line.strip())
        if indoor_temp is None:
            indoor_temp = external_temp

        # turn on heating if the house is too cold
        if indoor_temp < min_temp:
            action = "heating"
            indoor_temp += 0.5

        #  turn on cooling if the house is too hot
        elif indoor_temp > max_temp:
            action = "cooling"
            indoor_temp -= 0.5
        else:
            action = "nothing"

            # slowly move the indoor temperature toward the external temperature
            if indoor_temp > external_temp:
                indoor_temp = max(external_temp, indoor_temp - 0.25)
            elif indoor_temp < external_temp:
                indoor_temp = min(external_temp, indoor_temp + 0.25)

        print(f"{external_temp} - {action} - {indoor_temp}")

if __name__ == "__main__":
    main()