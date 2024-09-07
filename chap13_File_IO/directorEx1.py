
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' an exercise of directory operation '

__author__ = 'victor yu'

# 利用os模块编写一个能实现dir -l输出的程序
# use os module to write a program which can implement the output as "ls -l"


import os
import stat
import time

def file_mode(mode):
    # Convert file mode to a format similar to `ls -l` output
    is_dir = 'd' if stat.S_ISDIR(mode) else '-'
    perms = [
        'r' if mode & stat.S_IRUSR else '-',
        'w' if mode & stat.S_IWUSR else '-',
        'x' if mode & stat.S_IXUSR else '-',
        'r' if mode & stat.S_IRGRP else '-',
        'w' if mode & stat.S_IWGRP else '-',
        'x' if mode & stat.S_IXGRP else '-',
        'r' if mode & stat.S_IROTH else '-',
        'w' if mode & stat.S_IWOTH else '-',
        'x' if mode & stat.S_IXOTH else '-',
    ]
    return is_dir + ''.join(perms)

def display_detailed_file_info(directory='.'):
    # Get all files and directories in the current directory
    with os.scandir(directory) as entries:
        for entry in entries:
            # Get file status
            info = entry.stat()
            # Get file mode/permissions
            mode = file_mode(info.st_mode)
            # Get number of hard links
            nlink = info.st_nlink
            # File size (in bytes)
            size = info.st_size
            # Last modification time
            mtime = time.strftime('%Y-%m-%d %H:%M', time.localtime(info.st_mtime))
            # File or directory name
            name = entry.name
            
            # Output in a format similar to `ls -l`
            print(f"{mode} {nlink} {size} {mtime} {name}")

# Call the function to display detailed file information for the current directory
display_detailed_file_info()
