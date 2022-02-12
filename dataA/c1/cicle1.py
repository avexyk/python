# break
s = 0
for n in range(1, 10):
  if n % 7 == 0:
    break
  s += n

print(s)

# continue
s = 0
for n in range(1, 10):
  if n % 2 == 0:
    continue
  s += n
print(s)

# break
s = 0
for n in range(1, 10):
  if n % 11 == 0:
    break
  s += n
else:
  s += 10
print(s)

# pass
s = 0
for n in range(1, 10):
  if n % 2 == 0:
    pass
  s += n
print(s)

# continue
s = 0
for n in range(1, 10):
  if n%2 != 0:
    continue
s+=n

print(s)