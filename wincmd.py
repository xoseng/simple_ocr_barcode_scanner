import subprocess, sys

def execcmd(command):
    cmd = command
    p = subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE)
    # Don't wait finished, start output immediately
    while True:
        out = p.stderr.read(1)
        if out == '' and p.poll() != None:
            break
        if out != '':
            sys.stdout.write(out)
            sys.stdout.flush()
