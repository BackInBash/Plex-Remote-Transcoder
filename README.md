# Plex Remote Transcoder

![Plex Backend](/content/plex.png "Plex Backend")
<br />
![Plex Deploy](content/plex_deploy.png "Plex Deploy")

## Install Dependencies

* Python2.7
* Python2.7-dev
* build-essential
* python-setuptools
* git
* ffmpeg
* ssh
* NFS / SMB
* openvpn client

## Worker Node Configuration

### Hetzner Cloud INIT

* Install Dependencies
* Configure OpenVPN Client
* Install Plex Remote Transcoder
* Crete Plex User & Group
* Configure NFS Share over VPN
* Test SSH Connection from Master
* Todo
    * Unattend Deploy Slaves from Master

```yaml
# Plex Remote Transcoder
# Cloud INIT v0.9

#cloud-config
package_update: true
package_upgrade: true

packages:
 - htop
 - iftop
 - git
 - curl
 - python2.7
 - python2.7-dev
 - python-setuptools
 - build-essential
 - openvpn
 - ffmpeg
 - nfs-kernel-server

write_files:
  - path: /etc/openvpn/client.conf
    content: |
         client
         dev tun
         proto udp
         remote 159.69.115.XX 1194
         resolv-retry infinite
         persist-key
         persist-tun
         ca ca.crt
         cert client1.crt
         key client1.key
         comp-lzo
         verb 3
  - path: /etc/openvpn/ca.crt
    content: |
         -----BEGIN CERTIFICATE-----
         MIIExzCCA6+gAwIBAgIJAIdqbWMIBFT+MA0GCSqGSIb3DQEBCwUAMIGdMQswCQYD
         VQQGEwJERTELMAkGA1UECBMCQkExDTALBgNVBAcTBEZTTjExDTALBgNVBAoTBGRh
         dGExFjAUBgNVBAsUDVtPbUddIE5ldHdvcmsxEDAOBgNVBAMTB2RhdGEgQ0ExEDAO
         BgNVBCkTB0Vhc3lSU0ExJzAlBgkqhkiG9w0BCQEWGHdlYm1hc3RlckBvbWctbmV0
         d29yay5kZTAeFw0xODA5MDYxNTQ3NTNaFw0yODA5MDMxNTQ3NTNaMIGdMQswCQYD
         VQQGEwJERTELMAkGA1UECBMCQkExDTALBgNVBAcTBEZTTjExDTALBgNVBAoTBGRh
         dGExFjAUBgNVBAsUDVtPbUddIE5ldHdvcmsxEDAOBgNVBAMTB2RhdGEgQ0ExEDAO
         BgNVBCkTB0Vhc3lSU0ExJzAlBgkqhkiG9w0BCQEWGHdlYm1hc3RlckBvbWctbmV0
         d29yay5kZTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBANzADMBCFNIC
         OtMAaWfAeOyVQJQiBI7BxpWCBaml98velZMiLW3VcFzFPtgn72KEkgKb7NWabWUu
         u5OOpySc8c1kc/YtXDLY2746pfJokpIoIOvr+T86OyuUuw3mC1NJFbwlx8tQFYnl
         9g7sCCHPwAy+7O6lVJ1+qduqpvr0CzRkeBMKO5wm3HLlwnw7oPXihceMbVD+/Wf4
         CzgZ2RVs99khrqxgXqGiQy4OxMOjECDFaqWEhrocpkTAbZeB3AKE141MF3us8zTg
         TQnM4jirExN0mWbE9PemTbd2DAdd3DLhjhMw04u4sOyEpM7HMvn70g8fn4toeEjO
         F2ReCz0SEoECAwEAAaOCAQYwggECMB0GA1UdDgQWBBRVjPhSQpi1i+QNjSRfml9+
         ShqzOzCB0gYDVR0jBIHKMIHHgBRVjPhSQpi1i+QNjSRfml9+ShqzO6GBo6SBoDCB
         VQQKEwRkYXRhMRYwFAYDVQQLFA1bT21HXSBOZXR3b3JrMRAwDgYDVQQDEwdkYXRh
         IENBMRAwDgYDVQQpEwdFYXN5UlNBMScwJQYJKoZIhvcNAQkBFhh3ZWJtYXN0ZXJA
         b21nLW5ldHdvcmsuZGWCCQCHam1jCARU/jAMBgNVHRMEBTADAQH/MA0GCSqGSIb3
         DQEBCwUAA4IBAQCAfG37gywyECgnpxrgtHOzdyHuZhJBhacihYvrqsNHCK6wLo2D
         0NxlIBgSDbi/xoIHHLB2St3YNM1VXRyQVzJ6KRLo5q6cPuDHQ+MhdvIYYQNqMBtN
         nb8hsDy8MEmDxzDGtIWfmvXOF7iDJ9wF+1tDgtjc1hOmwb9gu5V6T4dndEXAnUHz
         a5t5U9AiAuC0iH3gYnJOKjc2JD+x3JCbfgYrt845Of3y5ToFG5AXj3TLZ97pqaP8
         H5I/XsFPjj1qBkSRNndtaDBlxKDqcyDDCYfVDDyjwCl+ZbedSZ4Qq+3DTWqTkwmZ
         sJYud+AjrIo1vrzelk73Cp5CXZyTjYLZym3F
         -----END CERTIFICATE-----
  - path: /etc/openvpn/client1.crt
    content: |
         Certificate:
         Data:
         Version: 3 (0x2)
         Serial Number: 2 (0x2)
         Signature Algorithm: sha256WithRSAEncryption
         Issuer: C=DE, ST=BA, L=FSN1, O=data, OU=[OmG] Network, CN=data CA/name=EasyRSA/emailAddress=webmaster(AT)omg-network.de
         Validity
         Not Before: Sep  6 15:48:37 2018 GMT
         Not After : Sep  3 15:48:37 2028 GMT
         Subject: C=DE, ST=BA, L=FSN1, O=data, OU=[OmG] Network, CN=client1/name=EasyRSA/emailAddress=webmaster(AT)omg-network.de
         Subject Public Key Info:
         Public Key Algorithm: rsaEncryption
         Public-Key: (2048 bit)
         Modulus:
         00:c7:53:4e:d6:ea:34:da:dd:f7:1a:19:2c:6a:17:
         97:1d:30:a9:51:b9:06:11:50:ef:e8:d9:c5:a2:89:
         9a:89:dc:e8:63:6f:db:5b:4e:37:fc:fb:60:38:45:
         b1:3d:e0:86:d1:c9:66:ee:e8:a9:94:61:3c:40:64:
         7a:e7:76:83:8a:66:ad:66:61:4d:ac:e8:e0:d3:72:
         3b:31:fd:de:0a:44:04:61:7a:51:8f:2b:f6:29:f5:
         1e:9f:46:85:f4:a1:bb:1a:fa:8b:82:f2:27:77:9f:
         f6:be:90:31:03:93:bf:bf:58:97:84:e5:69:81:8a:
         5b:22:ad:1d:eb:fb:a1:c0:c0:04:e8:94:f2:33:1e:
         d5:27:13:2c:b0:23:c9:32:c2:87:12:e9:5a:5a:c6:
         1c:0a:d1:1f:cf:e7:ad:73:68:a0:8f:e2:5a:51:7b:
         1a:1d:45:e6:0c:7d:39:c9:46:79:cf:f7:a3:34:11:
         f6:71:c2:59:7b:8d:94:1e:b0:b6:ea:ff:78:3d:01:
         7b:33:79:1c:31:b0:5e:ed:51:b7:64:8a:9e:ff:e8:
         e6:f1:bf:5e:c5:12:25:a8:b4:03:89:87:ca:69:25:
         b0:70:62:c8:09:36:dc:40:94:e3:70:90:b2:80:f5:
         a2:53:eb:b6:59:55:88:68:65:09:06:4b:d1:71:34:
         b8:7f
         Exponent: 65537 (0x10001)
         X509v3 extensions:
         X509v3 Basic Constraints: 
         CA:FALSE
         Netscape Comment: 
         Easy-RSA Generated Certificate
         X509v3 Subject Key Identifier: 
         93:3F:F7:5C:7C:1C:FD:62:72:C9:AF:8D:7E:2B:B2:E0:F2:6A:9B:B1
         X509v3 Authority Key Identifier: 
         keyid:55:8C:F8:52:42:98:B5:8B:E4:0D:8D:24:5F:9A:5F:7E:4A:1A:B3:3B
         DirName:/C=DE/ST=BA/L=FSN1/O=data/OU=[OmG] Network/CN=data CA/name=EasyRSA/emailAddress=webmaster(AT)omg-network.de
         serial:87:6A:6D:63:08:04:54:FE
         X509v3 Extended Key Usage: 
         TLS Web Client Authentication
         X509v3 Key Usage: 
         Digital Signature
         X509v3 Subject Alternative Name: 
         DNS:client1
         Signature Algorithm: sha256WithRSAEncryption
         31:d5:22:ab:dd:52:0b:46:99:0f:12:9d:da:ea:b4:67:d9:11:
         92:30:23:73:6b:64:93:ef:65:b3:19:a2:2b:08:88:f6:b7:ab:
         aa:a7:2a:be:f4:d2:71:26:d1:bc:27:30:d9:2b:2a:5a:7d:71:
         7b:e6:b3:b2:17:27:44:b5:33:64:0c:9d:19:8d:6f:59:2d:f7:
         87:55:d5:6b:fa:21:5d:37:68:7a:6f:7b:dc:fa:64:1f:9c:20:
         16:93:3d:58:3c:e0:31:12:35:99:47:c7:ea:8f:af:99:ce:72:
         2d:6c:61:eb:f2:c7:a4:85:36:1f:46:db:ae:75:f9:75:f5:51:
         dd:8e:24:5f:8d:76:8e:1c:e7:e1:4d:76:6d:2e:79:7a:d6:df:
         4a:5c:b6:10:3b:8a:82:43:44:d3:32:4d:1d:51:a1:d5:df:78:
         46:f1:3e:5b:c5:c0:a5:0a:31:27:d9:b3:4a:1b:33:a3:05:02:
         36:f2:1a:2b:78:ef:22:3e:ea:70:59:f2:cb:5b:0a:54:46:07:
         1c:3b:fb:06:5c:a1:38:e9:6c:10:d5:c3:a3:b1:a7:17:90:2c:
         90:ce:0a:1f:45:12:a9:e0:34:0c:47:7f:1b:59:ca:66:3c:19:
         32:66:0b:52:33:84:0c:c6:86:8f:a1:4c:7e:1b:fd:98:45:1a:
         05:e9:37:93
         -----BEGIN CERTIFICATE-----
         MIIFITCCBAmgAwIBAgIBAjANBgkqhkiG9w0BAQsFADCBnTELMAkGA1UEBhMCREUx
         CzAJBgNVBAgTAkJBMQ0wCwYDVQQHEwRGU04xMQ0wCwYDVQQKEwRkYXRhMRYwFAYD
         VQQLFA1bT21HXSBOZXR3b3JrMRAwDgYDVQQDEwdkYXRhIENBMRAwDgYDVQQpEwdF
         YXN5UlNBMScwJQYJKoZIhvcNAQkBFhh3ZWJtYXN0ZXJAb21nLW5ldHdvcmsuZGUw
         HhcNMTgwOTA2MTU0ODM3WhcNMjgwOTAzMTU0ODM3WjCBnTELMAkGA1UEBhMCREUx
         CzAJBgNVBAgTAkJBMQ0wCwYDVQQHEwRGU04xMQ0wCwYDVQQKEwRkYXRhMRYwFAYD
         VQQLFA1bT21HXSBOZXR3b3JrMRAwDgYDVQQDEwdjbGllbnQxMRAwDgYDVQQpEwdF
         YXN5UlNBMScwJQYJKoZIhvcNAQkBFhh3ZWJtYXN0ZXJAb21nLW5ldHdvcmsuZGUw
         ggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDHU07W6jTa3fcaGSxqF5cd
         MKlRuQYRUO/o2cWiiZqJ3Ohjb9tbTjf8+2A4RbE94IbRyWbu6KmUYTxAZHrndoOK
         Zq1mYU2s6ODTcjsx/d4KRARhelGPK/Yp9R6fRoX0obsa+ouC8id3n/a+kDEDk7+/
         WJeE5WmBilsirR3r+6HAwATolPIzHtUnEyywI8kywocS6VpaxhwK0R/P561zaKCP
         4lpRexodReYMfTnJRnnP96M0EfZxwll7jZQesLbq/3g9AXszeRwxsF7tUbdkip7/
         6Obxv17FEiWotAOJh8ppJbBwYsgJNtxAlONwkLKA9aJT67ZZVYhoZQkGS9FxNLh/
         AgMBAAGjggFoMIIBZDAJBgNVHRMEAjAAMC0GCWCGSAGG+EIBDQQgFh5FYXN5LVJT
         suDyapuxMIHSBgNVHSMEgcowgceAFFWM+FJCmLWL5A2NJF+aX35KGrM7oYGjpIGg
         MIGdMQswCQYDVQQGEwJERTELMAkGA1UECBMCQkExDTALBgNVBAcTBEZTTjExDTAL
         BgNVBAoTBGRhdGExFjAUBgNVBAsUDVtPbUddIE5ldHdvcmsxEDAOBgNVBAMTB2Rh
         dGEgQ0ExEDAOBgNVBCkTB0Vhc3lSU0ExJzAlBgkqhkiG9w0BCQEWGHdlYm1hc3Rl
         ckBvbWctbmV0d29yay5kZYIJAIdqbWMIBFT+MBMGA1UdJQQMMAoGCCsGAQUFBwMC
         MAsGA1UdDwQEAwIHgDASBgNVHREECzAJggdjbGllbnQxMA0GCSqGSIb3DQEBCwUA
         A4IBAQAx1SKr3VILRpkPEp3a6rRn2RGSMCNza2ST72WzGaIrCIj2t6uqpyq+9NJx
         JtG8JzDZKypafXF75rOyFydEtTNkDJ0ZjW9ZLfeHVdVr+iFdN2h6b3vc+mQfnCAW
         kz1YPOAxEjWZR8fqj6+ZznItbGHr8sekhTYfRtuudfl19VHdjiRfjXaOHOfhTXZt
         Lnl61t9KXLYQO4qCQ0TTMk0dUaHV33hG8T5bxcClCjEn2bNKGzOjBQI28horeO8i
         PupwWfLLWwpURgccO/sGXKE46WwQ1cOjsacXkCyQzgofRRKp4DQMR38bWcpmPBky
         ZgtSM4QMxoaPoUx+G/2YRRoF6TeT
         -----END CERTIFICATE-----
  - path: /etc/openvpn/client1.key
    content: |
         -----BEGIN PRIVATE KEY-----
         MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDHU07W6jTa3fca
         GSxqF5cdMKlRuQYRUO/o2cWiiZqJ3Ohjb9tbTjf8+2A4RbE94IbRyWbu6KmUYTxA
         ZHrndoOKZq1mYU2s6ODTcjsx/d4KRARhelGPK/Yp9R6fRoX0obsa+ouC8id3n/a+
         kDEDk7+/WJeE5WmBilsirR3r+6HAwATolPIzHtUnEyywI8kywocS6VpaxhwK0R/P
         561zaKCP4lpRexodReYMfTnJRnnP96M0EfZxwll7jZQesLbq/3g9AXszeRwxsF7t
         Ubdkip7/6Obxv17FEiWotAOJh8ppJbBwYsgJNtxAlONwkLKA9aJT67ZZVYhoZQkG
         S9FxNLh/AgMBAAECggEBAK0ISNyQnCmTnrrtN30x1WDlqVbkQ7wsgteklMiwo5Mi
         TipkJAxzLm9S2QiAl4ibrO3Y5J5pIy1H68IKeBcO7snqsIS7225LC0EDXRfcxjAr
         M5JbWQnso9lwjJC/6/GdpIubDBk0lcZm+xAapDHyxPYatg4MCTcHIG5N0jfVTWnA
         vmdUXnIp9gnVggWrLJOc+3VjXHZk4/Wd/xtKkUCi7lvegPJ3lX3pzY1S4OvjHl99
         3RHTN/VO5zLHBlGnkKQQMlBJsPQlBz3HZjzz4kLVfre7JioI2FE7jrec3Osz+bWS
         3TVx9lj66QWsj5Jqi5YnbsgrrB1yM5kVjJtbYEwjbaECgYEA8c4Zx/mcRg5KwH2k
         TT0WoVTmWqYpPOqbfZjoC7GmGoThXxhNJndhDWdcFjr34h7j+/1XyO3QnLq9QQvv
         cVZLczohfjdRUpF2BghM0BBu0x0CgYEA0wbQT29qS56SVhSF5pFnycGa6qvwAQ5/
         sgG4wk37O2Q2goZ1fSs4NQv6S7m/LO8rKkjH77b+OTd4AYzinffYgPDxhp28dodc
         ttUdO3+rJczcz3rrd/4eYo8VRjQnT52Ns8OXn65WdDinyZBEmsfWK1vV080kAocR
         HLoIKx6zK0sCgYEAoCWdY5mJC8j5b0WHmK6zerkeLHC8FDTnhmDZZN1pWMCCGf9p
         3iHPQlFkGuU1Fphe0j/AIlUUt6rg/G47dB5qd41wR0dXdpX3R5bW0K/m0BeD4GSK
         7FgSejsjfUGu3R8SZdmjo1sGWFdBcuxBuHGr5PPyLNLcVHAsl9A1d3P6wm0CgYAJ
         PPIfmBwKJW34kLtv5YuqnGwgu9gs46qZa1PgRbOq3O859ZLtINg8EkMpz37cA7hb
         CIagKt2kOZZqUvWUvsXely2rm/olIjXf1yKJeURPylEcUCBAx4IjBGqFAUF7TcVn
         Sje4CNTGD7jgrQ0jzX3FtiZ9OCzMY4dPP6Gd6aEkUwKBgB1T9ZoN1fJ5qRoIQJ6F
         zjw1+sIenf66zEvJbsA/X9oSkXEfxrok5hIGGD4FmXPkjGK9dTd1H7oYwLrhZE0z
         /RsuHBkYjf6kvvRIl6MhNUWif5YznTCnlC0bxpa0lcgSjb87btdNuowdSpTP3h53
         yxfn7iu5lq5pfAgBmutqXOH2
         -----END PRIVATE KEY-----
  - path: /etc/rc.local
    content: |
         #!/bin/sh -e
         #
         # rc.local
         #
         # This script is executed at the end of each multiuser runlevel.
         # Make sure that the script will "exit 0" on success or any other
         # value on error.
         #
         # In order to enable or disable this script just change the execution
         # bits.
         #
         # By default this script does nothing.

         if [ ! -d /var/lib/plexmediaserver ]; then
         /bin/mkdir -p /var/lib/plexmediaserver
         fi
         if [ ! -d /usr/lib/plexmediaserver ]; then
         /bin/mkdir -p /usr/lib/plexmediaserver
         fi
         if [ ! -d /opt/plex/tmp ]; then
         /bin/mkdir -p /opt/plex/tmp
         fi
         if [ ! -d /home/media ]; then
         /bin/mkdir -p /home/media
         fi

         sleep 3

         /bin/mount 10.88.88.1:/var/lib/plexmediaserver /var/lib/plexmediaserver
         /bin/mount 10.88.88.1:/usr/lib/plexmediaserver /usr/lib/plexmediaserver
         /bin/mount 10.88.88.1:/opt/plex/tmp /opt/plex/tmp
         /bin/mount 10.88.88.1:/home/media /home/media

         exit 0
runcmd:
 - [ addgroup, --gid, 1111, plex ]
 - [ useradd, --uid, 1111, --gid, 1111, --shell, /bin/bash, plex, --home-dir, /var/lib/plexmediaserver, --no-create-home ]
 - [ git, clone, "https://github.com/wnielson/Plex-Remote-Transcoder" ]
 - [ cd, Plex-Remote-Transcoder/ ]
 - [ python2.7, setup.py, install ]
 - [ sed, -i, 's/#AUTOSTART="all"/AUTOSTART="client"/g', /etc/default/openvpn ]
 - [ sh, -c, "systemctl daemon-reload && systemctl enable openvpn && systemctl restart openvpn" ]
 - [ sh, -c, "chmod +x /etc/rc.local && /etc/rc.local" ]
 ```
