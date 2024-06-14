import requests

url = 'http://127.0.0.1:5000/predice'
data = {
    "Your Current Country": "India", # Tu País Actual
    "Your Current Zip Code / Pin Code": "400022", # Tu Código Postal / Código PIN Actual
    "Your Gender": "Male", # Tu Género
    "Which of the below factors influence the most about your career aspirations ?": "People from my circle, but not family members", #¿Cuál de los siguientes factores influye más en tus aspiraciones profesionales?
    "Would you definitely pursue a Higher Education / Post Graduation outside of India ? If only you have to self sponsor it.": "No, But if someone could bare the cost I will", #¿Definitivamente perseguirías una educación superior / posgrado fuera de India si solo tienes que autofinanciarlo?
    #"How likely is that you will work for one employer for 3 years or more ?": "This will be hard to do, but if it is the right company I would try", #¿Qué tan probable es que trabajes para un empleador durante 3 años o más?
    "Would you work for a company whose mission is not clearly defined and publicly posted.": "Yes", # ¿Trabajarías para una empresa cuya misión no esté claramente definida y publicada públicamente?
    "How likely would you work for a company whose mission is misaligned with their public actions or even their product ?": "Will NOT work for them", # ¿Qué tan probable es que trabajes para una empresa cuya misión esté desalineada con sus acciones públicas o incluso con su producto?
    "How likely would you work for a company whose mission is not bringing social impact ?": "6", # ¿Qué tan probable es que trabajes para una empresa cuya misión no esté trayendo impacto social?
    "What is the most preferred working environment for you.": "Fully Remote with Options to travel as and when needed", # ¿Cuál es el entorno de trabajo más preferido para ti?
    "Which of the below Employers would you work with.": "Employer who rewards learning and enables that environment", # ¿Con cuál de los siguientes empleadores te gustaría trabajar?
    "Which type of learning environment that you are most likely to work in ?": "Self Paced Learning Portals, Instructor or Expert Learning Programs", # ¿En qué tipo de entorno de aprendizaje es más probable que trabajes?
    "Which of the below careers looks close to your Aspirational job ?": "Teaching in any of the institutes/online or Offline, Look deeply into Data and generate insights, Become a content Creator in some platform", # ¿Cuál de las siguientes carreras se parece más a tu trabajo aspiracional?
    "What type of Manager would you work without looking into your watch ?": "Manager who explains what is expected, sets a goal and helps achieve it", # ¿Qué tipo de gerente te gustaría tener sin mirar tu reloj?
    "Which of the following setup you would like to work ?": "Work with 5 to 6 people in my team" # ¿En qué tipo de configuración preferirías trabajar
}

    

response = requests.post(url, json=data)
print(response.json())
