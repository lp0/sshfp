#!/usr/bin/env python3
# SSH host key fingerprint generator
# Copyright 2016  Simon Arlott
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

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
