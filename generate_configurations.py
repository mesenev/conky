import os

path = "result"
src = "configs"
try:
    os.mkdir(path)
except OSError:
    print(f"Creation of the directory {path} failed")
else:
    print(f"Successfully created the directory {path}")

with open('base_settings.conf', 'r') as f:
    header = f.readlines()
for i in os.listdir('configs'):
    with open(f"{src}/{i}", 'r') as f:
        body = f.readlines()

    with open(f'{path}/{i}', 'w') as f:
        f.writelines(header + body)

print('All done!')
