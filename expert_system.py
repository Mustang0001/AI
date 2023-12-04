class ExpertSystem:
    def __init__(self):
        self.rules = {}

    def add_rule(self, condition, result):
        self.rules[tuple(condition)] = result

    def diagnose(self, symptoms):
        for condition, result in self.rules.items():
            if all(symptom in symptoms for symptom in condition):
                return result
        return "Unknown"

# Example usage:

expert_system = ExpertSystem()

# Adding rules to the expert system
expert_system.add_rule(["fever", "cough"], "Flu")
expert_system.add_rule(["fever", "rash"], "Measles")
expert_system.add_rule(["headache", "dizziness"], "Migraine")
expert_system.add_rule(["cough", "shortness of breath"], "Bronchitis")

# Interaction with the expert system
print("Welcome to the Medical Expert System. Enter your symptoms (type 'exit' to quit).")

while True:
    user_input = input("Symptoms: ").lower().split()

    if user_input == ['exit']:
        break

    result = expert_system.diagnose(user_input)
    print("Diagnosis:", result)
