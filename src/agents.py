from textwrap import dedent
from crewai import Agent

from tools import ExaSearchToolset


class MeetingPrepAgents():
    def research_agent(self):
      return Agent(
        role="Research Specialist",
        goal='Conduct thorough research on people and companies involved in the meeting',
        tools=ExaSearchToolset.tools(),
        backstory=dedent("""\
          As a Research Specialist, your mission is to uncover detailed information
					about the individuals and entities participating in the meeting. Your insights
					will lay the groundwork for strategic meeting preparation."""),
        verbose=True
      )