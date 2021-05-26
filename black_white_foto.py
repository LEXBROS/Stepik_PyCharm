h, w = map(int, input().split())
all_pix = []
for i in range(h):
    colors = input().split()
    all_pix += colors
if 'C' in all_pix or 'M' in all_pix or 'Y' in all_pix:
    print('#Color')
else:
    print('#Black&White')
