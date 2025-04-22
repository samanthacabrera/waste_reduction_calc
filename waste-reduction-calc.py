def waste_reduction_calculator():
    print("Welcome to the Waste Reduction Calculator!")
    
    plastic_bottles = int(input("How many plastic bottles do you use weekly? "))
    aluminum_cans = int(input("How many aluminum cans do you use weekly? "))
    paper_boxes = int(input("How many paper boxes do you use weekly? "))
    plastic_bags = int(input("How many plastic bags do you use weekly? "))
    
    plastic_bottle_weight = 0.5
    aluminum_can_weight = 0.3
    paper_box_weight = 1
    plastic_bag_weight = 0.05
    
    total_plastic_waste = plastic_bottles * plastic_bottle_weight
    total_aluminum_waste = aluminum_cans * aluminum_can_weight
    total_paper_waste = paper_boxes * paper_box_weight
    total_plastic_bag_waste = plastic_bags * plastic_bag_weight
    
    total_plastic_waste_annual = total_plastic_waste * 52
    total_aluminum_waste_annual = total_aluminum_waste * 52
    total_paper_waste_annual = total_paper_waste * 52
    total_plastic_bag_waste_annual = total_plastic_bag_waste * 52
    
    print("\nYour annual waste generation is as follows:")
    print(f"Plastic waste (bottles): {total_plastic_waste_annual:.2f} lbs")
    print(f"Aluminum can waste: {total_aluminum_waste_annual:.2f} lbs")
    print(f"Paper box waste: {total_paper_waste_annual:.2f} lbs")
    print(f"Plastic bag waste: {total_plastic_bag_waste_annual:.2f} lbs")
    
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
    
    print("\nBy following the suggestions, here’s how much waste you could save annually:")
    plastic_savings = total_plastic_waste_annual * 0.3
    aluminum_savings = total_aluminum_waste_annual * 0.5
    paper_savings = total_paper_waste_annual * 0.5
    plastic_bag_savings = total_plastic_bag_waste_annual * 0.8
    
    print(f"Plastic waste savings: {plastic_savings:.2f} lbs annually")
    print(f"Aluminum can waste savings: {aluminum_savings:.2f} lbs annually")
    print(f"Paper box waste savings: {paper_savings:.2f} lbs annually")
    print(f"Plastic bag waste savings: {plastic_bag_savings:.2f} lbs annually")
    
    total_savings = plastic_savings + aluminum_savings + paper_savings + plastic_bag_savings
    print(f"\nTotal potential waste savings: {total_savings:.2f} lbs annually")

if __name__ == "__main__":
    waste_reduction_calculator()
