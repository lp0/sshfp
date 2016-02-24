.PHONY: all clean

all: $(shell find . -mindepth 1 -maxdepth 1 -not -name '.git' -type d -printf '%p.txt\n')

clean:
	rm -f *.txt

%.txt: % %/*.pub Makefile
	(echo $< SSH host key fingerprints; echo; ./sshfp.py $</*.pub) | gpg2 --clearsign > $@
