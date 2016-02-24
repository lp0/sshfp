### SSH host key fingerprints

Use [RFC4255](https://tools.ietf.org/html/rfc4255) wherever possible.

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
|        oo=++o+E=|  MD5:
|         . =..o+*|    33:95:13:07:07:10:57:37:c3:ed:07:f8:5c:37:15:37
|          +  o +o|
|         . .  o o|  SHA1:
|        S       .|    ae:ff:7e:a9:1d:51:b1:bb:ad:22:21:14:1a:ab:93:28:d4:a0:59:b0
|         o       |
|                 |  SHA256:
|                 |    s+Hvdov6rSaURA0n3BbVgByRLB7pbwpAp/y6Tx4zEaA
|                 |    B3E1EF768BFAAD2694440D27DC16D5801C912C1EE96F0A40A7FCBA4F1E3311A0
+-----------------+

+---[ECDSA 521]---+
|        ..+ . .  |  MD5:
|         + = . o |    05:2f:5d:f7:92:ce:e9:f6:60:92:41:30:b4:8f:93:69
|        . = . o .|
|         o * o o |  SHA1:
|        S E o +  |    bf:d9:df:46:06:f6:53:40:dc:45:b4:bb:5e:76:a0:4e:d0:51:66:9b
|         . . +   |
|            o =  |  SHA256:
|             + o |    Zt1CuHBdQvZeJ7quUTpQ8BZcKWwOZWORjIbTcyfG/X8
|                .|    66DD42B8705D42F65E27BAAE513A50F0165C296C0E6563918C86D37327C6FD7F
+-----------------+

+--[ED25519 256]--+
|                 |  MD5:
|                 |    68:67:f6:2d:f2:7a:c0:93:ae:f4:10:3b:b2:7f:04:37
|                 |
|      ..E        |  SHA1:
|      ++So       |    80:c9:72:9c:0d:78:6e:52:d7:d9:e6:2f:e2:28:c1:43:99:87:6f:9a
|     . **. .     |
|    . =o.oo .    |  SHA256:
|     + +oo..     |    NhnXwcneUpZoPzQH9HyAV/dNDBNBpLP2HFBnQ9bFYpY
|    ..oooo.      |    3619D7C1C9DE5296683F3407F47C8057F74D0C1341A4B3F61C506743D6C56296
+-----------------+

+---[RSA 4096]----+
|B*  o            |  MD5:
|=+.=             |    02:e4:a4:cc:4a:fa:a1:e8:0d:17:20:44:a3:91:40:b8
|o++ o            |
|E..  .           |  SHA1:
|o ..  . S        |    fe:43:fe:bb:44:56:14:c2:fc:23:ab:e5:94:25:d5:4d:6d:8d:13:7f
|.o ..  .         |
|o...             |  SHA256:
|. +              |    yEqu2cAuzAcuLzfCwLeMzp9g34zAIOnG94dn1IvGAjc
| . .             |    C84AAED9C02ECC072E2F37C2C0B78CCE9F60DF8CC020E9C6F78767D48BC60237
+-----------------+

-----BEGIN PGP SIGNATURE-----
Version: GnuPG v2

iQIcBAEBCgAGBQJWzgytAAoJELr//1/1/6qvmycQAKn39cXfJlPzeCU6h5Onhnb+
5On5xsq0c4/BDmLjsC4EYQmhwaf781L1sSSusfTzyfJqDWvUVPeyDwSOXJFtD4gv
BZb0sP8BG6hTHdg8kfM+tfb/7z+su0VbWDaX4s4EMNU5FbqwcPd38WZdEY3iHmeb
odXtcJ5pbBoBlJcdgx6alt90yRrsUUO8SAXv/zd6Jr2I5WgvqjjzZSVjhc4v4rBv
lXBSGDfTb66RCb9H46321+yudjvXNmIX6zz7G2MswSVt679yiSsdgaxT4fns1/WT
SQPUTG5UZmQ/CUNQJ5PUZg22nsWQW9H7eFsTOEp32gOTbP3WCkwSD2SfigLoWdal
U2gftRk2u1auzhVotHCyfZ6GRtWg8x5CdAqUJ2YTWdZ5Y+5D3YEdAmBhiBacfZBD
AnUhLkCXlRIBDTX+o8p+S+tFQY7wesE7o/6E0kJXPXZwayGd+Pik6/fgFfdHK2l8
aKRkFjY7VmfBqLevmWq59wdnQ+G3iWx1p38TPfM6OkZIjJB2Plv35ObtdxRz5s/Q
GIr7cLH0CxXUWUFz5s0DraRlT61Tz4sQUlGb3t+MeyNMiEzlqAIjYKKXLw9Ehcjb
FF3v1ImSCUWaYCW6jmndMBEtopAvZi3WQ6tmSp+K5uMtZL6J4GPp+NG/LF7aXdHj
d92jzRDKe2ioo4B80t/Q
=EPZf
-----END PGP SIGNATURE-----
```