## Master Node Configuration
### OpenVPN Configuration
```ovpn
port 1194
proto udp
dev tun
ca /etc/openvpn/easy-rsa/keys/ca.crt
cert /etc/openvpn/easy-rsa/keys/server.crt
key /etc/openvpn/easy-rsa/keys/server.key
dh /etc/openvpn/easy-rsa/keys/dh2048.pem
duplicate-cn
server 10.88.88.0 255.255.255.0
keepalive 10 120
comp-lzo
user nobody
group nogroup
persist-key
persist-tun
status openvpn-status.log
verb 3
```
### NFS Share Configuration
```
/var/lib/plexmediaserver 10.88.88.*(ro,sync,no_subtree_check)
/usr/lib/plexmediaserver 10.88.88.*(ro,sync,no_subtree_check)
/opt/plex/tmp 10.88.88.*(rw,sync,no_subtree_check)
/home/media 10.88.88.*(rw,sync,no_subtree_check)
```
### Configure OpenSSH Client [Master]
To prevent SSH connection errors.
Adding the following to the <code>/etc/ssh/ssh_config</code> file.
```bash
   StrictHostKeyChecking no
   UserKnownHostsFile=/dev/null
```
### SSH Key Management
All SSH key configuration can done on the Master server, because the plex home folder ist shared to the transcode worker.

### Automatic Host Add / Remove
Needs a way to Add and Remove Hosts from the <code>.prt.conf</code>

Using the <code>prt</code> utility needs a yes / no input to confirm the input.
```bash
plex@plex-main:~$ prt add_host 192.168.11.1 22 plex y
We´re going to add the following transcode host:
  Host: 192.168.11.1
  Port: 22
  User: plex
Proceed: [y/n]
```
Removed the Yes / No switch from the Python source code.
Changed Python source of <code>prt.py</code> Line 665-697
```python
    elif sys.argv[1] == "add_host":
        host = None
        port = None
        user = None
        key  = None
        if len(sys.argv) >= 3:
            host = sys.argv[2]
        if len(sys.argv) >= 4:
            port = sys.argv[3]
        if len(sys.argv) >= 5:
            user = sys.argv[4]
        if len(sys.argv) >= 6:
            key = sys.argv[5]

        if host is None:
            host = raw_input("Host: ")
        if port is None:
            port = raw_input("Port: ")
        if user is None:
            user = raw_input("User: ")
        if key is None:
            key = raw_input("Proceed: ")

        if key  == "y":
            config = get_config()
            config["servers"][host] = {
                "port": port,
                "user": user
            }

            if save_config(config):
                print "Host successfully added"
```