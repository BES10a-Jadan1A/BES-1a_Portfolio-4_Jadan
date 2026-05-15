# =========================================================
# CHEMICAL LABORATORY CHEMICAL INVENTORY SYSTEM
# =========================================================
# This program demonstrates the use of:
# ✔ Functions
# ✔ Iterations / Loops
# ✔ Conditional Statements
# ✔ Counters and Summation Loops
# ✔ Filtering Data
# ✔ User Input and Type Conversion
#
# REAL-LIFE APPLICATION:
# This program simulates a laboratory inventory and
# concentration monitoring system used in Chemical
# Engineering laboratories.
#
# Chemical Engineering students often handle multiple
# chemical solutions in experiments. This program helps
# monitor:
# - Chemical concentration
# - Total chemical usage
# - Hazardous solutions
# - Average concentration
#
# SIGNIFICANCE:
# Accurate monitoring of laboratory chemicals is essential
# for:
# ✔ Laboratory safety
# ✔ Chemical process control
# ✔ Waste minimization
# ✔ Experimental accuracy
# ✔ Industrial chemical handling
#

# ---------------------------------------------------------
# FUNCTION 1:
# Computes the amount of solute used
# Formula:
# mass = molarity × volume × molar mass
# ---------------------------------------------------------
def compute_mass(molarity, volume_liters, molar_mass):
    mass = molarity * volume_liters * molar_mass
    return mass


# ---------------------------------------------------------
# FUNCTION 2:
# Determines safety level of the solution
# ---------------------------------------------------------
def safety_check(molarity):

    if molarity >= 5:
        return "HIGH RISK"
    
    elif molarity >= 1:
        return "MODERATE RISK"
    
    else:
        return "LOW RISK"


# ---------------------------------------------------------
# FUNCTION 3:
# Displays laboratory safety reminder
# (Void / Non-fruitful Function)
# ---------------------------------------------------------
def laboratory_reminder():

    print("\nLABORATORY SAFETY REMINDERS")
    print("1. Wear complete PPE.")
    print("2. Label all chemicals properly.")
    print("3. Avoid direct inhalation.")
    print("4. Dispose waste properly.")
    print("5. Follow laboratory protocols.\n")

# List containers
chemical_names = []
chemical_masses = []
chemical_concentrations = []

# Counter variables
chemical_count = 0
total_mass = 0

# Largest concentration tracker
highest_concentration = -1
most_concentrated_chemical = ""

print("CHEMICAL ENGINEERING LABORATORY INVENTORY SYSTEM")
print("Type 'done' as chemical name to stop.\n")

# ---------------------------------------------------------
# WHILE LOOP
# Continuously asks user for chemical data
# until the user types 'done'
# ---------------------------------------------------------

while True:

    chemical = input("Enter chemical name: ")

    # Break statement
    if chemical.lower() == "done":
        break

    # Continue statement
    if chemical.startswith("#"):
        continue

    molarity = float(input("Enter molarity (mol/L): "))
    volume_ml = float(input("Enter volume (mL): "))
    molar_mass = float(input("Enter molar mass (g/mol): "))

    # Convert mL to Liters
    volume_liters = volume_ml / 1000

    # Function call
    mass = compute_mass(
        molarity,
        volume_liters,
        molar_mass
    )

    # Store data in lists
    chemical_names.append(chemical)
    chemical_masses.append(mass)
    chemical_concentrations.append(molarity)

    # Counting loop pattern
    chemical_count = chemical_count + 1

    # Summation loop pattern
    total_mass = total_mass + mass

    # Largest value loop pattern
    if molarity > highest_concentration:

        highest_concentration = molarity
        most_concentrated_chemical = chemical

    print("\nChemical Recorded Successfully!\n")

# ---------------------------------------------------------
# FOR LOOP
# Displays all recorded chemicals
# ---------------------------------------------------------

print("\n========== CHEMICAL INVENTORY ==========")

for i in range(chemical_count):

    print("\nChemical #", i + 1)
    print("Name:", chemical_names[i])

    print("Concentration:",
          chemical_concentrations[i],
          "mol/L")

    print("Required Mass:",
          round(chemical_masses[i], 2),
          "grams")

    # Filtering in a loop
    if chemical_concentrations[i] >= 5:

        print("Status: HIGHLY CONCENTRATED")

    # Function call
    print("Safety Level:",
          safety_check(
              chemical_concentrations[i]
          ))

# ---------------------------------------------------------
# Average Loop Pattern
# ---------------------------------------------------------

sum_concentration = 0

for concentration in chemical_concentrations:

    sum_concentration = (
        sum_concentration + concentration
    )

# Avoid division by zero
if chemical_count > 0:

    average_concentration = (
        sum_concentration / chemical_count
    )

else:
    average_concentration = 0

print("\n========== LABORATORY SUMMARY ==========")

print("Total Chemicals Recorded:",
      chemical_count)

print("Total Chemical Mass Used:",
      round(total_mass, 2),
      "grams")

print("Average Concentration:",
      round(average_concentration, 2),
      "mol/L")

print("Most Concentrated Chemical:",
      most_concentrated_chemical)

print("Highest Concentration:",
      highest_concentration,
      "mol/L")

# Function call
laboratory_reminder()



