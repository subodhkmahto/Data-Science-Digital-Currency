import pandas as pd
import matplotlib.pyplot as plt

# Load data into a DataFrame
data = pd.read_csv(r'prices/BTC-USD.csv', parse_dates=['Date'])  # Ensure 'Date' is parsed as datetime
print(data.describe())

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(data['Date'], data['Close'], label='Close Price', color='blue', marker='o')

# Customize the plot
plt.title('Stock Close Prices Over Time', fontsize=14)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Close Price', fontsize=12)
plt.grid(True)
plt.legend()
plt.tight_layout()

# Show the plot
plt.show()
