# [Freqtrade](https://www.freqtrade.io/en/stable/)

## Freqtrade basic
### Freqtrade terminology
>- Strategy: Your trading strategy, telling the bot what to do.
>- Trade: Open position.
>- Open Order: Order which is currently placed on the exchange, and is not yet complete.
>- Pair: Tradable pair, usually in the format of Base/Quote(e.g, XRP/USDT).
>- Timeframe: Candle length to use(e.g, "5m","1h"...).
>- Indicators: Technical indicators(SMA, EMA, RSI...).
>- Limit Order: Limit orders which execute at the defined limit price or better.
>- Market Order: Guaranteed to fill, may move price depending on the order size.

### Fee handling
> All profit calculations of Freqtrade include fees. For Backtesting/Hyperopt/Dry-run modes, the exchange default fee is used(lowest tier on the exchange). For live operations, fees are used as applied by the exchange.

### Bot execution logic
>- Fetch open trades from persistence.
>- Calculate current list of tradable pairs.
>- Download ohlcv data for the pairlist including all informative paris.
   This step is only executed once per candle to avoid unnecessary network traffic.
>- Call bot_loop_start() strategy callback.   
>- Analyze strategy per pair.
   >>- Call populate_indicators()
   >>- Call populate_buy_trend()
   >>- Call populate_sell_trend()
>- Check timeouts for open orders.
   >>- Calls check_buy_timeout() strategy callback for open buy orders.
   >>- Calls check_sell_timeout() strategy callback for open sell orders.
>- Verify existing positions and eventually places sell orders.
   >>- Considers stopless, ROI and sell-signal, custom_sell() and custom_stoploss().
   >>- Determine sell-price based on ask_strategy configuration setting or by using the custom_exit_price() callback.
   >>- Before a sell order is placed, confirm_trade_exit() strategy callback is called.
>- Check if trade-slots are still available(if max_open_trades is reached).
>- Verifies buy signal trying to enter new positions.
    >>- Determine buy-price based on bid_strategy configuration setting, or by using the custom_entry_price() callback.
    >>- Determine stake size by calling the custom_stake_amount() callback.
    >>- Before a buy order is placed, confirm_trade_entry() strategy callback is called.

> This loop will be repeated again and again until the bot is stopped.

### Backtesting / Hyperopt execution logic
>- Load historic data for configured pairlist.
>- Calls bot_loop_start() once.
>- Calculate indicators(calls populate_indicators() once per pair).
>- Calculate buy/sell signals(calls populate_buy_trend() and populate_sell_trend() once per pair).
>- Loops per candle simulating entry and exit points.
   >>- Confirm trade buy/sell(calls confirm_trade_entry() and confirm_trade_exit() if implemented in the strategy).
   >>- Call custom_stopless() and custom_sell() to find custom exit points.
>- Generate backtest report output.

> Both Backtesting and Hyperopt include exchange default fees in the calculation. Custom fees can be passed to backtesting/hyperopt by specifiying the --fee argument.

## Strategy Customization
### Deploy your own strategy
#### Anatomy of a strategy
> A strategy file contains all the information needed to build a good strategy:
   >>- Indicators
   >>- Buy strategy rules
   >>- Sell strategy rules
   >>- Minimal ROI recommended
   >>- Stopless strongly recommended

#### Dataframe
> Freqtrade uses [pandas](https://pandas.pydata.org/) to store/provide the candlestick(OHLCV) data.
> Each row in a dataframe corresponds to one candle on a chart, with the latest candle always being the last in the dataframe(sorted by date).

> As a dataframe is a table, simple python comparisions like the following will not work
>```
> if dataframe['rsi'] > 30:
>     dataframe['buy'] = 1
>```
> The above section will fail with The truth value of a series is ambiguous.
> This must instead be written in a pandas-compatible way, so the operation is performed across the whole dataframe.
>```
> dataframe.loc[
>      (dataframe['rsi'] > 30)
>      , 'buy'] = 1
>```
> With this section, you have a new column in your dataframe, which has 1 assigned whenever RSI is above 30.

#### Customize Indicators
> Buy and sell strategies need indicators. You can add more indicators by extending the list contained in the method populate_indicators() from your strategy file.

> You should only add the indicators used in either populate_buy_trend() or populate_sell_trend(), or to populate another indicator, otherwise performance may suffer.

> It's important to always return the dataframe without removing/modifing the columns "open","hight","low","close","volumn", otherwise these fields would contain something unexpected.

#### Strategy startup period
> Most indicators have an instable startup period, in which they are either not available(NaN), or the calculation is incorrect. This can lead to inconsistancies, since Freqtrade does not know how long this instable period should be. To account for this, the strategy can be assigned the startup_candle_count attribute. This should be set to the maximum number of candles that the strategy requires to calculate stable indicators.

#### Buy signal rules
> populate_buy_trend() will define a new column, "buy", which needs to contain 1 for buys, and 0 for "no action".

> Buying requires sellers to buy from - therefore volumn needs to be > 0(dataframe['volumn'] > 0) to make sure that the bot does not buy/sell in no-activity periods.

#### Sell signal rules
> populate_sell_trend() will define a new column, "sell", which needs to contain 1 for sells, and 0 for "no action".

#### Minimal ROI
> This dict defines the minimal Return On Investment(ROI) a trade should reach before selling, independent from the sell signal.

> The calculation does include fees.

#### Stoploss
> Setting a stoploss is highly recommended to protect your capital from strong moves against you.

#### Timeframe
> This is set of candles the bot should download and use for the analysis. Common values are "1m","5m","15m","1h", however all values supported by your exchange should work.

> Please note that the same buy/sell signals may work well with one timeframe, but not with the others.

### Strategy file loading
> By default, freqtrade will attempt to load strategies from all .py files within user_data/strategies.

> Note that we're using the class-name, not the file name.

### Informative Pairs
#### Get data from non-tradable pairs
> Data for additional, informative pairs(reference pairs) can be beneficial for some strategies. OHLCV data for these pairs will be downloaded as part of the regular whitelist refresh process and is available via DataProvider just as other pairs.

> As these pairs will be refreshed as part of the regular whitelist refresh, it's best to keep this list short.

#### Additional data(DataProvider)
> The strategy provides access to the DataProvider. This allows you to get additional data to use in your strategy.

#### Prevent trades from happening for a specific pair
> Freqtrade locks pairs automatically for the current candle(until the candle is over) when a pair is sold, preventing an immediate re-buy of that pair.



