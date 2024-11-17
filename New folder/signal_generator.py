import pandas as pd
import talib

class SignalGenerator:
    def __init__(self, data):
        self.data = data

    def calculate_indicators(self):
        """
        Calculate the requested indicators.
        """
        self.data['RSI'] = talib.RSI(self.data['Close'], timeperiod=14)  # Example: RSI
        self.data['MACD'], self.data['MACD_signal'], _ = talib.MACD(
            self.data['Close'], fastperiod=12, slowperiod=26, signalperiod=9)  # Example: MACD

    def generate_signals(self):
        """
        Generate signals based on indicators.
        """
        self.data['Signal'] = 0  # Initialize Signal column
        self.data.loc[self.data['RSI'] < 30, 'Signal'] = 1  # RSI oversold (Buy)
        self.data.loc[self.data['RSI'] > 70, 'Signal'] = 0  # RSI overbought (Sell)
        return self.data
