card = []
num = int(input())
for i in range(num):
    suit, rank = input().split()
    rank = int(rank)
    card.append((suit, rank))

cards = [(s, r) for s in ["S", "H", "C", "D"] for r in range(1, 14)]
for trump in cards:
    if trump not in card:
        print(*trump)
