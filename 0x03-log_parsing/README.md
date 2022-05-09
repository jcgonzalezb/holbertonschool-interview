# Python - Log Parsing

## Description of the files inside this folder:

0. A script that reads stdin line by line and computes metrics.
```
- Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
```

After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics from the beginning.

```
- Total file size: File size: <total size>, where <total size> is the sum of all previous <file size>.
- Number of lines by status code: <status code>: <number>.
```
- Possible status code: 200, 301, 400, 401, 403, 404, 405 and 500.
- Status codes should be printed in ascending order.
- If a status code doesn’t appear or is not an integer, don’t print anything for this status code.


## Languages and Tools:

- OS: Ubuntu 20.04 LTS
- Language: Python 3.8.10
- Style guidelines: [PEP 8](https://www.python.org/dev/peps/pep-0008/)

<p align="left"> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>


## Author

- Juan Camilo González <a href="https://twitter.com/juankter" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="juankter" height="30" width="40" /></a>
<a href="https://bit.ly/2MBNR0t" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="https://bit.ly/2mbnr0t" height="30" width="40" /></a>
