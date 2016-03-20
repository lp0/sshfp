### SSH host key fingerprints

Use [RFC4255](https://tools.ietf.org/html/rfc4255)
and [VerifyHostKeyDNS yes](http://www.openbsd.org/cgi-bin/man.cgi/OpenBSD-current/man5/ssh_config.5?query=ssh_config&sec=5)
wherever possible.

Alternatively, provide signed fingerprint hashes using this script.

* Create ```hostname``` directory
* Copy ```hostname:/etc/ssh/*.pub``` to ```hostname/```
* Run ```make```


### Example output

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA512

example.com SSH host key fingerprints

+---[DSA 1024]----+
|=B=+...          |     MD5 = be:7d:47:f5:46:e1:20:30:4d:e4:d2:3d:c9:6f:dd:72
|o.+o.o.          |
|.o..++o          |    SHA1 = b0:c4:57:91:db:e3:aa:a8:5c:ed:7b:eb:7b:ab:e1:99:d2:a9:f3:dc
|. .....o .       |
|  ..  o S        |  SHA256 = ueAe42uiVhRPpLfO3tk2JmwaPB2ATMAeCYUVAC69j3o
|   o.= o o       |
|  ... X.o        |   SSHFP = 2 1 B0C45791DBE3AAA85CED7BEB7BABE199D2A9F3DC
| .E .+.*+o+      |
|.o.. o*+o+..     |   SSHFP = 2 2 B9E01EE36BA256144FA4B7CEDED936266C1A3C1D804CC01E09851500 2EBD8F7A
+----[SHA256]-----+

+---[ECDSA 521]---+
|    . +.++Boo .. |     MD5 = fb:99:95:f4:e6:f7:ea:2c:cc:e8:e3:c8:39:aa:83:ba
|   . + =+O** o  .|
|    o . @=+o.. . |    SHA1 = 05:34:4d:24:ae:c5:da:c0:23:67:93:b1:6a:13:11:95:39:fe:de:e3
|   . + E.=o . o  |
|    + o S. . o   |  SHA256 = WCUX441Zc63q+R8MoYRNsB4kHymtYmoR3Y9tkJjeJ6U
|   o        . o  |
|  .        . . o |   SSHFP = 3 1 05344D24AEC5DAC0236793B16A13119539FEDEE3
|            o   .|
|             ....|   SSHFP = 3 2 582517E38D5973ADEAF91F0CA1844DB01E241F29AD626A11DD8F6D90 98DE27A5
+----[SHA256]-----+

+--[ED25519 256]--+
|   +.*..E.   .oo |     MD5 = 1a:1f:f2:28:70:f5:1a:12:c7:d8:0a:49:fd:b6:52:8a
|  . O B . o ..o .|
|   o B * o o . . |    SHA1 = bd:4e:82:cd:70:77:0b:21:9f:de:6f:1a:c9:76:1a:51:64:8a:c7:d7
|  . . B = +   .  |
|   . . oS+oo.. . |  SHA256 = zqbRdduYDPt60D1RaGEoi3MjcpCzwNgThdbsKPXhVgc
|       + ..=.=o  |
|      . = ..= .. |   SSHFP = 4 1 BD4E82CD70770B219FDE6F1AC9761A51648AC7D7
|       +   ..    |
|      .   .o.    |   SSHFP = 4 2 CEA6D175DB980CFB7AD03D516861288B73237290B3C0D81385D6EC28 F5E15607
+----[SHA256]-----+

+---[RSA 4096]----+
|+BO+O=. .        |     MD5 = 13:9a:3d:ae:2a:43:30:bd:32:54:83:24:8d:33:89:93
|.+.O .oo         |
|  = o oo         |    SHA1 = df:fb:61:17:11:c1:6d:09:1f:ad:29:ca:1b:bc:4d:ae:77:85:cd:c2
| . + o  o        |
|. . = .ES        |  SHA256 = mot7v8ONny6BK1UAUAsEx0jUuzZoVJHs21GpAnlZFL8
| o = .oo.        |
|. . ..oo +       |   SSHFP = 1 1 DFFB611711C16D091FAD29CA1BBC4DAE7785CDC2
|    ..o.= ..     |
|    o+..o*+      |   SSHFP = 1 2 9A8B7BBFC38D9F2E812B5500500B04C748D4BB36685491ECDB51A902 795914BF
+----[SHA256]-----+

-----BEGIN PGP SIGNATURE-----
Version: GnuPG v2

iQIcBAEBCgAGBQJW7fLdAAoJEMiXXyBDyl0kUJ8P/3W5xGku6Dj7FI3OVx8v+9aG
CG/cP9ZMGryYbGmjiBaTYyHEsOMc54BzFcbOE8IzbNk/gEG/i+eLSZvIw9hAYNzi
raPRVCFNLq32aytJ8KtyBMcUG+T6Ai1PJUHVfL11TC0esEb5V3D/8E2YOe3kRBuN
xTAXPHNNDarZ0njXigT8E2azSDQ9+foxPxWvQ3vmgJF/BYkK/LH0rjqwZgU+eEzA
AlDNLDm2Wq+IiVUtHQT29LmoyzPttiKUhSG15A4CWt+w/HPCcDLMn+13O1COBpsy
l+4Kd+u7obTbX4pQ4lZpmUEzlG2945clFLgUHKxXtrS9RfBuAiQuG2DqkegS/qdF
dAaZ2XLcaM8SDfZlLkh0JWgHnLYwgi+TYhLu4T6qsakUJJkx0ev5LbyX9SLiv03F
HZmL33t0GziV5N4WpJ7t6BuW1++nDo9TQcaiWPvVGu6dkGccV6v7J/tsXkcjgrMH
KqoP6QAOx1TACRtdgVpmgeFYsNHjFwpfwzf0rmhtjrwLV2VzKvq4AZmJFCgHRTEZ
ndIV471562BhVEE6UM4Rz3PfUWTwSRxeoOG/NtBhV2Tk4mk8Vb9WfcMOCGVgq0kN
nI4VNfrZWC2/uDFSWPYgcR+78GV7xcTzih45aycYVXHcaCDhO1z34MlTBWmHoqhB
mMriMkDu/HgDCSwS3HyA
=EJLV
-----END PGP SIGNATURE-----
```
