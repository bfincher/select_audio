#!/usr/bin/python
import re
import sys
import subprocess

regex = re.compile(r'.*?Stream #(\d+):(\d+)\((\w+)\): Audio.*')

def convert(major, minor):
    command = '-map 0:0 -map %s:%s -c:v copy -c:a:%s libmp3lame -b:a:0 128k -strict -2' % (major, minor, minor)
    #command = ['ffmpeg', '-i', '$INPUT_FILE', '-map', '0:0', '-map %s:%s' % (major, minor), '-c:v', 'copy', '-c:a:%s' % minor, 'libmp3lame', '-b:a:0', '128k', '-strict', '-2']

    print command 

if __name__ == '__main__':
#    if p.returncode == 0:
    firstAudioMatch = True
    for line in sys.stdin:
        m = regex.match(line)
        if m:
            major = m.group(1)
            minor = m.group(2)
            lang = m.group(3)

            if firstAudioMatch:
                if lang == 'eng':
                    print 'default lang is already english'
                    sys.exit(-1)
            else:
               convert(major, minor)
               sys.exit(0)

            firstAudioMatch = False

    sys.exit(-1)
#    else:
#        print 'bad return code: %s.  Command = %s\n%s' % (p.returncode, command, result)
