# doc-tool
auto-generate python source code header docs

# usage

run `docs -h`

``` shell
usage: python source code doc generate tool. [-h] [-u AUTHOR]
                                             [-m [DESCRIPTION [DESCRIPTION ...]]]

optional arguments:
    -h, --help            show this help message and exit
    -u AUTHOR, --author AUTHOR File create author
    -m [DESCRIPTION [DESCRIPTION ...]], --description [DESCRIPTION [DESCRIPTION ...]] module function description

```

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
