import pandas as pd

class SignalExpiration:
    def __init__(self, data, expiration_time='1m'):
        self.data = data
        self.expiration_time = expiration_time

    def apply_signal_expiration(self):
        """
        Apply expiration time to signals.
        """
        time_conversion = {
            '5 sec': '5S', '10 sec': '10S', '15 sec': '15S', '30 sec': '30S',
            '1m': '1T', '2m': '2T', '3m': '3T', '4m': '4T', '5m': '5T',
            '10m': '10T', '15m': '15T', '30m': '30T', '1hr': '1H', '4hr': '4H', '1d': '1D'
        }
        expiration_duration = pd.to_timedelta(time_conversion[self.expiration_time])

        self.data['Signal_Expiration'] = self.data.index + expiration_duration
        self.data['Active_Signal'] = 0

        for i in range(len(self.data)):
            if self.data['Signal'].iloc[i] != 0:  # Signal is generated
                expiration_time = self.data['Signal_Expiration'].iloc[i]
                self.data.loc[self.data.index[i]:self.data.index.searchsorted(expiration_time), 'Active_Signal'] = self.data['Signal'].iloc[i]

        return self.data
