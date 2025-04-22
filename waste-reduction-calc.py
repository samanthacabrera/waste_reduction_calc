def waste_reduction_calculator():
    print("Welcome to the Waste Reduction Calculator!")
    
    plastic_bottles = int(input("How many plastic bottles do you use weekly? "))
    aluminum_cans = int(input("How many aluminum cans do you use weekly? "))
    paper_boxes = int(input("How many paper boxes do you use weekly? "))
    plastic_bags = int(input("How many plastic bags do you use weekly? "))
    
    # Average weights (in pounds) for each item
    plastic_bottle_weight = 0.5  # lbs per bottle
    aluminum_can_weight = 0.3  # lbs per can
    paper_box_weight = 1  # lbs per box
    plastic_bag_weight = 0.05  # lbs per bag
    
    # Calculate total waste in pounds
    total_plastic_waste = plastic_bottles * plastic_bottle_weight
    total_aluminum_waste = aluminum_cans * aluminum_can_weight
    total_paper_waste = paper_boxes * paper_box_weight
    total_plastic_bag_waste = plastic_bags * plastic_bag_weight
    
    # Convert to annual waste (in pounds)
    total_plastic_waste_annual = total_plastic_waste * 52
    total_aluminum_waste_annual = total_aluminum_waste * 52
    total_paper_waste_annual = total_paper_waste * 52
    total_plastic_bag_waste_annual = total_plastic_bag_waste * 52
    
    print("\nYour annual waste generation is as follows:")
    print(f"Plastic waste (bottles): {total_plastic_waste_annual:.2f} lbs")
    print(f"Aluminum can waste: {total_aluminum_waste_annual:.2f} lbs")
    print(f"Paper box waste: {total_paper_waste_annual:.2f} lbs")
    print(f"Plastic bag waste: {total_plastic_bag_waste_annual:.2f} lbs")
    
    # Waste reduction suggestions
    print("\nWaste Reduction Suggestions:")
    
    if plastic_bottles > 0:
        print("- Reduce plastic bottle usage by switching to reusable bottles.")
        print("- Recycle plastic bottles properly.")
    
    if aluminum_cans > 0:
        print("- Recycle aluminum cans and reduce single-use beverage containers.")
    
    if paper_boxes > 0:
        print("- Consider reusing paper boxes or recycling them.")
    
    if plastic_bags > 0:
        print("- Switch to reusable bags to reduce plastic bag waste.")
    
    # Calculate waste savings (in pounds)
    print("\nBy following the suggestions, here’s how much waste you could save annually:")
    plastic_savings = total_plastic_waste_annual * 0.3  # 30% reduction
    aluminum_savings = total_aluminum_waste_annual * 0.5  # 50% reduction
    paper_savings = total_paper_waste_annual * 0.5  # 50% reduction
    plastic_bag_savings = total_plastic_bag_waste_annual * 0.8  # 80% reduction
    
    print(f"Plastic waste savings: {plastic_savings:.2f} lbs annually")
    print(f"Aluminum can waste savings: {aluminum_savings:.2f} lbs annually")
    print(f"Paper box waste savings: {paper_savings:.2f} lbs annually")
    print(f"Plastic bag waste savings: {plastic_bag_savings:.2f} lbs annually")
    
    total_savings = plastic_savings + aluminum_savings + paper_savings + plastic_bag_savings
    print(f"\nTotal potential waste savings: {total_savings:.2f} lbs annually")

if __name__ == "__main__":
    waste_reduction_calculator()


# Future Improvements:
# - Integrate with a database to store user input for long-term tracking
# - Implement a graphical interface for visualizing waste reduction impact