def main():
    input = open("input.txt").read()
    ranges, _ = input.split("\n\n")
    ranges = [r.split("-") for r in ranges.split("\n")]
    ranges = [(int(lower), int(upper)) for lower, upper in ranges]

    while True:
        overlaps = []
        no_overlaps = []
        print(ranges)
        for r in ranges:
            has_overlaps = False
            for s in ranges:
                if r != s and check_overlap(r,s):
                    overlaps.append(fix_overlap(r,s))
                    has_overlaps = True
            if not has_overlaps:
                no_overlaps.append(r)
        if len(overlaps) == 0:
            break
        ranges = list(set(no_overlaps + overlaps))

    total_fresh = 0
    for l, u in ranges:
        total_fresh += u - l + 1

    print(total_fresh)



def check_overlap(range1, range2):
    lower1, upper1 = range1
    lower2, upper2 = range2
    return (upper1 >= lower2 and lower1 <= upper2) or (upper2 >= lower1 and lower2 <= upper1)


def fix_overlap(range1, range2):
    return min(range1[0],range2[0]), max(range1[1], range2[1])
            
main()
