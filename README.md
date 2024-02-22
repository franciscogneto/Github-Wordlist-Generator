# Script that generate a wordlist based in a github repository

Basically this script generate a wordlist based in the giver repository. But it doesn't do recursively.

> [!IMPORTANT]
> It doesn't need API KEY


## Installing dependencies 
```bash
pip3 install beautifulsoup4
```

## How it works

```bash
python3 githubWordlistGenerator.py -u <url to the repository> -o <output file>
```

## Examples
```bash
python3 githubWordlistGenerator.py -u https://github.com/ipfire/ipfire-2.x/ -o ipfireWordlist
```
```bash
python3 githubWordlistGenerator.py -u https://github.com/ipfire/ipfire-2.x/tree/master/html/cgi-bin -o ipfireWordlist
```
