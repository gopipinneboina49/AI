from owlready2 import get_ontology, Thing, DataProperty

# Step 1: Load the Ontology
ontology_path = "IntelligentTutoringSystem.rdf"  # Replace with your ontology file path
onto = get_ontology(ontology_path).load()
print("Ontology loaded successfully!")

# Step 2: Define Classes and Properties Dynamically (if not already in the ontology)
with onto:
    class Shape(Thing):
        pass

    class Square(Shape):
        pass

    class Triangle(Shape):
        pass

    class Circle(Shape):
        pass

    # Define properties
    class has_side(DataProperty):
        range = [float]

    class has_base(DataProperty):
        range = [float]

    class has_height(DataProperty):
        range = [float]

    class has_radius(DataProperty):
        range = [float]

onto.save(file="Updated_IntelligentTutoringSystem.rdf", format="rdfxml")
print("Ontology updated with necessary classes and properties.\n")

# Step 3: ITS Logic for Area Calculation
def main_menu():
    print("\nWelcome to the Intelligent Tutoring System!")
    print("Choose a shape to calculate its area:")
    print("1. Square")
    print("2. Triangle")
    print("3. Circle")
    print("4. Exit")

def calculate_area():
    while True:
        main_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":  # Square
            side = float(input("Enter the side length of the square: "))
            square = onto.Square(f"square_{side}")
            square.has_side.append(side)  # Append value for non-functional property
            area = side * side
            print(f"The area of the square is: {area:.2f}")

        elif choice == "2":  # Triangle
            base = float(input("Enter the base of the triangle: "))
            height = float(input("Enter the height of the triangle: "))
            triangle = onto.Triangle(f"triangle_{base}_{height}")
            triangle.has_base.append(base)
            triangle.has_height.append(height)
            area = 0.5 * base * height
            print(f"The area of the triangle is: {area:.2f}")

        elif choice == "3":  # Circle
            radius = float(input("Enter the radius of the circle: "))
            circle = onto.Circle(f"circle_{radius}")
            circle.has_radius.append(radius)
            area = 3.14159 * radius * radius
            print(f"The area of the circle is: {area:.2f}")

        elif choice == "4":  # Exit
            print("Thank you for using the Intelligent Tutoring System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

    # Save instances back to the ontology
    onto.save(file="Updated_IntelligentTutoringSystem.rdf", format="rdfxml")
    print("Ontology updated with new instances.\n")

# Step 4: Run the ITS
if __name__ == "__main__":
    calculate_area()

    # Print created instances for verification
    print("\nInstances in Updated Ontology:")
    for individual in onto.individuals():
        print(f"- {individual}")
