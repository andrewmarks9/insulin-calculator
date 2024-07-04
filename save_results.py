import csv
import os
from datetime import date, datetime

def save_results_to_csv(carb_ratio, sensitivity_factor, target_glucose, current_glucose, meal_carbs, iob, adjusted_bolus):
    today = date.today().strftime("%Y-%m-%d")
    log_filename = f"results_{today}.csv"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Create the log file if it doesn't exist
    if not os.path.exists(log_filename):
        with open(log_filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Timestamp", "Carb Ratio", "Sensitivity Factor", "Target Glucose", "Current Glucose", "Meal Carbs", "IOB", "Adjusted Bolus"])

    # Append the log entry to the CSV file
    data = [timestamp, carb_ratio, sensitivity_factor, target_glucose, current_glucose, meal_carbs, iob, adjusted_bolus]

    with open(log_filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

    print(f"Results saved to {log_filename}")
