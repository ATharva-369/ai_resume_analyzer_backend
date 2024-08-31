def generate_llm_scores(job_description,resume):
    import google.generativeai as genai
    import os
    from dotenv import load_dotenv
    
    load_dotenv()

    genai.configure(api_key=os.getenv("API_KEY"))
    model = genai.GenerativeModel("gemini-1.5-flash")

    # Upload the file and print a confirmation
    sample_file = genai.upload_file(path=resume,
                                    display_name="Resume")

    print(f"Uploaded file '{sample_file.display_name}' as: {sample_file.uri}")

    response1 = model.generate_content([sample_file, '''Analyze the following resume text based on the following 10 parameters, and provide a score out of 10:

    Relevant Skills: Does the resume include skills relevant to the job?
    Experience: How well does the work experience match the job requirements?
    Education: Is the educational background appropriate for the job?
    Keywords: Are the important keywords from the job description present?
    Projects: Does the resume include relevant projects that demonstrate applicable skills?
    Certifications: Are there certifications that are relevant to the job?
    Soft Skills: Does the resume highlight important soft skills?
    Achievements: Are there notable achievements that align with the job role?
    Formatting & Presentation: Is the resume well-organized, easy to read, and visually clear?
    Contact Information: Is the contact information complete, accurate, and professional?
    After scoring each parameter on a scale from 1 to 10, provide a final average score. Additionally, offer specific suggestions on how the resume could be improved to better align with these parameters.
                                            Generate the output in a markdown format '''])



    # Generate content using the model for the 2nd task
    response2 = model.generate_content([sample_file, f'''
    Compare the skills listed in the following resume with the skills required by the job description provided below.
    List the skills that match the job description and identify any key skills that are missing.
    Additionally, provide 5 actionable tips to improve the resume to better align with the job description.

    Resume Text:
    [Extracted resume text here]

    Job Description:
    {job_description}

 Generate the output in a markdown format
    '''])

    # Print the response from the model
    with open("Scores.md","w") as f:
        f.write("")
    f.close()

    with open("Scores.md","a") as f:
        f.write(response1.text+"\n\n")
        f.write(response2.text)
    f.close()


