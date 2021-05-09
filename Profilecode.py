# Profile Code

dev_name = "Karthik Mothiki"

def developer_details():
    print("Developer Name : ", dev_name)

def status():
    learning = ["Python", "Java", "Iot"]
    Interests = ["Robotics", "Artificial Intelligence", "ROS", "IoT"]
    print("Learning = ", learning)
    print("Interests = ", Interests)

def skills():
    languages = ["Python", "Kotlin", "C", "C++", "Java"]
    ide = ["Vs Code", "Visual Studio", "PyCharm", "Atom"]
    OS = ["Windows", "Linux", "Ubuntu", "Kali Linux", "Android"]
    Cloud = ["AWS"]
    print("Languages Using = ", languages)
    print("OS Used = ", OS)
    print("Cloud = ", Cloud)

def experience():
    internships = {"AI Tech Web" : "Technical Content Writer", "Indian Robotics Community" : "Campus Ambassador"}
    Community = {"TechnoPhiles" : "Discord Community"}
    print("Internships = ", internships)
    print("Founder at = ", Community)


if __name__ == "__main__":
    developer_details()
    status()
    skills()
    experience()
    
