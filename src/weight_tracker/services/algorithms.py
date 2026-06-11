"""All math algorithm.

Deal with all math to get absolute values.

Functions:
    bmr_value_man(weight, hight, age): calculate BMR value for man.
    bmr_value_woman(weight, hight, age): calculate BMR value for woman.
    exercise_burn(met, weight, time): calculate calory burn from exercise.
"""


def bmr_value_man(weight: float, hight: float, age: int) -> int:
    """Basal Metabolic Rate for Man.
    
    How much calory a man burn in day without any movement.
    
    Args:
        weight (float): Weight of man im kg.
        hight (float): Hight of man in cm.
        age (int): Age of man in year.
        
    Returns:
        int: The aproximet BMR value
    """
    man_bmr = 10 * weight + 6.25 * hight - 5 * age + 5 #Mifflin-St Jeor Equation
    
    return man_bmr


def bmr_value_woman(weight: float, hight: float, age: int) -> int:
    """Basal Metabolic Rate for Woman.
    
    How much calory a woman burn in day without any movement.
    
    Args:
        weight (float): Weight of woman im kg.
        hight (float): Hight of woman in cm.
        age (int): Age of woman in year.
        
    Returns:
        int: The aproximet BMR value
    """
    woman_bmr = 10 * weight + 6.25 * hight - 5 * age - 161 #Mifflin-St Jeor Equation
    
    return woman_bmr


def exercise_burn(met: float, weight: float, time: int) -> int:
    """Calory burn from movement.

    Find the calory a movemt burn in set time.

    Args:
        met (float): The natural burn rate of movement.
        weight (float): The weight of human doing it.
        time (int): The time duration in minute.

    Returns:
        int: Calory burn from movement.
    """
    burn = (met * 3.5 * weight * time) / 200 # Standerd formula

    return burn
