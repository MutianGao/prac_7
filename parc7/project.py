class Project:

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        return f"Project: {self.name} Start date: {self.start_date} Priority: {self.priority}" \
               f" Cost estimate: {self.cost_estimate} Completion percentage: {self.completion_percentage}"
