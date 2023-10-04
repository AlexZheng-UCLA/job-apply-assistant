class Role:
    def __init__(self, role_title, experience, projects, tech_stacks, last_updated):
        self.role_title = role_title
        self.experience = experience
        self.projects = projects
        self.tech_stacks = tech_stacks
        self.last_updated = last_updated

    def consolidated_info(self):
        info = f"role Title: {self.role_title}\n" \
               f"Experience: {self.experience} years\n" \
               f"Projects:\n{self.projects}\n" \
               f"Tech Stacks: {self.tech_stacks}\n" \
               f"Last Updated: {self.last_updated}"
        return info
    
    def get_role_title(self):
        return self.role_title

# Example usage
applicant = Role(
    role_title="Software Developer",
    experience=5,
    projects="1. Chatbot for customer support\n2. E-commerce website",
    tech_stacks="Python, JavaScript, Django, React",
    last_updated="2023-10-04"
)

print(applicant.consolidated_info())