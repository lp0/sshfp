#!/usr/bin/env python3

import base64
import hashlib
import subprocess
import sys

def __with_colons(hexdigest):
	it = iter(hexdigest)
	return ":".join(["".join(x) for x in zip(it, it)])

def sshfp(filename):
	with subprocess.Popen(["ssh-keygen", "-l", "-v", "-f", filename], stdout=subprocess.PIPE, universal_newlines=True) as process:
		visual_key = process.communicate()[0].split("\n")[1:]

	with open(filename, "r") as f:
		key_data = f.readline().split(" ")[1]
		key_data = base64.b64decode(key_data)

	visual_key[1] += "  MD5:"
	visual_key[2] += "    " + __with_colons(hashlib.md5(key_data).hexdigest())
	visual_key[4] += "  SHA1:"
	visual_key[5] += "    " + __with_colons(hashlib.sha1(key_data).hexdigest())
	visual_key[7] += "  SHA256:"
	visual_key[8] += "    " + base64.b64encode(hashlib.sha256(key_data).digest()).decode("ascii").strip("=")
	visual_key[9] += "    " + hashlib.sha256(key_data).hexdigest().upper()
	print("\n".join(visual_key))

if __name__ == "__main__":
	for filename in sys.argv[1:]:
		sshfp(filename)
