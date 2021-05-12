# from flask import Flask, render_template, request
# from os import system as s
# import subprocess
# import socket
# import sys

# whoami = subprocess.getstatusoutput('whoami')
# app = Flask(__name__)
# @app.route('/')
# def asdf():
#     return render_template('index.html')

# @app.route('/terminal', methods=['GET', 'POST'])
# def asdljkf():
#     if request.method == 'POST':
#         answer = subprocess.getstatusoutput(request.form['command'])
#         answer = answer[-1]
#         new_ans = ''
#         for i in answer.split('\n'):
#             new_ans = new_ans + i +'\n\n'
#     return render_template('index.html', card=new_ans, ask=str(socket.gethostname()).replace('.local', '')+'@'+whoami[-1]+'~ %')

# if __name__=="__main__":
#     app.run(debug=True)

from flask import Flask, render_template, request
from sys import platform
from subprocess import getstatusoutput as cmd
import datetime
import socket
import os

pwd = cmd('pwd')
pwd = pwd[-1]
pwd2 = pwd
name = socket.gethostname()
lastlogin = open('lastlogin.txt', 'r')
print(lastlogin.read())
lastlogin = open('lastlogin.txt', 'w')
lastlogin.write('Last Login: ' + str(datetime.datetime.now()))
lastlogin.close()
answer = ''

app = Flask(__name__)


@app.route('/')
def asdf():
    return render_template('index.html')


@app.route('/terminal', methods=['GET', 'POST'])
def adlfkj():
    if request.method == 'POST':
        global answer
        global pwd
        if pwd == pwd2:
            prompt = pwd.split('/')[-1]+'@'+name.replace('.local', '')+' ~ % '
        else:
            prompt = pwd2.split('/')[-1]+'@'+name.replace('.local', '')+' '+pwd.split('/')[-1]+' % '
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
        return render_template('index.html', ask=prompt, card=answer[-1])


if __name__ == "__main__":
    app.run(debug=True)
