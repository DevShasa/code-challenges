from collections import defaultdict

def special_pairs(xs):
    seen = defaultdict(int)
    count = 0
    for x in xs:
        count += seen[x]
        seen[x] += 1
    return count


def test_example():
    assert special_pairs([1, 2, 3, 1, 1, 3]) == 4