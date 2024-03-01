att = int(input())
comp = int(input())
yds = int(input())
td = int(input())
int_ = int(input())
passer_rating = (((comp / att - 0.3) * 5 + (yds / att - 3) * 0.25 \
                  + (td / att) * 20 + 2.375 - (int_ / att) * 25) / 6) * 100
print(round(passer_rating, 3))