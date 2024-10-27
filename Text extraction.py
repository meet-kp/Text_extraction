import re
import pandas as pd

# Function to extract information from the input text
def extract_information(input_text):
    # Define regular expressions to extract information
    vehicle_name_pattern = r"Veh Name:\s*(\w+\s*\w+)"
    case_number_pattern = r"CSR:\s*(\d+-\d+)"
    pickup_location_pattern = r"loc:\s*([\w\s]+)"
    drop_location_pattern = r"Near DLR:\s*([\w\s]+)"

    # Extract information using regex
    vehicle_name_match = re.search(vehicle_name_pattern, input_text)
    case_number_match = re.search(case_number_pattern, input_text)
    pickup_location_match = re.search(pickup_location_pattern, input_text)
    drop_location_match = re.search(drop_location_pattern, input_text)

    # Initialize a dictionary to store the extracted information
    data = {
        "Vehicle Name": vehicle_name_match.group(1) if vehicle_name_match else "",
        "Case Number": case_number_match.group(1) if case_number_match else "",
        "Pickup Location": pickup_location_match.group(1) if pickup_location_match else "",
        "Drop Location": drop_location_match.group(1) if drop_location_match else "",
    }

    return data

# Input different sample texts here
sample_text1 = """Veh Name: Tigor EV XZ+ CSR: 7-166777778871 Cust name: VISHAL THAKAR Mob No: 7276668888 Reg/Chassis No: GJ05RS3339 Issue: CHARGING ISSUE loc: GALAXY HOSPITAL Status: TASP ASSIGNED Near DLR: 3008590-Sv&Pa-Virar-SurAut Serv DLR : 3008590-Sv&Pa-Virar-SurAut Team TATA MOTORS LTD"""

sample_text2 = """Veh Name: Another Vehicle CSR: 8-9876543210 Cust name: JOHN DOE Mob No: 1234567890 Reg/Chassis No: ABC123 Issue: Engine Trouble loc: XYZ Garage Status: IN PROGRESS Near DLR: 12345-Someplace Serv DLR : 67890-Anotherplace Team Some Other Company"""

# Input a list of sample texts
sample_texts = [sample_text1, sample_text2]

# Initialize an empty DataFrame to store extracted data
all_data = []

# Process each sample text and extract information
for sample_text in sample_texts:
    data = extract_information(sample_text)
    all_data.append(data)

# Create a DataFrame from the extracted data
df = pd.DataFrame(all_data)

# Save the DataFrame to an Excel file
df.to_excel("extracted_data.xlsx", index=False)

print("Extracted data saved to 'extracted_data.xlsx'")
