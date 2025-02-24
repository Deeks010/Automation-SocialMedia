from crewai import Crew,Process
from agents import drafting_agent,seo_optimization_agent,editing_refinement_agent,chief_agent
from tasks import drafting_task,seo_task,chief_task,editing_task

crew = Crew(
    agents=[drafting_agent,editing_refinement_agent,seo_optimization_agent,chief_agent],
    tasks = [drafting_task,editing_task,seo_task,chief_task],
    process = Process.sequential,
    memory = True,
    cache = True,
    max_rpm = 100,
    share_crew = True

)

result = crew.kickoff(inputs = {'topic':'i recently participated in GDSC solution challenge and i also got selected in top 100 finalist'})
print(result)