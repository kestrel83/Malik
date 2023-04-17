import chemlib as ch

print("Remember to follow proper capitalisation for element symbols!\n".upper())
txt_input = input("Enter the compound formula: ")

compound = ch.Compound(txt_input)
print("The formula for this compound is: " + compound.formula + "\n")

compound_molmass = compound.molar_mass()
print("The molar mass of the compound is: " + str(round(compound_molmass)) + "\n")

compound_elements = compound.occurences
print("The ratio of the elements in this compound is: " + str(compound_elements) + "\n")

g_amt = input("Enter mass of compound (in grams): ")
stoi_amts = compound.get_amounts(grams = float(g_amt))
print(stoi_amts)

#Check input to see if compound is a hydrocarbon ie contains both C and H
i = 0
#Declare variables 'carbon' and 'hydrogen'
carbon = False
hydrogen = False 

while i < len(txt_input):
    if txt_input[i] == "C":
        carbon = True
        i += 1
    elif txt_input[i] == "H":
        hydrogen = True
        i += 1
    else:
        pass
        i += 1
        
#Analyze products of hydrocarbon combustion
def combustion_analysis():
    combustion_formula = ch.Combustion(compound)
    print("Combustion equation: " + str(combustion_formula))
    
if carbon == True and hydrogen == True:
    print("\nCompound is a hydrocarbon")
    combustion_analysis()
else:
    print("\nCompound is not a hydrocarbon")
