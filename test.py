import subprocess, os

args = "-alh"

subprocess.run(["ls", args])

arg1 = 'classify.py'
arg2 = '--in'
arg3 = '../CommonVoice/sample-000000.wav'
arg4 = '--restore_path'
arg5 = 'deepspeech-0.4.1-checkpoint/model.v0.4.1'

#subprocess.run(['python3', arg1, arg2, arg3, arg4, arg5])

for item in os.listdir("/content/CommonVoice"):
	subprocess.run(["python3", arg1, arg2, '/content/CommonVoice/' + item, arg4, arg5])
