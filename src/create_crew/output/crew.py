```python
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class CreateCrew():
    """CreateCrew crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['agente_pesquisador'],
            verbose=True
        )

    @agent
    def organizational_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['agente_organizacional'],
            verbose=True
        )

    @agent
    def scope_definer(self) -> Agent:
        return Agent(
            config=self.agents_config['agente_definidor_de_escopo'],
            verbose=True
        )

    @agent
    def material_creator(self) -> Agent:
        return Agent(
            config=self.agents_config['agente_criador_de_material'],
            verbose=True
        )

    @agent
    def evaluator(self) -> Agent:
        return Agent(
            config=self.agents_config['agente_de_avaliacao'],
            verbose=True
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],
        )

    @task
    def organization_task(self) -> Task:
        return Task(
            config=self.tasks_config['organization_task'],
        )

    @task
    def scope_definition_task(self) -> Task:
        return Task(
            config=self.tasks_config['scope_definition_task'],
        )

    @task
    def material_creation_task(self) -> Task:
        return Task(
            config=self.tasks_config['material_creation_task'],
            output_file='course_material.pdf'
        )

    @task
    def evaluation_task(self) -> Task:
        return Task(
            config=self.tasks_config['evaluation_task'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the CreateCrew crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,    # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )

# This script can be run to kick off the crew's tasks and agents execution
if __name__ == "__main__":
    crew_instance = CreateCrew()
    crew_instance.crew().start()
```

With this implementation in `crew.py`, we set up a complete multi-agent system for the creation and organization of courses in Generative Artificial Intelligence. The agents are clearly defined and loaded with their respective configurations from the `agents.yaml`, while the tasks are organized to ensure smooth execution through the crew. Each agent and task can operate in a coordinated manner within a sequential process, allowing careful monitoring and execution of the overall workflow aimed at developing high-quality learning materials for the course. The system ensures fluidity and interaction between agents for an efficient course development process, fulfilling the overarching goal of creating structured and relevant AI education.