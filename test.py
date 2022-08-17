import subprocess, os

args = "-alh"

subprocess.run(["ls", args])

for item in os.listdir("."):
	print(item)
