# doc-tool
auto-generate python source code header docs

# usage

run `docs -h`

``` shell
usage: python source code doc generate tool. [-h] author [docs [docs ...]]

positional arguments:
  author      File create author
  docs        module function description

optional arguments:
  -h, --help  show this help message and exit
```

run `python docs.py 'yourname' description > newfile.py` to generate new doc ready file.

# install

1. clone this repo
2. add execute to `docs.py` use `chmod`
3. rename and move to `/bin` dir

``` shell

git clone https://github.com/smileboywtu/doc-tool
cd doc-tool

chmod +x docs.py

sudo mv docs.py /usr/local/bin/pydocs

```

# lisence

MIT
