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

def __with_colons(hash):
	it = iter(hash.hexdigest().lower())
	return ":".join(["".join(x) for x in zip(it, it)])

def __openssh_base64(hash):
	return base64.b64encode(hash.digest()).decode("ascii").strip("=")

def __split_by_n(seq, n):
	"""A generator to divide a sequence into chunks of n units."""
	# http://stackoverflow.com/a/9475270/388191
	while seq:
		yield seq[:n]
		seq = seq[n:]

def __dns_format(hash):
	return " ".join(__split_by_n(hash.hexdigest().upper(), 56))

def __sshfp_type(visual_key):
	for (key, value) in { "[RSA ": 1, "[DSA ": 2, "[ECDSA ": 3, "[ED25519 ": 4, }.items():
		if key in visual_key[0]:
			return str(value)
	return "?"

def sshfp(filename):
	with subprocess.Popen(["ssh-keygen", "-l", "-v", "-f", filename], stdout=subprocess.PIPE, universal_newlines=True) as process:
		visual_key = process.communicate()[0].split("\n")[1:]

	with open(filename, "r") as f:
		key_data = f.readline().split(" ")[1]
		key_data = base64.b64decode(key_data)

	visual_key[1] += "     MD5 = " + __with_colons(hashlib.md5(key_data))
	visual_key[3] += "    SHA1 = " + __with_colons(hashlib.sha1(key_data))
	visual_key[5] += "  SHA256 = " + __openssh_base64(hashlib.sha256(key_data))
	visual_key[7] += "   SSHFP = " + __sshfp_type(visual_key) + " 1 " + __dns_format(hashlib.sha1(key_data))
	visual_key[9] += "   SSHFP = " + __sshfp_type(visual_key) + " 2 " + __dns_format(hashlib.sha256(key_data))
	print("\n".join(visual_key))

if __name__ == "__main__":
	for filename in sys.argv[1:]:
		sshfp(filename)
