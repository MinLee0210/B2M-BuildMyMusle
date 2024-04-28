# Built-in lib
import os
from dotenv import load_dotenv
from typing import Union
from copy import deepcopy

# LanChain lib
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate

# App modules
from schema import *
from controller import prompts

# ===== Controller =====
from pathlib import Path
import os
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    
llm = ChatGoogleGenerativeAI(model="gemini-pro", 
                             google_api_key=GEMINI_API_KEY, 
                             temperature=0.7, 
                             top_p=0.85, 
                             top_k=3)

# 1. 
async def generate_workout_plan(fitness_goal, instruction): 
    if isinstance(instruction, str): 
        b2m_prompt = prompts.workout_plans + instruction
    else: 
        b2m_prompt = prompts.workout_plans + prompts.instruction
    
    b2m_prompt = PromptTemplate.from_template(b2m_prompt)
    output_parser = StrOutputParser()
    b2m_llm = deepcopy(llm)
    b2m_chain = b2m_prompt | b2m_llm | output_parser
    
    response = b2m_chain.invoke({"fitness_goal": fitness_goal, 
                                 "instruction": instruction})
    return response


# 2. 
async def generate_specific_plan(specific_plan, instruction): 
    prompting_materials = dict(specific_plan)
    if isinstance(instruction, str): 
        b2m_prompt = prompts.reach_goals + instruction
    else: 
        b2m_prompt = prompts.reach_goals + prompts.instruction
    
    b2m_prompt = PromptTemplate.from_template(b2m_prompt)
    output_parser = StrOutputParser()
    b2m_llm = deepcopy(llm)
    b2m_chain = b2m_prompt | b2m_llm | output_parser
    
    response = b2m_chain.invoke(prompting_materials)
    return response

# 3. 
async def generate_meal_goals(meal_goals, instruction): 
    prompting_materials = dict(meal_goals)
    if isinstance(instruction, str): 
        b2m_prompt = prompts.meal_goals + instruction
    else: 
        b2m_prompt = prompts.meal_goals + prompts.instruction
    
    b2m_prompt = PromptTemplate.from_template(b2m_prompt)
    output_parser = StrOutputParser()
    b2m_llm = deepcopy(llm)
    b2m_chain = b2m_prompt | b2m_llm | output_parser
    
    response = b2m_chain.invoke(prompting_materials)
    return response

# 4. 
async def generate_health_recipes(diet_type, instruction): 
    prompting_materials = dict(diet_type)
    if isinstance(instruction, str): 
        b2m_prompt = prompts.health_recipes + instruction
    else: 
        b2m_prompt = prompts.health_recipes + prompts.instruction
    
    b2m_prompt = PromptTemplate.from_template(b2m_prompt)
    output_parser = StrOutputParser()
    b2m_llm = deepcopy(llm)
    b2m_chain = b2m_prompt | b2m_llm | output_parser
    
    response = b2m_chain.invoke(prompting_materials)
    return response
# 5. 
async def generate_supplement_guidance(supplement_guidance, instruction): 
    prompting_materials = dict(supplement_guidance)
    if isinstance(instruction, str): 
        b2m_prompt = prompts.supplement_guidance + instruction
    else: 
        b2m_prompt = prompts.supplement_guidance + prompts.instruction
    
    b2m_prompt = PromptTemplate.from_template(b2m_prompt)
    output_parser = StrOutputParser()
    b2m_llm = deepcopy(llm)
    b2m_chain = b2m_prompt | b2m_llm | output_parser
    
    response = b2m_chain.invoke(prompting_materials)
    return response

# 6. 
async def generate_goals_by_results(result, instruction): 
    prompting_materials = result
    if isinstance(instruction, str): 
        b2m_prompt = prompts.set_goals + instruction
    else: 
        b2m_prompt = prompts.set_goals + prompts.instruction
    
    b2m_prompt = PromptTemplate.from_template(b2m_prompt)
    output_parser = StrOutputParser()
    b2m_llm = deepcopy(llm)
    b2m_chain = b2m_prompt | b2m_llm | output_parser
    
    response = b2m_chain.invoke(prompting_materials)
    return response