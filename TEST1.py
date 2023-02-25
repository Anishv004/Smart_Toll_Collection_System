import csv

# Open the CSV file
with open('TEST.csv', 'r') as csv_file:
    # Create a reader object
    csv_reader = csv.DictReader(csv_file)

    # Create a list to store the updated rows
    updated_rows = []

    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Access the value of the "name" column for the current row
        name = row['VEH_NO']

        # Update the "balance" column based on some condition
        if name == '1111':     #INPUT THE VEHICLE NUMBER HERE
            if int(row['BALANCE'])>=20:
                bal=int(row['BALANCE'])-20
                row['BALANCE']=str(bal)
            else:
                bal=int(row['CRED_BILL'])+20
                row['CRED_BILL']=str(bal)
        # Add the updated row to the list of updated rows
        updated_rows.append(row)

# Open the same CSV file in write mode
with open('TEST.csv', 'w', newline='') as csv_file:
    # Create a writer object
    csv_writer = csv.DictWriter(csv_file, fieldnames=csv_reader.fieldnames)

    # Write the header row to the CSV file
    csv_writer.writeheader()

    # Write the updated rows to the CSV file
    csv_writer.writerows(updated_rows)
