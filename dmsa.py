def dmsa():

    nlp = spacy.load("en_core_web_lg")

    job_description = input("Please enter the job description here: ")

    #cleaning the text
    job_description = re.sub(r'\n+',' ', job_description)
    job_description = re.sub(r'\s+',' ', job_description).strip().lower()

    #initializing stuff
    description_doc = nlp(job_description)
    matcher = PhraseMatcher(nlp.vocab)

    #Getting patterns from json file
    with open('skills.json', 'r') as f:
        skills_data = json.load(f)
    skills = [x.lower() for x in skills_data['skills_keywords']]

    with open('experience.json', 'r') as f:
        experience_data = json.load(f)


    roles = [x.lower() for x in experience_data['roles']]

    skills_patterns = [nlp(text) for text in skills]
    roles_patterns = [nlp(text) for text in roles]

    #Adding patterns to matcher
    matcher.add('Skills', None, *skills_patterns)
    matcher.add('Roles', None, *roles_patterns)

    #Getting matches
    matches = matcher(description_doc)

    skill_matches = []
    roles_matches = []

    for match_id, start, end in matches:
        span = description_doc[start:end]
        if match_id == nlp.vocab.strings['Skills']:
            skill_matches.append(span.text)
        elif match_id == nlp.vocab.strings['Roles']:
            roles_matches.append(span.text)

    #Finding skills and roles present both in job description and resume
    with open('parsed_resume.json', 'r') as f:
        skills_data = json.load(f)

    parsed_skills = [x.lower() for x in skills_data['skills']]
    parsed_roles = [x.lower() for x in experience_data['roles']]

    matching_skills = [x for x in skill_matches if x in parsed_skills]
    matching_roles = [x for x in roles_matches if x in parsed_roles]

    #Saving to a json file
    data = {
        "match_skills" : matching_skills,
        "match_roles" : matching_roles,
    }

    with open('matching.json', 'w') as f:
        json.dump(data, f, indent= 4)

    #SCORE ON BASIS OF COMPATIBILITY OF CURRENT SKILLS COMPARED TO THE JOB DESCRIPTION
    score3_skills= len(matching_skills) / len(skill_matches)

    print("\n\n\n---------------SCORES-------------------\n\n\n")

    print(f"You have a {round(score3_skills*100,2)}% compatibility with the job description.\n\n")

    generate_llm_scores(job_description)