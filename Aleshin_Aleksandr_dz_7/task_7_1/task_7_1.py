import os
qwe = ['settings', 'authapp', 'adminapp', 'authapp']
for i in qwe:
    dir_path = os.path.join('my_project', i)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
