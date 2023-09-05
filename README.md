# mpl_updating_candlestick

this library can be used as an example for a updating candlestick chart using matplotlib and mplfinance

setup and start venv (not required):

```shell
py -m venv .
.\Scripts\activate
```

install required libraries from requirements.txt

```shell
pip install -r requirements.txt
```

run graphic

```shell
py mpl1.py
```

## known errors

matplotlib has no gui by default, so if your OS system does not have any gui module installed it won't work. On linux you can for example solve this problem by installing tk

```
sudo apt-get install python3-tk
```
