import os
from crewai import Agent, Task, Process, Crew

os.environ['OPENAI_API_KEY'] = ''

api = os.environ.get('OPENAI_API_KEY')

marketingAnalyst=Agent(role="Market Research Analyst",
             goal="Find out demand for motels in dallas, texas outskirts", 
             backstory="I am a market research analyst who is trying to find out the demand for a product in the market", 
             verbose=True,allow_delegation=True)

task1 = Task(description="Find out the demand for a product in the market",
             agent=marketingAnalyst,
             expected_output="A report on product demand")

crew = Crew(
    agents=[marketingAnalyst],
    tasks=[task1],
    verbose=True,
    process=Process.sequential,
)

result = crew.kickoff()
print(result)
