import os

# dir_name = 'first_dir'
# new_dir_name = '../first_dir_out'
# if os.path.exists(dir_name) and not os.path.exists(new_dir_name):
#     os.rename(dir_name, new_dir_name)


# import os
#
# for root, dirs, files in os.walk('my_project'):
#     for file in files:
#         if file.endswith(".html"):
#             path_file = os.path.join(root,file)
#             print(path_file)
#             q = path_file.split(r'authapp')
#             w = q[0]
#             print(w, ' w')
#             dir_name = w + r'\authapp'
#             print(dir_name)
#             new_dir_name = r'my_project\authapp'
#             if os.path.exists(dir_name) and not os.path.exists(new_dir_name):
#                 os.rename(dir_name, new_dir_name)


import os

# for root, dirs, files in os.walk('my_project'):
#     for dir in dirs:
#         print(dir)
#         if dir == 'authapp':
#             dir_name = 'authapp'
#             new_dir_name = '../authapp'
#             if os.path.exists(dir_name) and not os.path.exists(new_dir_name):
#                 os.rename(dir_name, new_dir_name)
#
#






# import os
#
# for root, dirs, files in os.walk('my_project'):
#     for file in files:
#         if file.endswith(".html"):
#             path_file = os.path.join(root,file)
#             print(path_file)
#             q = path_file.split(r'authapp')
#             w = q[0]
#             print(w, ' w')
#             dir_name =  w + r'\authapp'
#             print(dir_name)
#             new_dir_name = r'my_project/authapp'
#             if os.path.exists(dir_name) and not os.path.exists(new_dir_name):
#                 os.rename(dir_name, new_dir_name)
#

import os

for root, dirs, files in os.walk('my_project'):
    for file in files:
        if file.endswith(".html"):
            path_file = os.path.join(root,file)

            q = path_file.split('templates')
            s = root.split('templates')
            dir_name = s[0] + 'templates'

            for i in s:
                if i == s[1]:
                    print(i)
                    # os.mkdir('templates')

                    # if not os.path.exists(dir_path):
                    #     os.mkdir(dir_path)
                    #

                    if not os.path.exists('templates'):
                        os.mkdir('templates')
                    new_dir_name = r'.\templates' + i
                    print(dir_name)
                    print(new_dir_name)

                    if os.path.exists(dir_name) and not os.path.exists(new_dir_name):
                        os.rename(dir_name, new_dir_name)


# py_files = [os.path.join('my_project', item) for item in os.listdir('my_project') if item.lower().endswith('.html')]
# print(py_files)

        # dir_name = 'my_project\\authapp\\authapp'
        # new_dir_name = 'my_project/authapp/authapp'
        # if os.path.exists(dir_name) and not os.path.exists(new_dir_name):
        #     os.rename(dir_name, new_dir_name)