import pprint as p
import re

import pandas as pd

data = pd.read_excel('main_data.xlsx')

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
            if match[0] != '5':
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
        student = re.sub(r'cgpa.*|gap.*', '',
                         str(student), flags=re.IGNORECASE)

        # remove the word 5.* or 4.* from the string
        student = re.sub(r'3\.\d+|4\.\d+', '',
                         str(student), flags=re.IGNORECASE)
        student = re.sub(r'2\.\d+|4\.\d+', '',
                         str(student), flags=re.IGNORECASE)

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


def filter_languages(data):

    students = data.languages
    students = students.to_list()

    pattern = r'\d+'
    lang = []
    row = 2
    for student in students:

        # split according to comma, and, & using regex
        # also remove extra spaces around the values
        student = re.split(r'\,|\&|and|\.', str(student), flags=re.IGNORECASE)
        l1 = len(student)

        # only keep those values that are Bangla/English/Hindi/Japanese/German/Arabic/Bengali
        lang_list = ['Bangla', 'English', 'Hindi', 'Japanese',
                     'German', 'Arabic', 'Bengali', 'Spanish',
                     'Nepali', 'Urdu', 'Bangali']
        lang_list = [x.lower() for x in lang_list]
        student = [x for x in student if x.strip().lower() in lang_list]
        l2 = len(student)

        if len(student) == 0:
            lang.append("N/A")

        else:
            lang.append(student)

        row += 1

    # remove all unnecessary spaces
    l2 = []
    for item in lang:

        t = ''
        if item != 'N/A':
            for element in item:
                t += element.strip() + ' '
        else:
            t += 'N/A'

        l2.append(t)

    # append this value to languages column
    p.pprint(l2)
    for index, value in data.languages.items():
        data.at[index, 'languages'] = l2[index]


def filter_goals(data):

    students = data.goal
    students = students.to_list()

    goals = []
    row = 2
    for student in students:

        if isinstance(student, float):
            # print(f"{row} -- BLANK")
            goals.append("N/A")
        else:
            if len(student) != 0.0:
                value = student.split('.')
                # print(f"{row} => ", value[0])
                goals.append(value[0])

        row += 1

    # print(goals)

    for index, value in data.goal.items():
        data.at[index, 'goal'] = goals[index]


def filter_awards(data):

    students = data.awards
    students = students.to_list()

    awards = []
    row = 2
    for student in students:

        if isinstance(student, float):
            awards.append('N/A')
            # print(f"{row} -- BLANK")
        else:
            # print(f"{row} => ", student)
            awards.append(student)
        row += 1

    p.pprint(awards)

    for index, values in data.awards.items():
        data.at[index, 'awards'] = awards[index]


def filter_social_media(data):

    students = data.social
    students = students.to_list()

    social = []
    row = 2
    for student in students:

        arg = 'facebook'

        if isinstance(student, float) or student == 'No' or student == 'None' or student == 'Nil' or student == 'Nothing':
            social.append('N/A')
            # print(f"{row} -- BLANK")
        else:

            if arg in student.lower():
                social.append('N/A')
                row += 1

                continue

            if student.strip().lower() == 'linkedin':
                social.append('N/A')
                row += 1

                continue

            match = re.search(r'(?i)(?<=://)(.*)', student)
            if match:
                social.append(match.group(1).strip())
                # print(f"{row} => ", match.group(1).strip())
            else:
                # print(f"{row} => ", student)
                social.append(student)
                pass
        row += 1

    p.pprint(social)

    for index, values in data.social.items():
        data.at[index, 'social'] = social[index]


def filter_skills(data):

    students = data.skills
    students = students.to_list()

    skills = []
    row = 2
    for student in students:

        try:
            values = student.replace(';', ',')
            skills.append(student)
            # print(values)
        except:
            skills.append('N/A')
            values = student
            # print('N/A')
        row += 1

    p.pprint(skills)

    for index, values in data.skills.items():
        data.at[index, 'skills'] = skills[index]


def filter_training(data):

    students = data.training
    students = students.to_list()

    training = []
    row = 2
    for student in students:

        if isinstance(student, float):
            training.append('N/A')
            # print(f"{row} -- BLANK")
        else:
            # print(f"{row} => ", student)
            training.append(student)

    p.pprint(training)

    for index, values in data.training.items():
        data.at[index, 'training'] = training[index]


def filter_research(data):

    students = data.research
    students = students.to_list()

    training = []
    row = 2
    for student in students:

        if isinstance(student, float) or student == 'No' or student == 'None' or student == 'Absence' or student == 'Nothing':
            training.append('N/A')
            # print(f"{row} -- BLANK")
        else:
            # print(f"{row} => ", student)
            training.append(student)

    p.pprint(training)

    for index, values in data.research.items():
        data.at[index, 'research'] = training[index]


def filter_experience(data):

    students = data.experience
    students = students.to_list()

    training = []
    row = 2
    for student in students:

        print(student)


def filter_interest(data):

    students = data.interest
    students = students.to_list()

    interest = []
    row = 2
    for student in students:

        if isinstance(student, float):
            interest.append('N/A')
        else:

            values = student.replace('&', ',')
            values = values.replace('and', ',')
            values = values.replace(';', ',')

            interest.append(values)
        row += 1

    for index, values in data.interest.items():
        data.at[index, 'interest'] = interest[index]


def filter_courses(data):

    students = data.courses
    students = students.to_list()

    courses = []
    row = 2
    for student in students:

        if isinstance(student, float) or student == 'No' or student == 'None' or student == 'Absence' or student == 'Nothing':
            courses.append('N/A')
            # print(f"{row} -- BLANK")
        else:

            values = student.replace(';', ',')
            # print(f"{row} => ", values)
            courses.append(values)
        row += 1

    for index, values in data.courses.items():
        data.at[index, 'courses'] = courses[index]


def filter_experience(data):

    students = data.experience
    students = students.to_list()

    exp = []
    row = 2
    for student in students:

        if isinstance(student, float) or student == 'No' or student == 'None' or student == 'Absence' or student == 'Nothing':
            exp.append('N/A')
            print(f"{row} -- BLANK")
        else:

            # values = student.replace(';', ',')
            print(f"{row} => ", student)
            exp.append(student)
        row += 1

    for index, values in data.courses.items():
        data.at[index, 'courses'] = exp[index]


def filter_org(data):

    students = data.organisation
    students = students.to_list()

    organisation = []
    row = 2
    for student in students:

        if isinstance(student, float) or student == 'No' or student == 'None' or student == 'Absence' or student == 'Nothing':
            organisation.append('N/A')
            print(f"{row} -- BLANK")
        else:

            # values = student.replace(';', ',')
            print(f"{row} => ", student)
            organisation.append(student)
        row += 1

    for index, values in data.organisation.items():
        data.at[index, 'organisation'] = organisation[index]


extract_ssc_gpa(data)

extract_school_names(data)
extract_hsc_gpa(data)
extract_college_names(data)


extract_uni_cgpa(data)
extract_faculty_names(data)
filter_languages(data)
filter_goals(data)
filter_awards(data)
filter_social_media(data)
filter_skills(data)
filter_training(data)
filter_research(data)
filter_experience(data)
filter_interest(data)
filter_courses(data)
filter_experience(data)
filter_org(data)

# import pandas as pd
# df = pd.read_excel('data.xlsx')
# df.fillna('n/a', inplace=False)

# # save the data with this new column into another xlxs file
data.to_excel('updated_data.xlsx', index=False)
