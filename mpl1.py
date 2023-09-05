import random
from itertools import count 
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mplfinance.original_flavor import candlestick_ohlc
import matplotlib.dates as mpl_dates
from datetime import datetime

plt.style.use('ggplot')

base_time : datetime = datetime.today()

columns = ['date', 'open', 'high', 'low', 'close']
df = pd.DataFrame(columns=columns)
#df.set_index('date')

fig, ax = plt.subplots()

candlestick_ohlc(ax, df.values, width = 0.6, colorup='green', colordown='red', alpha=0.8)

ax.set_xlabel('Date')
ax.set_ylabel('Price')

index = count(5)

def rand_candle():
    global df
    open = random.randint(0, 10) if df.empty else df['close'].iloc[-1]
    close = random.randint(0, 10)
    high = random.randint(open if open > close else close, 10)
    low = random. randint(0, open if open < close else close)
    df2 = pd.DataFrame.from_dict({'date' : next(index), 
                'open' : [open],
                'close' : [close],
                'high' : [high],
                'low' : [low] 
    })
    #df2.set_index('date')
    df = pd.concat([df, df2])


def animate(i):
    rand_candle()
    plt.cla()
    candlestick_ohlc(ax, df.values, width = 0.6, colorup='green', colordown='red', alpha=0.8)
    print(df)

ani = FuncAnimation(fig, animate, interval=1000)

fig.autofmt_xdate()
fig.tight_layout()
rand_candle()
plt.show()