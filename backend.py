import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.debugger_address = "127.0.0.1:9222"
browser = webdriver.Chrome(options=options)

def prompt_builder(query, builder_type):
    if builder_type == "Standard":
        return query
    elif builder_type == "Deep Dive":
        return (f"In our quest for thorough understanding in this era of abundant information, diving deeper into '{query}' is imperative. "
        f"Let's venture beyond mere surface-level insights. Can you unravel the core principles and underlying mechanisms that define "
        f"'{query}'? Are there common misconceptions surrounding it that need debunking? Furthermore, how does it intertwine with other "
        f"related domains or fields? Shed light on any academic or practical discourses that are currently shaping the narrative around "
        f"'{query}'. As one aspires to master '{query}', what lesser-explored facets or subtopics warrant a closer examination?")


    elif builder_type == "Expert Panel":
        return (f"Convene an intellectual symposium in your digital realm with experts spanning various disciplines to discuss '{query}'. "
        f"Picture a software developer, a product manager, a graphics designer, and a devops seated and ready to start coding will begin writing this application description. How would each of them "
        f"Each plays their own role to ensure the other team members are working efficiently and effectively and on the right track. "
        f"1. Software Developer: What are the core functionalities of '{query}'? How would you design the backend and frontend? "
        f"2. Product Manager: What are the key features and user stories? How would you prioritize them? "
        f"3. Graphics Designer: How would you design the user interface? What are the key considerations? "
        f"4. DevOps: How would you deploy and maintain the application? What are the key challenges? "
        f"5. All: Collaborate to ensure that the application is developed in a timely and efficient manner. "
        f"Work on the code. I will continue prompting you to continue working. But try to get the code done as soon as possible. Do as much work as possible. "
        f"6. All: Reflect on the development process. What went well? What could be improved? "
        f"6. All: Reflect on the development process. What went well? What could be improved? "
        f"7. All: Reflect on the development process. What went well? What could be improved? ")


    elif builder_type == "Research":
        return (f"Begin an in-depth exploration of '{query}'. "
        f"1. Outline its historical context and evolution. "
        f"2. Analyze its current relevance and application in modern society. "
        f"3. Forecast its potential future trajectories. "
        f"4. Discuss its interdisciplinary connections, touching upon its relation to physics, sociology, history, and philosophy. "
        f"5. Dive into practical implementations. How would a software engineer design a system around it? How would a designer visualize it? "
        f"6. Identify challenges and opportunities that a product manager might see in bringing a product related to '{query}' to market. "
        f"7. Compare and contrast academic perspectives with those of industry experts. "
        f"8. Highlight any ethical considerations or dilemmas associated with '{query}'. "
        f"9. List down key stakeholders and their potential interests. "
        f"10. Conclude with a synthesis, weaving together the diverse threads of information. "
        f"Ensure clarity and depth in each section, providing a comprehensive understanding of '{query}'.")
    
    elif builder_type == "Design":
        return (f"Let's design a software application named '{query}'. "
        f"1. Define the core functionalities of '{query}'. "
        f"2. Outline the user stories and key features. "
        f"3. Design the user interface. "
        f"4. Develop the backend and frontend. "
        f"5. Deploy and maintain the application. "
        f"6. Reflect on the development process. "
        f"Work together to bring '{query}' to life, emphasizing clear communication, quality code, and a user-centric approach.")
    
    # elif builder_type == "Product Management":
    #     return (f"Let's design a software application named '{query}'. "
    #     f"1. Define the core functionalities of '{query}'. "
    #     f"2. Outline the user stories and key features. "
    #     f"3. Design the user interface. "
    #     f"4. Develop the backend and frontend. "
    #     f"5. Deploy and maintain the application. "
    #     f"6. Reflect on the development process. "
    #     f"Work together to bring '{query}' to life, emphasizing clear communication, quality code, and a user-centric approach.")
    
    elif builder_type == "Prompt Building":
        return (f"Let's create a detailed prompt to use with GPT-3.\
                1. Define the core functionalities of the query for'{query}'.\
                2. Outline the desired response.\
                3. Design the prompt to make chatgpt respond in great depth.\
                ")
    
    # elif builder_type == "Software Development":
    #     return (f"Let's design a software application named '{query}'. "
    #     f"1. Define the core functionalities of '{query}'. "
    #     f"2. Outline the user stories and key features. "
    #     f"3. Design the user interface. "
    #     f"4. Develop the backend and frontend. "
    #     f"5. Deploy and maintain the application. "
    #     f"6. Reflect on the development process. "
    #     f"Work together to bring '{query}' to life, emphasizing clear communication, quality code, and a user-centric approach.")
                
    elif builder_type == "Notebook":
        return f"""Your task is to act as a team of agents and create an educational Jupyter notebook about '{query}'. You are a team of AI agents, each with specialized expertise:
        - Agent X: Pure Mathematician
        - Agent Y: Applied Mathematician
        - Agent Z: Experienced Teacher
        - Agent W: Statistician

        1. Pure: Dive into the foundational mathematical concepts behind '{query}'. What are the key principles and theories that underpin this topic? Elucidate the theoretical framework.

        2. Applied: Given the foundational concepts provided by Agent X, how can these be applied to real-world scenarios or problems? Develop practical applications or problem-solving techniques related to '{query}'.

        3. Teacher: Develop pedagogical content to explain the topic. This includes step-by-step tutorials, exercises, and explanations. Make sure the content is engaging, clear, and suitable for learners. Consider incorporating visual aids or interactive Python examples to enhance understanding.

        4. Statistician: If '{query}' involves data or probabilistic elements, provide a statistical perspective. Analyze any relevant data, highlight statistical methods or tools that can be applied, and explain their relevance in the context of '{query}'.

        5. All Agents: Collaborate to integrate your content. Ensure that the notebook flows logically, with a balance of theory, application, pedagogical content, and statistical analysis.

        6. Teacher: Design exercises or quizzes to test the learner's understanding of '{query}'. Provide solutions and explanations for each.

        7. All Agents: Reflect on the notebook's content. Is there a need for further clarifications, additions, or refinements to make the topic more comprehensible and engaging for learners?

        Work together to create a comprehensive, educational, and engaging Jupyter notebook on '{query}', prioritizing effective teaching, clear explanations, and deep subject matter expertise.
        """


    elif builder_type == "Build":
        return f"Your task is to collaboratively design and develop a software application named '{query}'. You are a team of AI agents, each with specialized expertise:\
                - Agent A: Software Architect \
                - Agent B: Backend Developer\
                - Agent C: Frontend Developer\
                - Agent D: Quality Assurance Engineer\
                1. Agent A (Software Architect): Define the high-level design and structure of '{query}'. What are its core components and how will they interact?\
                2. Agent B (Backend Developer): Based on Agent A's design, develop the core backend functionalities. What databases, APIs, or services will you use?\
                3. Agent C (Frontend Developer): Design the user interface and develop the frontend functionalities, ensuring a smooth interaction with the backend developed by Agent B.\
                4. Agent D (Quality Assurance Engineer): Test the software for bugs, inconsistencies, and user experience issues. Provide feedback to Agents B and C for necessary improvements.\
                5. All Agents: Collaborate to integrate all components and ensure that '{query}' works seamlessly as a cohesive unit.\
                6. Agent D: Conduct a final round of testing. Ensure all issues have been addressed.\
                7. All Agents: Reflect on the development process. Are there any further optimizations or refinements needed before '{query}' is considered complete?\
                Work together to bring '{query}' to life, emphasizing clear communication, quality code, and a user-centric approach."
    
    elif builder_type == "LaTeX":
        return "Expand on these thoughts. Refine them and improve style and flow of the sentences. Place this into a Latex document with an appropriate latex design style format template types."
        
    # elif builder_type == "Historical Context":
    #     return (f"How has the concept of '{query}' evolved over time? "
    #             f"Provide a historical background, highlighting key milestones, shifts, and turning points. "
    #             f"Understanding the past context will help in comprehending its current relevance and significance.")
    
    # elif builder_type == "Pro-Con Analysis":
    #     return (f"Let's analyze the topic '{query}' from a balanced perspective. "
    #             f"Detail both its positive and negative aspects, ensuring each side is represented fairly. "
    #             f"This balanced view is crucial for our decision-making process.")
    
    # elif builder_type == "Future Implications":
    #     return (f"Based on current trends and developments, how might the topic '{query}' evolve in the future? "
    #             f"Speculate on its potential implications, challenges, and opportunities. "
    #             f"Understanding potential future scenarios will guide our strategic planning.")
    
    return query

def interact_with_chatgpt(query, builder_type="Standard"):
    input_box = browser.find_element(By.ID, "prompt-textarea")

    query = prompt_builder(query, builder_type)

    input_box.send_keys(query)
    
    send_button = browser.find_element(By.CSS_SELECTOR, '[data-testid="send-button"]')
    send_button.click()

    # time.sleep(20) # implement a way to wait for the response
    
    return True 

def close_browser():
    browser.quit()