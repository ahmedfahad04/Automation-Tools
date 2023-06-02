import os
import re
import sys

import pandas as pd
import win32com.client as win32
from docxtpl import DocxTemplate


def convert_to_pdf(doc):
    word = win32.DispatchEx("Word.Application")
    new_name = os.path.splitext(doc)[0] + ".pdf"
    worddoc = word.Documents.Open(doc)
    worddoc.SaveAs(new_name, FileFormat=17)
    worddoc.Close()
    word.Quit()


# read the doc file
data = pd.read_excel('data.xlsx')
doc = DocxTemplate("template.docx")

# # operation for a single file
# context = {'Name': 'Akash'}

# show the attributes
i = 1

for index, row in data.iterrows():
    lang = row['languages']
    name = row['name']
    goal = row['goal']
    school = row['ssc']
    college = row['hsc']
    email = row['email']
    address = row['address']
    mobile = row['mobile']
    ssc_gpa = row['ssc_gpa']
    hsc_gpa = row['hsc_gpa']
    cgpa = row['cgpa']
    awards = row['awards']
    social = row['social']
    skills = row['skills']
    training = row['training']
    research = row['research']
    interest = row['interest']
    courses = row['courses']
    exp = row['experience']
    organisation = row['organisation']

    # Language configuration
    if lang == 'N/A' or isinstance(lang, float):
        lang_context = {'l1': 'N/A', 'l2': 'N/A', 'l3': 'N/A'}
    else:
        lang_values = lang.split(' ')
        lang_values = [x.strip().title() for x in lang_values]

        # Set default values for placeholders
        l1 = l2 = l3 = 'N/A'

        # Assign values to placeholders based on the number of values in 'lang_values' list
        if len(lang_values) >= 1:
            l1 = lang_values[0].strip()
        if len(lang_values) >= 2:
            l2 = lang_values[1].strip()
        if len(lang_values) >= 3:
            l3 = lang_values[2].strip()

        # make the language context for the template
        lang_context = {
            'l1': l1,
            'l2': l2,
            'l3': l3,
        }

    # Award configuration
    if awards == 'N/A' or isinstance(awards, float):
        award_context = {'achievement_1': 'N/A', 'achievement_2': 'N/A'}
    else:
        award_values = awards.split(', ')

        a1 = a2 = 'N/A'

        if len(award_values) >= 1:
            a1 = award_values[0].strip()
        if len(award_values) >= 2:
            a2 = award_values[1].strip()

        award_context = {
            'achievement_1': a1,
            'achievement_2': a2,
        }

    # skill configuration
    if skills == 'N/A' or isinstance(skills, float):
        skill_context = {
            's1': 'N/A',
            's2': 'N/A',
            's3': 'N/A',
            's4': 'N/A',
        }
    else:

        values = re.split(r',', skills)
        values = [x.strip().title() for x in values]

        s1 = s2 = s3 = s4 = 'N/A'

        if len(values) >= 1:
            s1 = values[0].strip()
        if len(values) >= 2:
            s2 = values[1].strip()
        if len(values) >= 3:
            s3 = values[2].strip()
        if len(values) >= 4:
            s4 = values[3].strip()

        skill_context = {
            's1': s1,
            's2': s2,
            's3': s3,
            's4': s4,
        }

    # training configuration
    if training == 'N/A' or isinstance(training, float):
        training_context = {'training': 'N/A'}
    else:
        training_context = {'training': training}

    # research configuration
    if research == 'N/A' or isinstance(research, float):
        research_context = {'research': 'N/A'}
    else:
        research_context = {'research': research}

    # social configuration
    if social == 'N/A' or isinstance(social, float):
        social_context = {'social': 'N/A'}
    else:
        social_context = {'social': social}

    # interest configuration
    if interest == 'N/A' or isinstance(interest, float):
        interest_context = {'i1': 'N/A', 'i2': 'N/A', 'i3': 'N/A', 'i4': 'N/A'}
    else:

        values = interest.split(',')
        values = [x.strip().title() for x in values]

        i1 = i2 = i3 = i4 = 'N/A'

        if len(values) >= 1:
            i1 = values[0]
        if len(values) >= 2:
            i2 = values[1]
        if len(values) >= 3:
            i3 = values[2]
        if len(values) >= 4:
            i4 = values[3]

        interest_context = {
            'i1': i1,
            'i2': i2,
            'i3': i3,
            'i4': i4,
        }

    # courses configuration
    if courses == 'N/A' or isinstance(courses, float):
        course_context = {'course_title_1': 'N/A',
                          'course_title_2': 'N/A', 'course_title_3': 'N/A'}
    else:

        values = courses.split(',')
        values = [x.strip().title() for x in values]

        course_title_1 = course_title_2 = course_title_3 = 'N/A'

        if len(values) >= 1:
            course_title_1 = values[0]
        if len(values) >= 2:
            course_title_2 = values[1]
        if len(values) >= 3:
            course_title_3 = values[2]

        course_context = {
            'course_title_1': course_title_1,
            'course_title_2': course_title_2,
            'course_title_3': course_title_3,
        }

    # experience configuration
    if exp == 'N/A' or isinstance(exp, float):
        experience_context = {'exp_1': 'N/A', 'exp_2': 'N/A'}
    else:

        values = exp.split(',')
        values = [x.strip().title() for x in values]

        exp_1 = exp_2 = 'N/A'

        if len(values) >= 1:
            exp_1 = values[0]
        if len(values) >= 2:
            exp_2 = values[1]

        experience_context = {
            'exp_1': exp_1,
            'exp_2': exp_2,
        }

    # organization configuration
    if organisation == 'N/A' or isinstance(organisation, float):
        organisation_context = {'org_1': 'N/A', 'org_2': 'N/A'}
    else:
        
        values = organisation.split(',')
        values = [x.strip().title() for x in values]

        org_1 = org_2 = 'N/A'

        if len(values) >= 1:
            org_1 = values[0]
        if len(values) >= 2:
            org_2 = values[1]

        organisation_context = {
            'org_1': org_1,
            'org_2': org_2,
        }   
    
    # make the name context for the template
    name_context = {
        'name': name
    }

    goal_context = {
        'goal': goal
    }

    school_context = {
        'ssc': school
    }

    college_context = {
        'hsc': college
    }

    email_context = {
        'email': email
    }

    address_context = {
        'address': address
    }

    mobile_context = {
        'mobile': mobile
    }

    ssc_gpa_context = {
        'ssc_gpa': ssc_gpa
    }

    hsc_gpa_context = {
        'hsc_gpa': hsc_gpa
    }

    cgpa_context = {
        'cgpa': cgpa
    }

    # Render and save the document with both language and name contexts
    doc.render({
        **lang_context,
        **name_context,
        **goal_context,
        **school_context,
        **college_context,
        **email_context,
        **address_context,
        **mobile_context,
        **ssc_gpa_context,
        **hsc_gpa_context,
        **cgpa_context,
        **award_context,
        **social_context,
        **skill_context,
        **training_context,
        **research_context,
        **interest_context,
        **course_context,
        **experience_context,
        **organisation_context,
    })
    doc.save(f"Output/{name}.docx")
    print(f"{i} doc generated!")

    i += 1
    # if i > 10:
    #     break
