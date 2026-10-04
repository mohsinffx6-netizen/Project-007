def calculate_bmi_metric(weight_kg, height_m):
    """Calculates BMI using standard metric units."""
    return weight_kg / (height_m ** 2)

def calculate_bmi_imperial(weight_lbs, height_in):
    """Calculates BMI using standard imperial units."""
    return (weight_lbs / (height_in ** 2)) * 703

def get_bmi_category(bmi):
    """Categorizes the BMI value according to standard ranges."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight (Healthy)"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("=== Welcome to the Python BMI Calculator ===")
    
    # 1. Choose Unit System
    while True:
        choice = input("Choose unit system - Enter '1' for Metric (kg/m) or '2' for Imperial (lbs/in): ").strip()
        if choice in ['1', '2']:
            break
        print("Invalid choice. Please enter 1 or 2.\n")
        
    # 2. Get User Input with Error Handling
    while True:
        try:
            if choice == '1':
                weight = float(input("Enter your weight in kilograms (e.g., 70): "))
                height = float(input("Enter your height in meters (e.g., 1.75): "))
            else:
                weight = float(input("Enter your weight in pounds (e.g., 150): "))
                height = float(input("Enter your height in inches (e.g., 68): "))
                
            if weight <= 0 or height <= 0:
                print("Weight and height must be positive numbers. Please try again.\n")
                continue
            break
        except ValueError:
            print("Invalid numeric input. Please enter numbers only.\n")

    # 3. Calculate BMI
    if choice == '1':
        bmi = calculate_bmi_metric(weight, height)
    else:
        bmi = calculate_bmi_imperial(weight, height)

    # 4. Display Results
    category = get_bmi_category(bmi)
    print("\n" + "="*35)
    print(f"Your calculated BMI is: {bmi:.2f}")
    print(f"Weight Category: {category}")
    print("="*35)

if __name__ == "__main__":
    main()
    