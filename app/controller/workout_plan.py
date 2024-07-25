from config import config_distribution

from b2m.prompts import workout_plans
from b2m.agent import TinyAgent

config = config_distribution()
tiny_agent = TinyAgent(config=config)

async def generate_workout_plan(fitness_goal): 
    prompt = workout_plans.format(fitness_goal=fitness_goal)
    result = tiny_agent.query(prompt)
    return result