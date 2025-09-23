from crewai import Agent, Crew, Task,Process
from crewai.project import CrewBase, agent, crew
from crewai_tools import SerperDevTool
from crewai.decorators import agent,task

@CrewBase
class ResumeATSCrew:
  """Crew for handling resume ATS tasks."""

  agents_config = "config/agents.yaml"
  tasks_config = "config/tasks.yaml"
  
  @agent
  def parser_agent(self) -> Agent:
    return Agent(
      config=self.agents_config['parser_agent'],  # type: ignore[index]
      verbose=True,
      tools=[SerperDevTool()]
    )

  @agent
  def ats_writer_agent(self) -> Agent:
    return Agent(
      config=self.agents_config['ats_writer_agent'],
      verbose=True,
      tools=[SerperDevTool()]
    )

  @agent
  def evaluator_agent(self) -> Agent:
    return Agent(
      config=self.agents_config['evaluator_agent'],
      verbose=True,
      tools=[SerperDevTool()]
    )

  @agent
  def refiner_agent(self) -> Agent:
    return Agent(
      config=self.agents_config['refiner_agent'],
      verbose=True,
      tools=[SerperDevTool()]
    )

  @agent
  def general_question_agent(self) -> Agent:
    return Agent(
      config=self.agents_config['general_question_agent'],
      verbose=True,
      tools=[SerperDevTool()]
    )

  @agent
  def managerial_question_agent(self) -> Agent:
    return Agent(
      config=self.agents_config['managerial_question_agent'],
      verbose=True,
      tools=[SerperDevTool()]
    )

  @agent
  def hr_question_agent(self) -> Agent:
    return Agent(
      config=self.agents_config['hr_question_agent'],
      verbose=True,
      tools=[SerperDevTool()]
    )

  @agent
  def behavioral_question_agent(self) -> Agent:
    return Agent(
      config=self.agents_config['behavioral_question_agent'],
      verbose=True,
      tools=[SerperDevTool()]
    )

  @agent
  def technical_question_agent(self) -> Agent:
    return Agent(
      config=self.agents_config['technical_question_agent'],
      verbose=True,
      tools=[SerperDevTool()]
    )

  @task
  def parse_resume_task(self) -> Task:
    return Task(
      config=self.tasks_config['parse_resume_task']  # type: ignore[index]
    )

  @task
  def rewrite_for_ats_task(self) -> Task:
    return Task(
      config=self.tasks_config['rewrite_for_ats_task']
    )

  @task
  def refine_bullets_task(self) -> Task:
    return Task(
      config=self.tasks_config['refine_bullets_task']
    )

  @task
  def evaluate_ats_task(self) -> Task:
    return Task(
      config=self.tasks_config['evaluate_ats_task']
    )

  @task
  def general_question_task(self) -> Task:
    return Task(
      config=self.tasks_config['general_question_task']
    )

  @task
  def managerial_question_task(self) -> Task:
    return Task(
      config=self.tasks_config['managerial_question_task']
    )

  @task
  def hr_question_task(self) -> Task:
    return Task(
      config=self.tasks_config['hr_question_task']
    )

  @task
  def behavioral_question_task(self) -> Task:
    return Task(
      config=self.tasks_config['behavioral_question_task']
    )

  @task
  def technical_question_task(self) -> Task:
    return Task(
      config=self.tasks_config['technical_question_task']
    )

  @crew
  def full_pipeline_crew(self) -> Crew:
    return Crew(
      agents=[
        self.parser_agent(),
        self.ats_writer_agent(),
        self.refiner_agent(),
        self.evaluator_agent(),
        self.general_question_agent(),
        self.managerial_question_agent(),
        self.hr_question_agent(),
        self.behavioral_question_agent(),
        self.technical_question_agent(),
      ],
      tasks=[
        self.parse_resume_task(),
        self.rewrite_for_ats_task(),
        self.refine_bullets_task(),
        self.evaluate_ats_task(),
        self.general_question_task(),
        self.managerial_question_task(),
        self.hr_question_task(),
        self.behavioral_question_task(),
        self.technical_question_task(),
      ],
      process=Process.sequential
    )