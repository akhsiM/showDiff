import os, difflib

# Prep files
while True:
    file1 = input('Enter Filename 1:')
    if os.path.exists(os.path.join(os.getcwd(), file1)):
        break
while True:
    file2 = input('Enter Filename 2:')
    if os.path.exists(os.path.join(os.getcwd(), file2)):
        break 

file3 = str(os.path.join(os.getcwd(),'diff'))

with open(file1) as f1, open(file2) as f2:
    f1 = f1.readlines()
    f2 = f2.readlines()

diff = difflib.ndiff(f1, f2)
count = 0
with open(file3, 'w') as result:
    for line in diff:
        if line[0] == '+':
            count+= 1
            result.write('{line} - [{file}]\n'.format(line = line[2:-1], file = os.path.basename(file2)))
        elif line[0] == '-':
            count+= 1
            result.write('{line} - [{file}]\n'.format(line = line[2:-1], file = os.path.basename(file1)))


print(f'{str(count)} differences.')
