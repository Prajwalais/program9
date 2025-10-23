def calculate_bmi(weight, height):
    return weight / (height ** 2)

if __name__ == "__main__":
    weight = float(input("Enter weight (kg): "))
    height = float(input("Enter height (m): "))
    
    bmi = calculate_bmi(weight, height)
    
    print(f"Weight: {weight} kg")
    print(f"Height: {height} m")
    print(f"BMI: {bmi:.1f}")
