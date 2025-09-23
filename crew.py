from crewai import Agent, Crew, Process
from crewai.project import CrewBase, agent, crew
from crewai_tools import SerperDevTool

@CrewBase
class ResumeATSCrew():
  """Resume ATS crew"""

  agents_config = "config/agents.yaml"


from crewai import Agent
from crewai_tools import SerperDevTool
from crewai.decorators import agent

class MyAgents:

  agents_config = "config/agents.yaml"
  
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
