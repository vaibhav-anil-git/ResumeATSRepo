from crew import ResumeATSCrew
crew = ResumeATSCrew()

raw_resume_text = """
Vaibhav Yaramwar
Email:vaibhav.yaramwar@gmail.com
Phone: +91 9130080800
LinkedIn: https://www.linkedin.com/in/vaibhavyaramwar/
GitHub: https://dummygithubprofile.com
Portfolio: https://dummydummydummydummydummydummydummyd
Seasoned Technology Lead having an illustrated career of 12 years with experience
in developing & designing effective solutions, providing consultancy, formulating
transformation and transforming applications.
 Business-Driven Problem Solver: Exceptional professional with a keen ability to
comprehend holistic jsdjkhdshjkjlhsdl;oml.ksafklahjkasjhkj business needs and customer requirements. Harnesses
extensive technical knowledge to deliver continuous enhancements in business
performance. Skilled in crafting applications that streamline operations, reduce
errors, and elevate productivity while adeptly leading teams and fostering a culture
of continuous improvement
 Extensive Client Interaction: extensive client interactions and successful
collaborations across multiple business units. Proven track record of surpassing
expectations and elevating the customer experience through innovative solutions
"""
job_title = "Senior Software Engineer"
job_description = """
We are seeking a highly skilled Senior Software Engineer to join our dynamic team.
In this role, you will be responsible for designing, developing, and maintaining
high-quality software solutions that meet our clients' needs. The ideal candidate
will have a strong background in software development, excellent problem-solving
skills, and the ability to work collaboratively in a fast-paced environment.
Responsibilities:
- Design, develop, and maintain software applications.
- Collaborate with cross-functional teams to define, design, and ship new features.
- Write clean, maintainable, and efficient code.
- Conduct code reviews and provide constructive feedback to team members.
- Troubleshoot and debug applications to ensure optimal performance.
- Stay up-to-date with emerging technologies and industry trends.
"""
crew.run_pipeline(raw_resume_text,job_title,job_description)


