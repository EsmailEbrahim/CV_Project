import os


class Experience:
    def __init__(self, StartDate, EndDate, Company, JobTitle):
        self.StartDate = StartDate
        self.EndDate = EndDate
        self.Company = Company
        self.JobTitle = JobTitle

    def __str__(self):
            ExperienceString = str(f"\t\tFrom: {self.StartDate} To: {self.EndDate}\n\t\tCompany: {self.Company}\n\t\tJob Title: {self.JobTitle}")
            return ExperienceString
    
    def DisplayExperience(self):
         print(str(f"From: {self.StartDate} To: {self.EndDate}\nCompany: {self.Company}\nJob Title: {self.JobTitle}"))


class Education:
    def __init__(self, Institution, CompletionDate, Degree):
        self.Institution = Institution
        self.CompletionDate = CompletionDate
        self.Degree = Degree

    def __str__(self):
            EducationString = str(f"\t\tInstitution: {self.Institution}\n\t\tCompletion Date: {self.CompletionDate}\n\t\tDegree: {self.Degree}")
            return EducationString
    
    def DisplayEducation(self):
         print(str(f"Institution: {self.Institution}\nCompletion Date: {self.CompletionDate}\nDegree: {self.Degree}"))


class Skill:
    def __init__(self, Skill, Percentage):
        self.Skill = Skill
        self.Percentage = Percentage

    def __str__(self):
            SkillString = str(f"\t\tSkill: {self.Skill}\n\t\tPercentage: {self.Percentage}")
            return SkillString
    
    def DisplaySkill(self):
         print(str(f"Skill: {self.Skill}\nPercentage: {self.Percentage}"))


class CV:
    Experiences = []
    Educations = []
    Skills = []

    def __init__(self, Name, BirthDate, Phone):
        self.Name = Name
        self.BirthDate = BirthDate
        self.Phone = Phone

    def AddExperience(self):
         Company = input("\nEnter company: ")
         JobTitle = input("Enter job title: ")
         StartDate = input("Enter start date: ")
         EndDate = input("Enter end date: ")
         ExperienceObject = Experience(StartDate, EndDate, Company, JobTitle)
         self.Experiences.append(ExperienceObject)
         Choice = input("\nAdded successfuly.\n\nAdd experience?\t\t1. Yes\t0. No ")
         if (Choice == "1"):
            self.AddExperience()

    def AddEducation(self):
         Institution = input("\nEnter institution: ")
         CompletionDate = input("Enter completion date: ")
         Degree = input("Enter degree: ")
         EducationObject = Education(Institution, CompletionDate, Degree)
         self.Educations.append(EducationObject)
         Choice = input("\nAdded successfuly.\n\nAdd education?\t\t1. Yes\t0. No ")
         if (Choice == "1"):
            self.AddEducation()
    
    def AddSkill(self):
         skill = input("\nEnter skill: ")
         Percentage = input("Enter percentage: ")
         SkillObject = Skill(skill, Percentage)
         self.Skills.append(SkillObject)
         Choice = input("\nAdded successfuly.\n\nAdd skill?\t\t1. Yes\t0. No ")
         if (Choice == "1"):
            self.AddSkill()

    def GetExperiences(self):
        if len(self.Experiences) == 0:
            return "\tThere is no experience."
        else:
            ExperiencesString = ""
            for Index, Exper in enumerate(self.Experiences):
                if ExperiencesString == "":
                    ExperiencesString = str(f"\t{str(Index + 1)}:\n{Exper}")
                else:
                    ExperiencesString = str(f"{ExperiencesString}\n\t{str(Index + 1)}:\n{Exper}")
            return ExperiencesString
    
    def GetEducation(self):
        if len(self.Educations) == 0:
            return "\tThere is no education."
        else:
            EducationString = ""
            for Index, Edu in enumerate(self.Educations):
                if EducationString == "":
                    EducationString = str(f"\t{str(Index + 1)}:\n{Edu}")
                else:
                    EducationString = str(f"{EducationString}\n\t{str(Index + 1)}:\n{Edu}")
            return EducationString

    def GetSkills(self):
        if len(self.Skills) == 0:
            return "\tThere is no skill."
        else:
            SkillsString = ""
            for Index, Skill in enumerate(self.Skills):
                if SkillsString == "":
                    SkillsString = str(f"\t{str(Index + 1)}:\n{Skill}")
                else:
                    SkillsString = str(f"{SkillsString}\n\t{str(Index + 1)}:\n{Skill}")
            return SkillsString

    def __str__(self):
        YourCV = str(f"| {self.Name}'s CV |".center(os.get_terminal_size().columns, "_"))
        Lines = str("_".center(os.get_terminal_size().columns, "_"))
        CVString = str(f"\n{YourCV}\nName: {self.Name}\nBirth date: {self.BirthDate}\nPhone number: {self.Phone}\nExperiences:\n{self.GetExperiences()}\nEducation:\n{self.GetEducation()}\nSkills:\n{self.GetSkills()}\n{Lines}")
        return CVString
    
    def DisplayCV(self):
         print(self.__str__())
    
    def SaveCV(self):
        try:
            DesktopPath = os.path.expanduser("~/Desktop")
            FileName = str(self.Name + " CV.txt")
            FilePath = os.path.join(DesktopPath, FileName)
            CVString = self.__str__()

            with open(FilePath, "w", encoding="UTF-8") as file:
                file.write(CVString)
            print("\nYour CV saved successfuly to " + str(FilePath))
        except Exception as e:
            print(e)


def Program():
    os.system("cls")
    Name = input("Enter your name: ")
    BirthDate = input("Enter your birth date: ")
    Phone = input("Enter your phone number: ")
    CVObject = CV(Name, BirthDate, Phone)
    Choice = input("\nAdd experience?\t\t1. Yes\t0. No ")
    if (Choice == "1"):
        CVObject.AddExperience()
    Choice = input("\nAdd education?\t\t1. Yes\t0. No ")
    if (Choice == "1"):
        CVObject.AddEducation()
    Choice = input("\nAdd skill?\t\t1. Yes\t0. No ")
    if (Choice == "1"):
        CVObject.AddSkill()
    CVObject.DisplayCV()
    Choice = input("\n\nSave CV to your desktop as a \"txt\" file?\t\t1. Yes\t0. No ")
    if (Choice == "1"):
        CVObject.SaveCV()
    Choice = input("\n\nPress:\t1. Create CV again\t0. Exit ")
    if (Choice == "1"):
        Program()
    else:
        exit()
    

Program()
