Clone the repository :

```console
kali@kali:~$ git clone
```

Install Python Libraries :

```console
kali@kali:~$ pip install argparse
kali@kali:~$ pip install Wave
kali@kali:~$ sudo pip install opencv-python
kali@kali:~$ pip install numpy
kali@kali:~$ pip install Pillow
kali@kali:~$ pip install pytest-shutil
kali@kali:~$ pip install subprocess.run
kali@kali:~$ sudo pip install stegano
```

## How To Use?

To Use The Code:

```console
kali@kali:~$ cd Steganography
kali@kali:~$ sudo python3 ./Steganography.py <File Type> <Encode/Decode> <File Location>
```

For Audio Cover File:

```console
# Encoding
    kali@kali:~$ sudo python3 ./Steganography.py -a -e <location of file>
    kali@kali:~$ sudo python3 ./Steganography.py --audio --encode <location of file>
# Decoding
    kali@kali:~$ sudo python3 ./Steganography.py -a -d <location of file>
    kali@kali:~$ sudo python3 ./Steganography.py --audio --decode <location of file>
```

For Video Cover File :

```console
# Encoding
    kali@kali:~$ sudo python3 ./Steganography.py -v -e <location of file>
    kali@kali:~$ sudo python3 ./Steganography.py --video --encode <location of file>
# Decoding
    kali@kali:~$ sudo python3 ./Steganography.py -v -d <location of file>
    kali@kali:~$ sudo python3 ./Steganography.py --video --decode <location of file>
```

For Image Cover File :

```console
# Encoding
    kali@kali:~$ sudo python3 ./Steganography.py -i -e <location of file>
    kali@kali:~$ sudo python3 ./Steganography.py --image --encode <location of file>
# Decoding
    kali@kali:~$ sudo python3 ./Steganography.py -i -d <location of file>
    kali@kali:~$ sudo python3 ./Steganography.py --image --decode <location of file>
```

For Text Cover File :

```console
# Encoding
    kali@kali:~$ sudo python3 ./Steganography.py -t -e <location of file>
    kali@kali:~$ sudo python3 ./Steganography.py --text --encode <location of file>
# Decoding
    kali@kali:~$ sudo python3 ./Steganography.py -t -d <location of file>
    kali@kali:~$ sudo python3 ./Steganography.py --text --decode <location of file>
```

## Demo :

```console
┌──(kali㉿kali)-[~/Desktop]
└─$ cd Steganography

┌──(kali㉿kali)-[~/Desktop/Steganography]
└─$ ls
libs  Steganography.py

┌──(kali㉿kali)-[~/Desktop/Steganography]
└─$ sudo python3 ./Steganography.py -v -e /home/kali/Desktop/Test/test.mp4
[sudo] password for kali:

[INFO] Video Steganography ENCODING

[*] Enter the message :hii
[INFO] temp directory is created
[INFO] frame ./temp/0.png holds h
[INFO] frame ./temp/1.png holds i
[INFO] frame ./temp/2.png holds i
[INFO] The message is stored in the Embedded_Video.mp4 file
[INFO] temp files are cleaned up
[INFO] FILE LOCATION:/home/kali/Desktop/Test/test.mp4

┌──(kali㉿kali)-[~/Desktop/Steganography]
└─$ sudo python3 ./Steganography.py -v -d /home/kali/Desktop/Test/test.mp4

[INFO] Video Steganography DECODING

[INFO] temp directory is created

[*] The Encoded data was:hii

[INFO] temp files are cleaned up
```

## Authors :

- [@Ronit_Jena](https://github.com/ronitjena09)
- [@Kausik_Kishore_Mishra](https://github.com/KKmishra24)

## Disclaimer

**"EDUCATIONAL PURPOSES ONLY"**

######

## Legal Disclaimer

The use of code contained in this repository, either in part or in its totality,
for engaging targets without prior mutual consent is illegal. **It is
the end user's responsibility to obey all applicable local, state and
federal laws.**

Developers assume **no liability** and are not
responsible for misuses or damages caused by any code contained
in this repository in any event that, accidentally or otherwise, it comes to
be utilized by a threat agent or unauthorized entity as a means to compromise
the security, privacy, confidentiality, integrity, and/or availability of
systems and their associated resources. In this context the term "compromise" is
henceforth understood as the leverage of exploitation of known or unknown vulnerabilities
present in said systems, including, but not limited to, the implementation of
security controls, human- or electronically-enabled.

The use of this code is **only** endorsed by the developers in those
circumstances directly related to **educational environments** or
**authorized penetration testing engagements** whose declared purpose is that
of finding and mitigating vulnerabilities in systems, limiting their exposure
to compromises and exploits employed by malicious agents as defined in their
respective threat models.

######

The application must be used for **"EDUCATIONAL PURPOSES ONLY"**

### Contact Us on:

###### **RONIT JENA** : https://www.linkedin.com/in/ronit-jena-02a3b7146/

###### **KAUSIK KISHORE MISHRA** : https://github.com/KKmishra24
