
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' an exercise of multiprocessing'

__author__ = 'victor yu'

from multiprocessing import Process, freeze_support
import os
import time

def run_proc(name):
    print(f'Run child process {name} ({os.getpid()})...')
    time.sleep(3)

if __name__ == '__main__':
    # This ensures the program runs correctly on platforms that use spawn
    freeze_support()

    print(f'Parent process {os.getpid()}.')
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    
    p.start()
    p.join()

    print('Child process end.')