import numpy as np
import matplotlib.pyplot as plt

# Define the initial investment, interest rate, and time period
initial_investment = int(input("Enter initial investment value: "))
annual_investment = int(input("Enter annual recurring investment value: "))
interest_rate = int(input("Enter annualised rate of return in %: ")) / 100
years = int(input("Enter investment horizon in years: "))

# Calculate the future value using the compound interest formula
future_value = (annual_investment * years + initial_investment) * (1 + interest_rate)**years

print(f"The future value is: ${future_value:.2f}.")
# Create a list of years for the x-axis of the graph
x_values = np.arange(years + 1)

# Create a list of future values for the y-axis of the graph
y_values = [(annual_investment * years + initial_investment) * (1 + interest_rate)**i for i in x_values]

# Create a line graph of the future value over time
plt.plot(x_values, y_values)
plt.xlabel('Years')
plt.ylabel('Future Value')
plt.title('Investment Growth Over Time')
plt.show()
