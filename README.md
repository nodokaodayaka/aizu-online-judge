# aizu-online-judge

# Python env setting from my Mac

## pyenv install & env setting

```
$ git clone https://github.com/pyenv/pyenv.git ~/.pyenv

$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
$ echo 'eval "$(pyenv init -)"' >> ~/.bashrc
```

## How to

### pyenv version

```
$ pyenv -v
pyenv 1.2.18-12-g098227f2
```

### show pyton list

```
pyenv install --list
```

### install target python version

```
pyenv install 3.6.1
$ pyenv install 3.8.2
Downloading openssl-1.1.0j.tar.gz...
-> https://www.openssl.org/source/old/1.1.0/openssl-1.1.0j.tar.gz
Installing openssl-1.1.0j...
.....

```


### use target python version for global

```
$ pyenv global 3.6.1
$ python --version
```

### use target python version for local

```
$ cd dir
$ pyenv local 3.6.1
$ python --version
```

