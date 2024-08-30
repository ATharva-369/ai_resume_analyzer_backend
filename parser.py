def parser():

    nlp = spacy.load("en_core_web_lg")


    #Opening PDF
    file = input("What is the file's path? ")
    f = open(file, 'rb')

    #Reading the pdf and converting to text
    pdf_reader = PyPDF2.PdfReader(f)
    resume_text = ""

    for page in pdf_reader.pages:
        resume_text += page.extract_text().strip()


    #cleaning the text
    resume_text = re.sub(r'\n+',' ', resume_text)
    resume_text = re.sub(r'\s+',' ', resume_text).strip()

    #initializing stuff
    doc = nlp(resume_text.lower())
    matcher = PhraseMatcher(nlp.vocab)

    #Getting patterns from json file
    with open('skills.json', 'r') as f:
        skills_data = json.load(f)
    skills = [x.lower() for x in skills_data['skills_keywords']]

    with open('experience.json', 'r') as f:
        experience_data = json.load(f)

    roles = [x.lower() for x in experience_data['roles']]
    companies = [x.lower() for x in experience_data['companies']]

    skills_patterns = [nlp(text) for text in skills]
    roles_patterns = [nlp(text) for text in roles]
    companies_patterns = [nlp(text) for text in companies]

    #Adding patterns to matcher
    matcher.add('Skills', None, *skills_patterns)
    matcher.add('Roles', None, *roles_patterns)
    matcher.add('Companies', None, *companies_patterns)

    #Getting matches
    matches = matcher(doc)

    #Making list of seperate types of matches 
    skill_matches = []
    roles_matches = []
    companies_matches = []

    for match_id, start, end in matches:
        span = doc[start:end]

        if match_id == nlp.vocab.strings['Skills']:
            if span.text not in skill_matches:
                skill_matches.append(span.text)

        elif match_id == nlp.vocab.strings['Roles']:
            if span.text not in roles_matches:
                roles_matches.append(span.text)
                
        elif match_id == nlp.vocab.strings['Companies']:
            if span.text not in companies_matches:
                companies_matches.append(span.text)

    #Making JSON file to store our parsed data
    data = {
        "skills" : skill_matches,
        "roles" : roles_matches,
        "companies_matches" : companies_matches
    }

    with open('parsed_resume.json', 'w') as f:
        json.dump(data, f, indent= 4)

