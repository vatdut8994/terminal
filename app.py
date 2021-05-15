from flask import Flask, render_template, request
from sys import platform
from subprocess import getstatusoutput as cmd
import datetime
import socket
import os

cd = False
name = socket.gethostname()
whoami = cmd('whoami')
pwd = cmd('pwd')[-1]
answer = ''

app = Flask(__name__)
@app.route('/')
def asdf():
    return render_template('index.html')

@app.route('/terminal', methods=['GET', 'POST'])
def asdljkf():
    if request.method == 'POST':
        global answer
        global pwd
        global cd
        if cd == False:
            prompt = whoami[-1]+'@'+name.replace('.local', '')+' ~ % '
        else:
            prompt = whoami[-1]+'@'+name.replace('.local', '')+' '+pwd.split('/')[-1]+' % '
        command = request.form['command']
        if platform.lower() != 'win32' or 'windows':
            if command == 'exit':
                exit()
            elif command =='cls':
                answer = cmd('clear')
            elif command == 'dir':
                answer = cmd('ls')
            else:
                answer = cmd(command)
                if 'cd' in command:
                    os.chdir(command.split(' ')[-1])
                    if '/' in command:
                        pwd = pwd+'/'+command.split('/')[-1]
                    else:
                        pwd = pwd+'/'+command.split(' ')[-1]
                    cd = True

        else:
            if command == 'exit':
                exit()
            else:
                answer = cmd(command)
                if 'cd' in command:
                    os.chdir(command.split(' ')[-1])
                    if '/' in command:
                        pwd = pwd+'/'+command.split('/')[-1]
                    else:
                        pwd = pwd+'/'+command.split(' ')[-1]
                    cd = True
        return render_template('index.html', ask=prompt, card=answer[-1])


if __name__ == "__main__":
    app.run()
