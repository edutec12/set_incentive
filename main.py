import random
import time

# Define the parameters of the model
n_hours = 24
peak_hours = [16, 17, 18, 19, 20]
incentive = 0.2
ac_cycles = 4

# Simulate the daily operation of the electric grid
for hour in range(n_hours):
    # Check if it's a peak hour
    if hour in peak_hours:
        # Determine if the air conditioner should be cycled off
        if random.uniform(0, 1) < 1 / ac_cycles:
            # Cycle off the air conditioner
            print(f"Cycling off the air conditioner at hour {hour}")
            time.sleep(1)
        else:
            # Keep the air conditioner running
            print(f"Air conditioner running at hour {hour}")
            time.sleep(1)
    else:
        # Keep the air conditioner running
        print(f"Air conditioner running at hour {hour}")
        time.sleep(1)

# Calculate the incentive for the customer
incentive_amount = ac_cycles * incentive
print(f"The customer will receive an incentive of ${incentive_amount:.2f} for participating in the demand response program.")
