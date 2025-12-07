import openai
import os
import json

# Ensure you have your OpenAI API key set as an environment variable
# export OPENAI_API_KEY='YOUR_API_KEY'

def get_robot_plan(user_command, robot_capabilities, available_locations, available_objects):
    """
    Generates a robot action plan using OpenAI's GPT-4.

    Args:
        user_command (str): The natural language instruction from the user.
        robot_capabilities (list): List of actions the robot can perform.
        available_locations (list): List of locations the robot can interact with.
        available_objects (list): List of objects the robot can manipulate.

    Returns:
        list: A JSON list of robot actions, or None if an error occurs.
    """
    prompt = f"""
You are a robot task planner. Your goal is to convert high-level human commands into a sequence of atomic robot actions.
The robot has the following capabilities:
{'- ' + chr(10).join(robot_capabilities)}

Available locations: {', '.join(available_locations)}.
Available objects: {', '.join(available_objects)}.

User command: "{user_command}"

Generate a JSON list of actions, for example:
[{{ "action": "move_to", "location": "kitchen" }}, {{ "action": "pick_up", "object": "cup" }}]
"""
    try:
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that generates robot plans in JSON format."},
                {"role": "user", "content": prompt}
            ],
            response_format={ "type": "json_object" }
        )
        plan_text = response.choices[0].message.content
        return json.loads(plan_text)
    except openai.APIError as e:
        print(f"OpenAI API error: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON response from GPT-4: {e}")
        print(f"GPT-4 response: {plan_text}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

if __name__ == "__main__":
    capabilities = [
        "move_to(location)", "pick_up(object)", "place_object(object, location)", "detect_object(object_name)"
    ]
    locations = ["kitchen", "living_room", "bedroom"]
    objects = ["cup", "book", "block"]

    command1 = "Go to the kitchen, pick up the cup, and bring it to the living room."
    print(f"Planning for: '{command1}'")
    plan1 = get_robot_plan(command1, capabilities, locations, objects)
    print(json.dumps(plan1, indent=2))
    print("-" * 30)

    command2 = "Find the book in the bedroom and place it on the table in the living room."
    print(f"Planning for: '{command2}'")
    plan2 = get_robot_plan(command2, capabilities, locations, objects)
    print(json.dumps(plan2, indent=2))
