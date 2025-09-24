from crewai import Agent, Crew, Task,Process
from crewai.project import CrewBase, agent, crew
from crewai.project import agent,task

from crewai import Agent

import os

# Use your working OpenAI key

@CrewBase
class ResumeATSCrew:
  """Crew for handling resume ATS tasks."""

  agents_config = "config/agents.yaml"
  tasks_config = "config/tasks.yaml"
  
  @agent
  def parser_agent(self) -> Agent:
    return Agent(
      config=self.agents_config['parser_agent'],  # type: ignore[index]
      verbose=True
    )

  @agent
  def ats_writer_agent(self) -> Agent:
    return Agent(
      config=self.agents_config['ats_writer_agent'],
      verbose=True
    )

  @agent
  def evaluator_agent(self) -> Agent:
    return Agent(
      config=self.agents_config['evaluator_agent'],
      verbose=True
    )

  @agent
  def refiner_agent(self) -> Agent:
    return Agent(
      config=self.agents_config['refiner_agent'],
      verbose=True
    )

  @agent
  def general_question_agent(self) -> Agent:
    return Agent(
      config=self.agents_config['general_question_agent'],
      verbose=True
    )

  @agent
  def managerial_question_agent(self) -> Agent:
    return Agent(
      config=self.agents_config['managerial_question_agent'],
      verbose=True
    )

  @agent
  def hr_question_agent(self) -> Agent:
    return Agent(
      config=self.agents_config['hr_question_agent'],
      verbose=True
    )

  @agent
  def behavioral_question_agent(self) -> Agent:
    return Agent(
      config=self.agents_config['behavioral_question_agent'],
      verbose=True
    )

  @agent
  def technical_question_agent(self) -> Agent:
    return Agent(
      config=self.agents_config['technical_question_agent'],
      verbose=True
    )
  
  def parse_resume_task(self,agent, raw_resume_text):
    # Truncate if too long
    truncated_text = raw_resume_text[:1500] + "..." if len(raw_resume_text) > 1500 else raw_resume_text
    
    return Task(
        description=(
            f"Clean this resume text quickly:\n\n{truncated_text}\n\n"
            "Remove artifacts, normalize bullets to '-', keep all content. Be fast and direct."
        ),
        agent=agent,
        expected_output=("Clean resume text with proper structure.")
    )
    
  def rewrite_for_ats_task(self,agent, cleaned_resume_text, job_title, job_description):
    # Truncate inputs if too long
    truncated_resume = cleaned_resume_text[:1200] + "..." if len(cleaned_resume_text) > 1200 else cleaned_resume_text
    truncated_jd = job_description[:300] + "..." if len(job_description) > 300 else job_description
    
    return Task(
        description=(
            f"Rewrite resume for {job_title}:\n\n"
            f"JOB: {truncated_jd}\n\n"
            f"RESUME: {truncated_resume}\n\n"
            "Match keywords, use action verbs, add metrics. Target 80+ ATS score. Be direct and fast."
        ),
        agent=agent,
        expected_output="ATS-optimized resume with keyword placement and metrics."
    )
    
  def refine_bullets_task(self,agent, rewritten_resume_text):
    truncated_text = rewritten_resume_text[:1000] + "..." if len(rewritten_resume_text) > 1000 else rewritten_resume_text
    
    return Task(
        description=(
            f"Polish these bullets with action verbs and metrics:\n\n{truncated_text}\n\n"
            "Add strong verbs and numbers. Be fast and direct."
        ),
        agent=agent,
        expected_output="Resume with enhanced bullet points and metrics."
    )
    
    
  def evaluate_ats_task(self,agent, final_resume_text, job_title, job_description):
    truncated_resume = final_resume_text[:800] + "..." if len(final_resume_text) > 800 else final_resume_text
    truncated_jd = job_description[:200] + "..." if len(job_description) > 200 else job_description
    
    return Task(
        description=(
            f"Score this resume for {job_title}:\n\n"
            f"JOB: {truncated_jd}\n\n"
            f"RESUME: {truncated_resume}\n\n"
            "Rate 1-5: keywords, structure, metrics, verbs, format. Return JSON with overall_score (0-100), breakdown, missing_keywords, quick_wins."
        ),
        agent=agent,
        expected_output="JSON evaluation with scores and recommendations."
    )

  def general_question_task(self,agent, final_resume_text, job_title, job_description):
    truncated_text = final_resume_text[:1000] + "..." if len(final_resume_text) > 1000 else final_resume_text
    
    return Task(
        description=(
            f"Given the candidate’s resume, generate 5 general interview questions exploring career journey, \n\n"
            "strengths, and overall experience having Experienced as {final_resume_text}.\n\n"
            "Job Title: {job_title}\n\n"
            "Job Description: {job_description}\n\n"
            "Questions should be open-ended, not role-specific, and avoid technical depth."
        ),
        agent=agent,
        expected_output="Questions in bullet format."
    )

  def manager_question_task(self,agent, final_resume_text, job_title, job_description):
    truncated_text = final_resume_text[:1000] + "..." if len(final_resume_text) > 1000 else final_resume_text
    
    return Task(
        description=(
            f"Based on the resume, generate 5 tough managerial questions focusing on leadership, decision-making, conflict resolution, and client management.\n\n"
              "Questions should assess leadership skills and handling pressure. {truncated_text}.\n\n"
            "Job Title: {job_title}\n\n"
            "Job Description: {job_description}\n\n"
        ),
        agent=agent,
        expected_output="5 challenging managerial questions exploring leadership and stakeholder management."
    )
  
  def hr_question_task(self,agent, final_resume_text, job_title, job_description):
    truncated_text = final_resume_text[:1000] + "..." if len(final_resume_text) > 1000 else final_resume_text
    
    return Task(
        description=(
            f"Using the resume {truncated_text} as context, generate 5 HR questions exploring motivation, cultural fit, salary expectations, career aspirations, and work preferences \n\n."
              "Avoid technical details. .\n\n"
            "Job Title: {job_title}\n\n"
            "Job Description: {job_description}\n\n"
        ),
        agent=agent,
        expected_output="5 HR questions about motivation, culture fit, and career goals"
    )
  
  def behavioral_question_task(self,agent, final_resume_text, job_title, job_description):
    truncated_text = final_resume_text[:1000] + "..." if len(final_resume_text) > 1000 else final_resume_text
    
    return Task(
        description=(
            f"Given the resume {truncated_text}, generate 5 STAR-based behavioral questions focusing on past challenges, team interactions, and problem-solving. \n\n"
              "Avoid technical details. .\n\n"
            "Job Title: {job_title}\n\n"
            "Job Description: {job_description}\n\n"
        ),
        agent=agent,
        expected_output="5 behavioral interview questions based on Situation, Task, Action, Result framework."
    )
    
  def technical_question_task(self,agent, final_resume_text, job_title, job_description):
    truncated_text = final_resume_text[:1000] + "..." if len(final_resume_text) > 1000 else final_resume_text
    
    return Task(
        description=(
            f"Based on the candidate’s resume, generate 5 challenging technical questions tailored to their skills and domain. \n\n"
              "Focus on applied knowledge and scenario-based answers.\n\n"
            "Job Title: {job_title}\n\n"
            "Job Description: {job_description}\n\n"
        ),
        agent=agent,
        expected_output="5 technical questions that test problem-solving and applied knowledge."
    )
  
  def run_pipeline(self,raw_resume_text:str,job_title:str,job_description:str):
    parser_agent = self.parser_agent()
    ats_writer_agent = self.ats_writer_agent()
    evaluator_agent = self.evaluator_agent()
    refiner_agent = self.refiner_agent()
    general_question_agent = self.general_question_agent()
    managerial_question_agent = self.managerial_question_agent()
    hr_question_agent = self.hr_question_agent()
    behavioral_question_agent = self.behavioral_question_agent()
    technical_question_agent = self.technical_question_agent()

    parse_resume_task = self.parse_resume_task(agent = parser_agent, raw_resume_text = raw_resume_text)
    rewritten_resume_text = self.rewrite_for_ats_task(ats_writer_agent, raw_resume_text, job_title, job_description)
    
    general_question_task = self.general_question_task(general_question_agent, raw_resume_text, job_title, job_description)
    managerial_question_task = self.manager_question_task(managerial_question_agent, raw_resume_text, job_title, job_description)
    hr_question_task = self.hr_question_task(hr_question_agent, raw_resume_text, job_title, job_description)
    behavioral_question_task = self.behavioral_question_task(behavioral_question_agent, raw_resume_text, job_title, job_description)
    #technical_question_task = self.technical_question_task()

    parsed_resume_crew = Crew(
        agents=[parser_agent],
        tasks=[parse_resume_task],
        process=Process.sequential,
        verbose=True
    )

    parsed_resume = parsed_resume_crew.kickoff()
    clean_resume = str(parsed_resume).strip()
    
    rewritten_resume_crew = Crew(
        agents=[ats_writer_agent],
        tasks=[rewritten_resume_text],
        process=Process.sequential,
        verbose=True
    ) 
    rewritten_resume = rewritten_resume_crew.kickoff()
    rewritten_resume = str(rewritten_resume).strip()
    print(rewritten_resume)
    
    refine_bullets_task = self.refine_bullets_task(refiner_agent,rewritten_resume)

    final_resume_crew = Crew(
        agents=[refiner_agent],
        tasks=[refine_bullets_task],
        process=Process.sequential,
        verbose=True
    ) 
    final_resume = final_resume_crew.kickoff()
    final_resume = str(final_resume).strip()
    print(final_resume)
    
    evaluate_ats_task = self.evaluate_ats_task(evaluator_agent,final_resume, job_title, job_description)
    evaluation_crew = Crew(
        agents=[evaluator_agent],
        tasks=[evaluate_ats_task],
        process=Process.sequential,
        verbose=True
    ) 
    evaluation = evaluation_crew.kickoff()
    evaluation = str(evaluation).strip()
    print(evaluation)

    general_question_crew = Crew(
        agents=[general_question_agent],
        tasks=[general_question_task],
        process=Process.sequential,
        verbose=True
    ) 
    general_questions = general_question_crew.kickoff()
    general_questions = str(general_questions).strip()
    print(general_questions)

    managerial_question_task_crew = Crew(
        agents=[managerial_question_agent],
        tasks=[managerial_question_task],
        process=Process.sequential,
        verbose=True
    ) 
    managerial_questions = managerial_question_task_crew.kickoff()
    managerial_questions = str(managerial_questions).strip()
    print(managerial_questions)

    hr_question_task_crew = Crew(
        agents=[hr_question_agent],
        tasks=[hr_question_task],
        process=Process.sequential,
        verbose=True
    ) 
    hr_questions = hr_question_task_crew.kickoff()
    hr_questions = str(hr_questions).strip()
    print(hr_questions)

    behavioral_question_task_crew = Crew(
        agents=[behavioral_question_agent],
        tasks=[behavioral_question_task],
        process=Process.sequential,
        verbose=True
    ) 
    behavioral_questions = behavioral_question_task_crew.kickoff()
    behavioral_questions = str(behavioral_questions).strip()
    print(behavioral_questions)

    technical_question_task_crew = Crew(
        agents=[technical_question_agent],
        tasks=[self.technical_question_task(technical_question_agent, final_resume, job_title, job_description)],
        process=Process.sequential,
        verbose=True
    ) 
    technical_questions = technical_question_task_crew.kickoff()
    technical_questions = str(technical_questions).strip()
    print(technical_questions)

    print("Pipeline execution completed.")
    return clean_resume, rewritten_resume, final_resume, evaluation, general_questions, managerial_questions, hr_questions, behavioral_questions, technical_questions
    