import os, sys, time, subprocess
import pandas as pd
import itertools

commands = pd.read_csv('commands.txt', index_col=None)

os.chdir('./SharpRDP/SharpRDP/bin/Debug/')

for index, row in commands.iterrows():
    if str(row['mode']) == 'winr':
        subprocess.run("""SharpRDP.exe computername={} command="{}" username={} password={} elevated=winr""".format(row['ip'], row['command'], row['username'], row['password']), shell=True, timeout=30)
    if str(row['mode']) == 'cmd':
        subprocess.run("""SharpRDP.exe computername={} command="{}" username={} password={}  exec=cmd""".format(row['ip'], row['command'], row['username'], row['password']), shell=True, timeout=30)
    else:
        subprocess.run("""SharpRDP.exe computername={} command="{}" username={} password={}""".format(row['ip'], row['command'], row['username'], row['password']), shell=True, timeout=30)
    time.sleep(row['time_delay']/1000)