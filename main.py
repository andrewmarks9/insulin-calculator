from save_results import save_results_to_csv


print("Insulin Bolus Calculator")
print("This program calculates an insulin bolus for a meal based on carb ratio and insulin sensitivity factor.")
print("Using mg/dL units")
print("This info is for educational purposes only. Consult your healthcare provider for medical advice.")

# Get user inputs
carb_ratio = float(input("Enter carb ratio (grams of carbs per unit of insulin): "))
sensitivity_factor = float(input("Enter insulin sensitivity factor (mg/dL per unit): "))
target_glucose = float(input("Enter target blood glucose level (mg/dL): "))
current_glucose = float(input("Enter current blood glucose level (mg/dL): "))
meal_carbs = float(input("Enter grams of carbs for the meal: "))
iob = float(input("Enter insulin on board (units): "))

# Calculate insulin doses
carb_dose = meal_carbs / carb_ratio
correction_dose = (current_glucose - target_glucose) / sensitivity_factor

# Calculate total insulin bolus
total_bolus = carb_dose + correction_dose

# Adjust for insulin on board
adjusted_bolus = total_bolus - iob

# Round bolus to nearest 0.5 units
adjusted_bolus = round(adjusted_bolus * 2) / 2
print (f"Adjusted Bolus is {adjusted_bolus} units")

# Calculate estimated blood glucose after bolus
#estimated_glucose = int(round(current_glucose - (adjusted_bolus * sensitivity_factor)))
# estimated_glucose = current_glucose - adjusted_bolus - sensitivity_factor
#print(f"Estimated blood glucose after bolus: {estimated_glucose} mg/dL")


# Display results
print(f"\nRecommended insulin bolus: {adjusted_bolus} units")
print(f"Current blood glucose: {current_glucose} mg/dL")
print(f"Target blood glucose: {target_glucose} mg/dL")
#print(f"Estimated blood glucose after bolus: {estimated_glucose} mg/dL")

# Call the save_results_to_csv function with the relevant data
save_results_to_csv(carb_ratio, sensitivity_factor, target_glucose, current_glucose, meal_carbs, iob, adjusted_bolus)
