#!/usr/bin/env python3

import sys;
import signal;

def sigint_handler(signal, frame):
    print("Keyboard Interrupt")
    sys.exit(0)

def main():
    MAX_HOUR = 8
    sum_percent = 0
    sum_minute = 0
    sum_percent_left = 100
    result = []
    input_percent = []

    total_tasks = 0
    should_prompt_total_task = len(sys.argv) < 2

    if should_prompt_total_task:
        total_tasks = int(input("Enter total task : "))
    else:
        total_tasks = int(sys.argv[1])

    for i in range(0, total_tasks):
        percent = 0

        if i < (total_tasks - 1):
            percent = int(input(f"({sum_percent_left}%)\t-> Percent #{i + 1} : "))
        else:
            percent = sum_percent_left
            print(f"({sum_percent_left}%)\t-> Percent #{i + 1} : {percent}")

        sum_percent += percent
        sum_percent_left -= percent

        input_percent.append(percent)

        if percent % 5 != 0:
            print("Only accept number that can divide by 5")
            quit()

        raw = MAX_HOUR * (percent / 100)
        hour = int(raw)
        minute = int((raw - hour) * 60)
        seconds = round(((raw - hour) * 60) - minute) * 60

        if seconds >= 60:
            minute += 1
            seconds = 0

        sum_minute += (hour * 60) + minute + (seconds / 60)
        result.append(f"{hour}h, {minute}m, {seconds}s")

    print("------------------------------")

    can_use_output = True

    for i in range(0, len(result)):
        if input_percent[i] <= 0:
            can_use_output = False
        print(f"#{i+1} : {result[i]}")

    print("------------------------------")
    print(f"Sum : {sum_percent}%, {sum_minute}m")

    if sum_percent < 100:
        can_use_output = False

    if not can_use_output:
        print("*** Cannot use this output ***")


if __name__ == "__main__":
    signal.signal(signal.SIGINT, sigint_handler)
    main()

