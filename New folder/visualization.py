import matplotlib.pyplot as plt

class SignalVisualizer:
    def __init__(self, data, market_type, expiration_time):
        self.data = data
        self.market_type = market_type
        self.expiration_time = expiration_time

    def visualize_signals(self):
        """
        Visualize signals and active signals on the chart.
        """
        plt.figure(figsize=(14, 10))
        plt.plot(self.data['Close'], label='Close Price', color='blue')

        # Active signals
        buy_signals = self.data[self.data['Active_Signal'] == 1]
        sell_signals = self.data[self.data['Active_Signal'] == 0]
        plt.scatter(buy_signals.index, buy_signals['Close'], label='Active Buy Signal', marker='^', color='green', alpha=1)
        plt.scatter(sell_signals.index, sell_signals['Close'], label='Active Sell Signal', marker='v', color='red', alpha=1)

        plt.title(f"{self.market_type} Market Signals with {self.expiration_time} Expiration")
        plt.legend()
        plt.show()
