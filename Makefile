.PHONY: all

all: $(shell find . -mindepth 1 -maxdepth 1 -type d -printf '%p.txt\n')

%.txt: % %/*.pub Makefile
	(echo $< SSH host key fingerprints; echo; ./sshfp.py $</*.pub) | gpg2 --clearsign > $@
