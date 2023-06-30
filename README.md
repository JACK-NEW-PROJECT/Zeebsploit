![Zeebsploit|framework](https://img.shields.io/badge/Zeebsploit-Framework-orange.svg)
![python|3.x](https://img.shields.io/badge/python-3.x-blue.svg)
- 2021: I hope someone can rebuild my tool
- 2022: whyyy??
- 2023 : THIS PROJECT WILL BE CLOSED 



<img src="zeeb_src/utils/Zeebsploit.png" width="250" height="250">

#### Installation
```
$ apt-get install git python
$ git clone https://github.com/jaxBCD/Zeebsploit.git
$ cd Zeebsploit
$ python -m pip install -r requirements.txt
$ python zsf.py
$ * and follow instruction
```
* exploits 17
* scanners 11
* footprinting 10


#### Docker Build

 ```
 $ docker build -t xshuden/zeebsploit .
 ```

#### Docker Usage

 ```
 $ docker run --rm -it xshuden/zeebsploit
 $ docker run --rm -it -v '$(pwd):/tmp/' xshuden/zeebsploit
 ```


##### requirements:

required:
* requests
* asyncio
* aiohttp
* python-whois
* bs4
* dirhunt
* colorlog

#### last update:

<br>wed, 28 apr 2019<br>
new:
* update version to 1.1
* fix error
* add new modules
