.PHONY: all clean example

all: $(shell find . -mindepth 1 -maxdepth 1 -not -name '.git' -type d -printf '%p.txt\n')

clean:
	rm -f *.txt

%.txt: % %/*.pub Makefile
	(echo $< SSH host key fingerprints; echo; ./sshfp.py $</*.pub) | gpg2 --clearsign > $@

example:
	@rm -f example_dsa example_rsa example_ecdsa example_ed25519
	@rm -f example_dsa.pub example_rsa.pub example_ecdsa.pub example_ed25519.pub
	@ssh-keygen -t dsa -b 1024 -f example_dsa -N "" >/dev/null
	@ssh-keygen -t rsa -b 4096 -f example_rsa -N "" >/dev/null
	@ssh-keygen -t ecdsa -b 521 -f example_ecdsa -N "" >/dev/null
	@ssh-keygen -t ed25519 -b 256 -f example_ed25519 -N "" >/dev/null
	@(echo "example.com SSH host key fingerprints"; echo; ./sshfp.py example_*.pub) | gpg2 --clearsign
	@rm -f example_dsa example_rsa example_ecdsa example_ed25519
	@rm -f example_dsa.pub example_rsa.pub example_ecdsa.pub example_ed25519.pub
