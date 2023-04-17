import numpy as np
import matplotlib.pyplot as plt

# Define the initial investment, interest rate, and time period
initial_investment = int(input("Enter initial investment value: $"))
annual_investment = int(input("Enter annual recurring investment value: $"))
years = int(input("Enter investment horizon in years: "))
interest_rate_6pc = 0.06
interest_rate_9pc = 0.09

# Calculate the future value using the compound interest formula
future_value_6pc = (annual_investment * years + initial_investment) * (1 + interest_rate_6pc)**years
future_value_9pc = (annual_investment * years + initial_investment) * (1 + interest_rate_9pc)**years

print(f"The future value is: ${future_value_6pc:.2f} at 6% IRR.")
print(f"The future value is: ${future_value_9pc:.2f} at 9% IRR.")

# Create a list of years for the x-axis of the graph
x_values = np.arange(years + 1)

# Create a list of future values for the y-axis of the graph
y_values_9pc = [(annual_investment * years + initial_investment) * (1 + interest_rate_9pc)**i for i in x_values]
y_values_6pc = [(annual_investment * years + initial_investment) * (1 + interest_rate_6pc)**i for i in x_values]

# Create a line graph of the future value over time
plt.plot(x_values, y_values_6pc)
plt.plot(x_values, y_values_9pc)
plt.xlabel('Years')
plt.ylabel('Future Value')
plt.title('Investment Growth Over Time')
plt.show()

