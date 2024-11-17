import pandas as pd
import numpy as np
from signal_generator import SignalGenerator
from signal_expiration import SignalExpiration
from visualization import SignalVisualizer

# Example usage
if __name__ == "__main__":
    # Example data (Random for demonstration)
    np.random.seed(42)
    dates = pd.date_range('2023-01-01', periods=200, freq='S')  # Second-level data for fine granularity
    close_prices = np.random.normal(loc=100, scale=5, size=(200,))
    high_prices = close_prices + np.random.uniform(1, 5, size=(200,))
    low_prices = close_prices - np.random.uniform(1, 5, size=(200,))
    volume = np.random.randint(100, 1000, size=(200,))

    data = pd.DataFrame({'Close': close_prices, 'High': high_prices, 'Low': low_prices, 'Volume': volume}, index=dates)

    # Specify market type and expiration time
    market_type = 'Live'
    expiration_time = '1m'  # Change this to any of the provided time intervals

    # Initialize and run the signal generator
    signal_generator = SignalGenerator(data)
    signal_generator.calculate_indicators()
    data_with_signals = signal_generator.generate_signals()

    # Apply signal expiration
    signal_expiration = SignalExpiration(data_with_signals, expiration_time)
    data_with_expiration = signal_expiration.apply_signal_expiration()

    # Visualize signals
    signal_visualizer = SignalVisualizer(data_with_expiration, market_type, expiration_time)
    signal_visualizer.visualize_signals()
