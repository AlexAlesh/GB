import os
import shutil

for root, dirs, files in os.walk('my_project'):
    if not os.path.exists('my_project/templates'):
        os.mkdir('my_project/templates')
    for file in files:
        if file.endswith(".html"):
            path_file = os.path.join(root,file)
            path_file_new = os.path.join('my_project/templates', os.path.basename(os.path.dirname(path_file)))
            if not os.path.exists(path_file_new):
                os.mkdir(path_file_new)
            path_file_save = os.path.join(path_file_new, os.path.basename(path_file))
            shutil.copy(path_file, path_file_save)
