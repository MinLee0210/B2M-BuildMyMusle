from pydantic import BaseModel, Field


class GetWorkoutPlan(BaseModel): 
    fitness_goal: str = Field(description="Demonstrate your fitness goals. For instance, lose weights in 1 week, have 6 packs in 4 weeks")

class GetSpecificPlan(BaseModel): 
    workout_type: str = Field(description="Demontrate what body type do you want: bodybuilder,  power-lifter, etc.")
    fitness_goal: str = Field(description="Demonstrate your fitness goals. For instance, lose weights in 1 week, have 6 packs in 4 weeks")

class GetMealGoals(BaseModel): 
    specific_goal: str = Field(description="Demonstrate your goals of fitness. ")

class GetHealthRecipes(BaseModel): 
    diet_type: str = Field(description="Demonstrate your diet routine or your desired diet routine. For instnace, I am taking part in intermittent fasting; to be more precise, I follows 5:2 diet.")

class GetSupplementGuidance(BaseModel): 
    specific_goal: str = Field(description="Demonstrate your goals of fitness. ")


class GetSetGoals(BaseModel): 
    result: str = Field(description="Demonstrate concisely what type of fitness goals that you want to achieve.")

class GenerateAnswer(BaseModel): 
    generated_answer: str = Field(description="LLM agent suggests you something ...")