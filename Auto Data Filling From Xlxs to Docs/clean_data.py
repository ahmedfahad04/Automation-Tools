import re

import pandas as pd

data = pd.read_excel('data.xlsx')

# remove all the extra spaces in the column names
data.columns = data.columns.str.strip()


def extract_ssc_gpa(data):

    ################# Extract the GPA from the SSC column #################
    students = data.ssc
    students = students.to_list()

    pattern = r'\d+'
    ssc_gpa = []
    row = 2
    for student in students:

        # print(f"row=> {row}", student)
        # find all the numbers in the string
        match = re.findall(pattern, str(student))
        if match:
            # 15, 137
            # print(f"row=> {row}", match)
            if row == 15 or row == 137:
                match = match[1:]
                ssc_gpa.append(match[0]+'.'+match[1])
                # print(f"UPDATED: row {row}=>", match[0]+'.'+'00')
            elif match[0] != '5':
                ssc_gpa.append(match[0]+'.'+match[1])
                # print(f"BELOW 5 row {row}=>", match[0]+'.'+match[1])
            else:
                match = match[0]
                ssc_gpa.append(match+'.'+'00')
                # print(f"row {row}=>", match+'.'+'00')

        else:
            # print(f"row=> {row}", match)
            ssc_gpa.append('N/A')

        row += 1

    # Create a new column named 'NewColumn' and initialize it with None
    data['ssc_gpa'] = None

    # Iterate over the DataFrame rows
    for index, row in data.iterrows():

        data.at[index, 'ssc_gpa'] = ssc_gpa[index]


def extract_school_names(data):

    ################# Extract the SChool name from the SSC column #################
    students = data.ssc
    students = students.to_list()

    pattern = r'\d+'
    values = []
    row = 2
    for student in students:

        # print("PREV: ", student)
        # find and remove the word gpa and the words after it
        student = re.sub(r'GPA.*', '', str(student), flags=re.IGNORECASE)

        # remove the word 5.* or 4.* from the string
        student = re.sub(r'5\.\d+|4\.\d+', '',
                         str(student), flags=re.IGNORECASE)

        # remove all ( and ) from the string
        student = re.sub(r'\(|\)|\,|\:|\;|\-', '',
                         str(student), flags=re.IGNORECASE)

        # remove all ssc words from the string
        student = re.sub(r'ssc*', '', str(student), flags=re.IGNORECASE)

        # remove all the ending fullstops
        student = re.sub(r'\.(?=$|\s)', '', str(student), flags=re.IGNORECASE)

        # print(f'row {row} => ', student)
        values.append(student)

        # print()

        row += 1

    # write this values to ssc column

    for index, value in data.ssc.items():
        data.at[index, 'ssc'] = values[index-2]


def extract_hsc_gpa(data):

    ################# Extract the GPA from the HSC column #################
    students = data.hsc
    students = students.to_list()

    pattern = r'\d+'
    hsc_gpa = []
    row = 2
    for student in students:

        # print(f"row=> {row}", student)
        # find all the numbers in the string
        match = re.findall(pattern, str(student))
        if match:
            # 15, 137
            # print(f"row=> {row}", match)
            if row == 15:
                match = match[1:]
                hsc_gpa.append(match[0]+'.'+'00')
                print(f"UPDATED: row {row}=>", match[0]+'.'+'00')
            elif match[0] != '5':
                hsc_gpa.append(match[0]+'.'+match[1])
                print(f"BELOW 5 row {row}=>", match[0]+'.'+match[1])
            else:
                match = match[0]
                hsc_gpa.append(match+'.'+'00')
                print(f"row {row}=>", match+'.'+'00')
            # print(f"row=> {row}", match)

        else:
            print(f"BLANK row=> {row}", match)
            hsc_gpa.append('N/A')

        row += 1

    print(hsc_gpa)

    # Create a new column named 'NewColumn' and initialize it with None
    data['hsc_gpa'] = None

    # Iterate over the DataFrame rows
    for index, row in data.iterrows():

        data.at[index, 'hsc_gpa'] = hsc_gpa[index]


def extract_college_names(data):

    ################# Extract the SChool name from the SSC column #################
    students = data.hsc
    students = students.to_list()

    pattern = r'\d+'
    values = []
    row = 2
    for student in students:

        # print("PREV: ", student)
        # find and remove the word gpa and the words after it
        student = re.sub(r'GPA.*', '', str(student), flags=re.IGNORECASE)

        # remove the word 5.* or 4.* from the string
        student = re.sub(r'5\.\d+|4\.\d+', '',
                         str(student), flags=re.IGNORECASE)

        # remove all ( and ) from the string
        student = re.sub(r'\(|\)|\,|\:|\;|\-', '',
                         str(student), flags=re.IGNORECASE)

        # remove all ssc words from the string
        student = re.sub(r'hsc*|golden*|a\+', '',
                         str(student), flags=re.IGNORECASE)

        # remove all the ending fullstops
        student = re.sub(r'\.(?=$|\s)', '', str(student), flags=re.IGNORECASE)

        print(f'row {row} => ', student)
        values.append(student)

        print()

        row += 1

    # write this values to hsc column

    for index, value in data.ssc.items():
        data.at[index, 'hsc'] = values[index-2]


def extract_uni_cgpa(data):

    ################# Extract the GPA from the HSC column #################
    students = data.faculty
    students = students.to_list()

    pattern = r'\d+'
    cgpa = []
    row = 2
    for student in students:

        # print(f"row=> {row}", student)
        # find all the numbers in the string
        match = re.findall(pattern, str(student))

        if match:

            cgpa.append(match[0]+'.'+match[1])
            # print(f"Row {row}=>", match[0]+'.'+match[1])

        else:
            # print(f"BLANK row=> {row}", match)
            cgpa.append('N/A')

        row += 1

    print(cgpa)

    data['cgpa'] = None
    for index, values in data.faculty.items():
        data.at[index, 'cgpa'] = cgpa[index]


def extract_faculty_names(data):
    ################# Extract the SChool name from the SSC column #################
    students = data.faculty
    students = students.to_list()

    pattern = r'\d+'
    values = []
    row = 2
    for student in students:

        # print("PREV: ", student)
        # find and remove the word gpa and the words after it
        student = re.sub(r'cgpa.*|gap.*', '', str(student), flags=re.IGNORECASE)

        # remove the word 5.* or 4.* from the string
        student = re.sub(r'3\.\d+|4\.\d+', '', str(student), flags=re.IGNORECASE)
        student = re.sub(r'2\.\d+|4\.\d+', '', str(student), flags=re.IGNORECASE)

        # remove all ( and ) from the string
        student = re.sub(r'\(|\)|\,|\:|\;|\-', '',
                        str(student), flags=re.IGNORECASE)

        # remove all the ending fullstops
        student = re.sub(r'\.(?=$|\s)', '', str(student), flags=re.IGNORECASE)

        if len(student) == 0:
            # print(f'BLANK {row} => ', student)
            values.append('N/A')
        else:
            # print(f'row {row} => ', student)
            values.append(student)

        print()

        row += 1

        # write this values to hsc column

    for index, value in data.faculty.items():
        data.at[index, 'faculty'] = values[index]


# extract_ssc_gpa(data)
# extract_school_names(data)
# extract_hsc_gpa(data)
# extract_college_names(data)

# extract_uni_cgpa(data)
# extract_faculty_names(data)

# # save the data with this new column into another xlxs file
data.to_excel('updated_data.xlsx', index=False)
