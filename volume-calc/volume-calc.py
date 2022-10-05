#Functions
def calculate_volume(length, base, height):
    volume = length * base * height
    return (volume)


#Welcome Message
print("\n" "Empty Rectangular Tank Volume Calculator (in units)" "\n")

#Input
length_input = float(input("Length value : ")) 
base_input = float(input("Base value : "))
height_input= float(input("Height value .: " ))


#Convert Inputs to float
length = float(length_input)
base = float(base_input)
height= float(height_input)

#Call Function
calculated_volume= calculate_volume(length, base, height)


#Results

print(f"\nRectangular Tank Volume is: {calculated_volume} units cubed" )

