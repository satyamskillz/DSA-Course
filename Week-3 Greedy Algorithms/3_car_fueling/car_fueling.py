# python3
import sys


def compute_min_refills(distance, tank, stops):
    current = 0
    nos = 0
    if (tank >= distance):
        nos = 0
    elif (stops[0] > tank):
        nos = -1
    else:
        i = 0
        while current <= distance:
            last = current
            while i < len(stops) and (stops[i]) - last <= tank:
                current = stops[i]
                i = i + 1
            if last == current and current < distance:
                nos = -1
                break
            if current != last:
                nos = nos + 1
            if distance - current <= tank:
                break
    return nos


if __name__ == '__main__':
    d, m, _, *stops = map(int, input().rstrip().split())
    print(compute_min_refills(d, m, stops))
