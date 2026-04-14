import re
from datetime import datetime

class ResumeChecker:
    def __init__(self, resume_text):
        self.text = resume_text
        self.text_lower = resume_text.lower()
        self.lines = [line.strip() for line in resume_text.split('\n') if line.strip()]
        
    def check_contact_details(self):
        """Check for contact information and return score with found items"""
        score = 0
        found_items = []

        # Phone patterns
        phone_patterns = [
            r'(\+?\d{1,4}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}',
            r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b',
            r'\+\d{1,4}[-.\s]?\d{6,14}',
        ]

        email_patterns = [
          r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
          r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b',
          r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})*\b',
          r'\b[a-zA-Z0-9!#$%&\'*+/=?^_`{|}~-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b',
          r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x5f-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
        ]
        
        for pattern in phone_patterns:
            if re.search(pattern, self.text):
                score += 1
                found_items.append("Phone Number")
                break

        for pattern in email_patterns:
            if re.search(pattern,self.text):
                score += 1
                found_items.append("email")
                break


        # Professional profiles
        profile_patterns = ['linkedin.com', 'github.com', 'gitlab.com', 'portfolio', 'behance.net']
        if any(profile in self.text_lower for profile in profile_patterns):
            score += 1
            found_items.append("Professional Profile/Portfolio")

        # Location indicators
        location_keywords = ['address', 'location', 'city', 'state', 'country', 'street', 'avenue']
        if any(keyword in self.text_lower for keyword in location_keywords):
            score += 1
            found_items.append("Location/Address")

        return min(score, 4), found_items

    def check_structure(self):
        """Check for common resume sections"""
        section_patterns = {
           "work experience": [
                r'\b(work\s+experience|professional\s+experience|employment\s+history|career\s+history|job\s+history)\b',
                r'\b(experience|employment|career|jobs?)\b',
                r'\b(professional\s+background|work\s+background)\b',
                r'\b(work\s+summary|job\s+summary|employment\s+summary)\b',
                r'\b(professional\s+journey|career\s+trajectory)\b',
                r'\b(previous\s+experience|past\s+employment)\b',
                r'\b(professional\s+timeline|work\s+timeline)\b',
                r'\b(relevant\s+experience|industry\s+experience)\b',
                r'\b(project\s+experience|client\s+experience)\b',
                r'\b(on-the-job\s+experience|hands-on\s+experience)\b'
            ],                      
                          
            "skills": [
                r'\b(skills?|technical\s+skills?|core\s+competencies|expertise|proficiencies)\b',
                r'\b(technologies|tools?|programming\s+languages?|software)\b',
                r'\b(competencies|abilities|capabilities|qualifications)\b',
                r'\b(areas\s+of\s+expertise|skill\s+set|knowledge\s+areas)\b',
                r'\b(technical\s+proficiency|technical\s+know[- ]?how)\b',
                r'\b(key\s+skills|functional\s+skills|industry\s+skills)\b',
                r'\b(professional\s+skills|language\s+skills|soft\s+skills)\b',
                r'\b(technology\s+stack|tech\s+stack|stack)\b',
                r'\b(expertise\s+in|familiar\s+with|experienced\s+in)\b'
            ],      
                         
            "education": [
                r'\b(education|educational\s+background|academic\s+background|academics)\b',
                r'\b(qualifications|degrees?|certifications?|training|academic\s+qualifications)\b',
                r'\b(university|college|school|institute|academy|polytechnic)\b',
                r'\b(academic\s+credentials|educational\s+qualifications|learning\s+history)\b',
                r'\b(academic\s+achievements|study\s+history|scholarly\s+background)\b',
                r'\b(academic\s+record|higher\s+education|formal\s+education)\b',
                r'\b(instructional\s+background|courses\s+taken|coursework)\b',
                r'\b(alma\s+mater|degree\s+obtained|graduated\s+from)\b'
            ],          
                              
           "projects": [
                r'\b(projects?|personal\s+projects?|portfolio|work\s+samples|case\s+studies)\b',
                r'\b(notable\s+projects?|key\s+projects?|selected\s+projects?|highlighted\s+projects?)\b',
                r'\b(accomplishments\s+and\s+projects?|achievements\s+&\s+projects?|project\s+work)\b',
                r'\b(independent\s+projects?|academic\s+projects?|freelance\s+projects?)\b',
                r'\b(project\s+experience|client\s+projects|professional\s+projects)\b',
                r'\b(research\s+projects?|engineering\s+projects?|development\s+projects?)\b',
                r'\b(implementation\s+projects?|consulting\s+projects?|internship\s+projects?)\b',
                r'\b(major\s+projects|team\s+projects|capstone\s+project|thesis\s+project)\b',
                r'\b(portfolio\s+items|demos|live\s+projects?|repos?)\b'
            ],          
                              
           "certifications": [
                r'\b(certifications?|certificates?|licenses?|credentials?)\b',
                r'\b(professional\s+certifications?|technical\s+certifications?|industry\s+certifications?)\b',
                r'\b(courses\s+completed|training\s+programs?|continuing\s+education)\b',
                r'\b(certification\s+programs?|diplomas?|authorized\s+training)\b',
                r'\b(certified\s+(developer|engineer|manager|specialist|analyst|expert))\b',
                r'\b(cleared\s+(exam|certification|test))\b',
                r'\b(formal\s+training|official\s+certifications?)\b',
                r'\b(licensure|registered\s+professional|licensed\s+practitioner)\b'
            ],          
                    
            "achievements": [
                r'\b(achievements?|awards?|honors?|recognitions?)\b',
                r'\b(accomplishments?|distinctions?|accolades|laurels?)\b',
                r'\b(outstanding\s+performance|top\s+performer|employee\s+of\s+the\s+month)\b',
                r'\b(merit\s+awards?|scholarships?|ranking|ranked\s+(first|top))\b',
                r'\b(recognized\s+for|commended\s+for|appreciation\s+certificate)\b',
                r'\b(excellence\s+award|leadership\s+award|best\s+performer)\b',
                r'\b(achievement\s+summary|notable\s+achievements?)\b',
                r'\b(honorable\s+mention|achievement\s+highlights)\b'
            ]         

        }
        
        found_sections = []
        for section_name, patterns in section_patterns.items():
            for pattern in patterns:
                if re.search(pattern, self.text_lower):
                    found_sections.append(section_name)
                    break
        
        score = (len(found_sections) / len(section_patterns)) * 5
        return min(score, 5), found_sections

    def check_work_experience(self):
        """Check for work experience details"""
        score = 0
        found_items = []
        
        job_titles = [
         'intern', 'trainee', 'junior', 'assistant', 'associate', 'apprentice',
         'executive', 'coordinator', 'officer', 'representative', 'advisor','analyst',
         'engineer', 'developer', 'consultant', 'technician', 'specialist', 'senior', 'lead', 'manager', 'architect', 'strategist', 'supervisor',
         'director', 'head', 'principal', 'partner', 'vp', 'vice president',
         'cto', 'ceo', 'coo', 'cfo', 'cio', 'chief executive officer', 'chief technology officer',
         'chief operating officer', 'chief financial officer', 'chief information officer',
         'product manager', 'project manager', 'program manager', 'product owner', 'scrum master',
         'software engineer', 'backend developer', 'frontend developer', 'full stack developer',
         'devops engineer', 'data engineer', 'ml engineer', 'data scientist',
         'cloud engineer', 'site reliability engineer', 'qa engineer', 'test engineer',
         'ui designer', 'ux designer', 'product designer', 'graphic designer', 'visual designer',
         'motion designer', 'creative director',
         'data analyst', 'business analyst', 'research analyst', 'financial analyst',
         'bi analyst', 'data architect', 'data modeler', 'statistician',
         'sales associate', 'sales manager', 'account executive', 'account manager',
         'marketing manager', 'digital marketing specialist', 'seo specialist', 'content strategist',
         'brand manager', 'growth hacker',
         'accountant', 'auditor', 'financial analyst', 'controller', 'finance manager', 'bookkeeper',
         'hr manager', 'recruiter', 'talent acquisition specialist', 'people operations manager',
         'hr business partner', 'hr coordinator',
         'operations manager', 'admin assistant', 'office manager', 'facilities manager',
         'customer support representative', 'client success manager', 'support engineer',
         'technical support specialist', 'help desk technician',
         'legal counsel', 'lawyer', 'paralegal', 'legal assistant', 'compliance officer',
         'teacher', 'instructor', 'professor', 'lecturer', 'academic advisor',
         'nurse', 'doctor', 'physician', 'medical assistant', 'clinical researcher',
         'pharmacist', 'therapist', 'dentist',
         'entrepreneur', 'founder', 'freelancer', 'contractor', 'consultant'
        ]
        
        company_indicators = [
            'inc', 'inc.', 'llc', 'l.l.c.', 'ltd', 'ltd.', 'corp', 'corp.', 'co', 'co.',
            'company','plc', 'plc.', 'gmbh', 's.a.', 's.a', 's.a.s.', 's.a.s', 'oy', 'oyj', 'ab', 'bv', 'nv',
            'pte', 'pte.', 'pte ltd', 'pte. ltd.', 'pvt', 'pvt.', 'pvt ltd', 'pvt. ltd.', 'ag', 'sarl',
            'limited', 'llp', 'llp.', 'lllp', 'lllp.', 'k.k.', 'kk', 'sa', 'sae', 'as', 'aps', 'oy ab',
            'group', 'technologies', 'technology', 'solutions', 'systems', 'networks', 'enterprises',
            'partners', 'associates', 'industries', 'ventures', 'services', 'labs', 'logistics',
            'resources', 'holdings', 'global', 'international', 'media', 'digital', 'interactive',
            'consulting', 'innovation', 'institute', 'academy', 'developers', 'creatives', 'studios',
            'team', 'labs', 'works', 'creations', 'softwares', 'analytics', 'designs', 'platforms',
            'foundation', 'trust', 'ngo', 'nonprofit', 'society', 'council', 'board',
            'university', 'college', 'school', 'department', 'ministry', 'commission', 'authority',
            'organization', 'institute', 'association', 'bureau', 'agency', 'office',
            'tech', 'ai', 'ml', 'it', 'devs', 'cloud', 'incorporated', 'firm', 'studio'
            ]
                              
        date_patterns = [
            r'\b(jan|feb|mar|apr|may|jun|jul|aug|sep|sept|oct|nov|dec)[a-z]*\.?\s+\d{4}\b',    
            r'\b\d{1,2}\s+(jan|feb|mar|apr|may|jun|jul|aug|sep|sept|oct|nov|dec)[a-z]*\.?,?\s+\d{4}\b',   
            r'\b\d{4}\s*[-–—~to]+\s*(\d{4}|present|current)\b',         
            r'\b\d{1,2}/\d{4}\s*[-–—~to]+\s*(\d{1,2}/\d{4}|present)\b', 
            r'\b\d{1,2}-\d{4}\s*[-–—~to]+\s*(\d{1,2}-\d{4}|present)\b', 
            r'\bfrom\s+(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\.?\s+\d{4}\b',  
            r'\b(start(ed)?|begin|since)\s+(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)?[a-z]*\.?\s*\d{4}\b', 
            r'\b\w+\s+\d{4}\s*[-–—~to]+\s*(\w+\s+\d{4}|present|current)\b',
            r'\b\d{4}/\d{2}\b',                          
            r'\b\d{2}\.\d{4}\b',                        
            r'\b\d{4}-\d{2}\b',                          
            r'\b\d{2}-\d{2}-\d{4}\b',                    
            r'\b\d{2}/\d{2}/\d{4}\b',                    
            r'\b\d{4}\b'
        ]
        experience_indicators = 0
        
         
        for title in job_titles:
            if re.search(r'\b' + title + r'\b', self.text_lower):
                experience_indicators += 1
                found_items.append(f"Job Title: {title.title()}")
                break
        
         
        for indicator in company_indicators:
            if re.search(r'\b' + indicator + r'\b', self.text_lower):
                experience_indicators += 1
                found_items.append("Company Information")
                break
        
        
        for pattern in date_patterns:
            if re.search(pattern, self.text_lower):
                experience_indicators += 1
                found_items.append("Work Duration/Dates")
                break
        
        # Check for action verbs
        action_verbs = ['developed', 'managed', 'led', 'created', 'implemented', 'designed']
        for verb in action_verbs:
            if re.search(r'\b' + verb + r'\b', self.text_lower):
                experience_indicators += 1
                found_items.append("Action-oriented Descriptions")
                break
        
        score = min(experience_indicators, 5)
        return score, found_items

    def check_skills(self):
        """Check for relevant skills"""
        technical_skills = [
             'python', 'java', 'javascript', 'typescript', 'c', 'c++', 'c#', 'go', 'ruby', 'swift', 'kotlin',
             'php', 'rust', 'r', 'perl', 'scala', 'matlab'

        ]        
        soft_skills = [
         'project management', 'public speaking', 'teamwork', 'time management',
         'leadership', 'communication', 'effective communication', 'critical thinking',
         'analytical thinking', 'creativity', 'adaptability', 'problem solving',
         'emotional intelligence', 'collaboration', 'decision making', 'conflict resolution',
         'negotiation', 'attention to detail', 'resilience'
        ]
        programming_languages = [
            'python', 'java', 'javascript', 'c++', 'c#', 'php', 'ruby', 'go', 'rust',
            'swift', 'kotlin', 'scala', 'r', 'matlab', 'perl', 'lua', 'dart', 'typescript',
            'shell scripting', 'bash', 'objective-c', 'assembly', 'groovy', 'f#', 'elixir'
        ]
        web_technologies_and_framework = [
              'html', 'css', 'react', 'angular', 'vue', 'node.js', 'express', 'django',
              'flask', 'spring', 'laravel', 'wordpress', 'bootstrap', 'jquery', 'ajax',
              'next.js', 'nuxt.js', 'svelte', 'ember.js', 'nestjs', 'meteor', 'tailwind', 
              'ant design', 'semantic ui', 'pug', 'ejs'
        ]
        databases = [
         'mysql', 'postgresql', 'mongodb', 'sqlite', 'oracle', 'sql server',
         'redis', 'cassandra', 'elasticsearch', 'firebase', 'dynamodb',
         'neo4j', 'couchdb', 'hbase', 'bigquery', 'amazon redshift', 'snowflake'
         ]
        cloud_and_devops = [
         'aws', 'azure', 'gcp', 'docker', 'kubernetes', 'jenkins', 'git',
         'ci/cd', 'terraform', 'ansible', 'puppet', 'chef', 'vagrant', 'gitlab ci',
         'circleci', 'travisci', 'openshift', 'prometheus', 'grafana', 'splunk'
         ]
        datascience_and_analytics = [
         'machine learning', 'deep learning', 'data analysis', 'data visualization',
         'pandas', 'numpy', 'scikit-learn', 'tensorflow', 'pytorch',
         'matplotlib', 'seaborn', 'xgboost', 'lightgbm', 'keras',
         'tableau', 'power bi', 'excel', 'spss', 'sas', 'r studio', 'jupyter',
         'hadoop', 'spark', 'databricks', 'mlflow', 'airflow', 'bigml'
         ]
        business_and_marketing = [
         'seo', 'sem', 'google analytics', 'digital marketing', 'social media marketing',
         'content marketing', 'email marketing', 'crm', 'salesforce', 'hubspot',
         'marketing automation', 'campaign management', 'market research',
         'adobe photoshop', 'adobe illustrator', 'google ads', 'facebook ads', 
         'public relations', 'customer acquisition', 'brand management',
         'a/b testing', 'funnel optimization', 'copywriting', 'media planning'
        ]
        designer_roles = [
         'graphic designer', 'web designer','ui designer','ux designer','product designer',
         'visual designer','motion designer','interaction designer','creative director',
         'art director','design lead','ux researcher','design strategist','illustrator',
         'brand designer','service designer','information architect','typographer','user experience designer',
         'user interface designer','project designer','presentation designer','environmental designer',
          'design consultant'
        ]
        operating_systems = [
         'linux', 'unix', 'windows', 'macos', 'ios', 'android', 'chrome os'
       ]
        other_tools = [
         'jira', 'confluence', 'slack', 'trello', 'asana', 'microsoft office',
         'notion', 'monday.com', 'figma', 'adobe xd', 'sketch', 'canva',
         'zendesk', 'freshdesk', 'shopify', 'magento', 'wix', 'wordpress', 
         'zoom', 'google workspace', 'dropbox', 'onedrive'
        ]

        found_skills = []
         
        for skill in technical_skills:
            if re.search(r'\b' + re.escape(skill) + r'\b', self.text_lower):
                found_skills.append(skill.title())
        
        for skill in soft_skills:
            if re.search(r'\b' + re.escape(skill) + r'\b', self.text_lower):
                found_skills.append(skill.title())
                
        for skill in  programming_languages:
            if re.search(r'\b' + re.escape(skill) + r'\b', self.text_lower):
                found_skills.append(skill.title())

        for skill in web_technologies_and_framework:
            if re.search(r'\b' + re.escape(skill) + r'\b', self.text_lower):
                found_skills.append(skill.title())

        for skill in databases:
            if re.search(r'\b' + re.escape(skill) + r'\b', self.text_lower):
                found_skills.append(skill.title())

        for skill in cloud_and_devops:
            if re.search(r'\b' + re.escape(skill) + r'\b', self.text_lower):
                found_skills.append(skill.title())

        for skill in datascience_and_analytics:
            if re.search(r'\b' + re.escape(skill) + r'\b', self.text_lower):
                found_skills.append(skill.title())

        for skill in business_and_marketing:
            if re.search(r'\b' + re.escape(skill) + r'\b', self.text_lower):
                found_skills.append(skill.title())

        for skill in designer_roles:
            if re.search(r'\b' + re.escape(skill) + r'\b', self.text_lower):
                found_skills.append(skill.title())

        for skill in operating_systems:
            if re.search(r'\b' + re.escape(skill) + r'\b', self.text_lower):
                found_skills.append(skill.title())

        for skill in other_tools:
            if re.search(r'\b' + re.escape(skill) + r'\b', self.text_lower):
                found_skills.append(skill.title())
        
        score = min(len(found_skills) * 0.3, 5)
        return score, found_skills

    def check_education(self):
        """Check for education details"""
        score = 0
        found_items = []
        
         
        degrees = [ 
    'bachelor', 'master', 'phd', 'doctorate', 'diploma', 'certificate',
    'associate', 'undergraduate', 'postgraduate', 'graduate',
    'b.tech', 'm.tech', 'b.e', 'm.e', 'b.sc', 'm.sc', 'b.a', 'm.a',
    'b.com', 'm.com', 'bba', 'mba', 'bca', 'mca', 'bs', 'ms', 'ba', 'ma',
    'llb', 'llm', 'm.ed', 'b.ed', 'd.ed', 'm.phil', 'm.arch', 'b.arch',
    'mbbs', 'bds', 'bhms', 'bpt', 'bpharm', 'mpharm', 'bms', 'mms',
    'bachelor of science', 'master of science',
    'bachelor of arts', 'master of arts',
    'bachelor of commerce', 'master of commerce',
    'bachelor of business administration', 'master of business administration',
    'bachelor of computer applications', 'master of computer applications',
    'bachelor of engineering', 'master of engineering',
    'doctor of philosophy', 'doctor of medicine', 'doctor of dental surgery',
    'doctor of education', 'juris doctor', 'doctor of law',
    'executive mba', 'chartered accountant', 'company secretary',
    'pg diploma', 'advanced diploma', 'nanodegree',
    'vocational certificate', 'trade certificate', 'technical diploma',
    'industrial training institute', 'iti certificate',
    'b.ed', 'm.ed', 'd.ed', 'd.el.ed', 'b.el.ed',
    'llb', 'llm', 'bachelor of laws', 'master of laws', 'juris doctor',
    'msc', 'bsc', 'mba (executive)', 'dba', 'md', 'dds', 'do', 'dnp',
    'b.tech (hons)', 'm.tech (research)', 'msc (eng)', 'bfa', 'mfa',
    'b.design', 'm.design', 'b.fashion', 'm.fashion', 'b.lib', 'm.lib',
    'bmm', 'mass communication', 'journalism', 'fine arts',
    'computer science', 'information technology', 'data science', 'ai'
        ]
        
        institutions = [
    'university', 'college', 'institute', 'school', 'academy',
    'polytechnic', 'training center', 'technical school', 'technical institute',
    'engineering college', 'medical college', 'business school', 'law school',
    'faculty', 'department', 'campus', 'institute of technology',
    'open university', 'community college', 'junior college',
    'graduate school', 'postgraduate institute', 'research center',
    'educational institution', 'higher education institute', 'learning center',
    'center of excellence', 'research institute', 'university college',
    'iit', 'nit', 'iiit', 'mit', 'caltech', 'oxford', 'harvard',
    'stanford', 'cambridge', 'ucla', 'nyu', 'nus', 'ntu',
    'vocational institute', 'continuing education center', 'professional institute',
    'industrial training institute', 'iti', 'skill development center'
        ]

        for degree in degrees:
            if re.search(r'\b' + re.escape(degree) + r'\b', self.text_lower):
                score += 1
                found_items.append(f"Degree: {degree.upper()}")
                break
        
        for inst in institutions:
            if re.search(r'\b' + inst + r'\b', self.text_lower):
                score += 1
                found_items.append("Educational Institution")
                break
        
        if re.search(r'\b(graduated|graduation|class\s+of)\s+\d{4}\b', self.text_lower):
            score += 1
            found_items.append("Graduation Year")
        
        if re.search(r'\b(gpa|grade|cgpa|percentage)\b', self.text_lower):
            score += 1
            found_items.append("Academic Performance")
        
        return min(score, 4), found_items

    def check_projects(self):
        """Check for project details"""
        score = 0
        found_items = []
        
        project_keywords = [
    'project', 'projects', 'developed', 'built', 'created', 'designed',
    'implemented', 'executed', 'engineered', 'constructed', 'prototyped',
    'launched', 'deployed', 'integrated', 'contributed', 'collaborated on',
    'led', 'managed', 'spearheaded', 'initiated', 'completed',
    'portfolio', 'github', 'gitlab', 'bitbucket', 'demo', 'repository',
    'showcase', 'live demo', 'case study', 'walkthrough',
    'application', 'web application', 'mobile application',
    'website', 'web portal', 'platform', 'tool', 'dashboard',
    'system', 'software', 'product', 'module', 'solution',
    'capstone', 'minor project', 'major project', 'academic project',
    'personal project', 'client project', 'side project',
    'internship project', 'final year project', 'hackathon', 'proof of concept',
    'refactored', 'modernized', 'redesigned', 'enhanced',
    'automated', 'optimized', 'customized', 'contributed to',
    'evaluated', 'researched', 'tested', 'documented'
        ]

        project_count = 0
        for keyword in project_keywords:
            matches = len(re.findall(r'\b' + re.escape(keyword) + r'\b', self.text_lower))
            if matches > 0:
                project_count += matches
        
        if project_count > 0:
            score = min(project_count * 0.5, 3)
            found_items.append(f"Project-related content found ({project_count} mentions)")
        
        tech_terms = ['api', 'database', 'frontend', 'backend', 'web app', 'mobile app']
        for term in tech_terms:
            if re.search(r'\b' + re.escape(term) + r'\b', self.text_lower):
                found_items.append(f"Technical Term: {term.upper()}")
        
        return min(score, 3), found_items

    def check_achievements(self):
        """Check for achievements and awards"""
        score = 0
        found_items = []
        
        achievement_keywords = [
    'award', 'awards', 'recognition', 'recognised', 'honor', 'honour',
    'achievement', 'achievements', 'winner', 'winning', 'won',
    'certificate', 'certification', 'certified', 'scholarship',
    'medal', 'gold medal', 'silver medal', 'bronze medal',
    'prize', 'first place', 'runner-up', 'top performer',
    'distinction', 'excellence', 'merit', 'best performer',
    'commendation', 'nominated', 'employee of the month',
    'ranked', 'ranking', 'valedictorian', 'topper', 'high achiever',
    'honor roll', 'dean’s list', 'class rank', 'academic honors',
    'outstanding performance', 'star of the month', 'spot award',
    'exemplary performance', 'recognition letter', 'national award',
    'state award', 'special mention', 'accolade', 'notable mention',
    'leadership award', 'innovation award', 'achievement certificate',
    'extra mile award', 'appreciation', 'achievement badge'
        ]

        
        for keyword in achievement_keywords:
            if re.search(r'\b' + keyword + r'\b', self.text_lower):
                score += 0.5
                found_items.append(f"Achievement: {keyword.title()}")
        
        return min(score, 2), found_items

    def check_formatting(self):
        """Check basic formatting quality"""
        score = 5   
        if len(self.text) < 500:
            score -= 2
        
        if "lorem ipsum" in self.text_lower:
            score -= 2
        
        if len(self.lines) < 10:
            score -= 1
        
        return max(score, 0)

    def get_overall_rating(self, percentage):
        """Convert percentage to rating"""
        if percentage >= 85:
            return "Excellent"
        elif percentage >= 70:
            return "Very Good"
        elif percentage >= 55:
            return "Good"
        elif percentage >= 40:
            return "Fair"
        else:
            return "Needs Improvement"

    def calculate_score(self):
        """Calculate overall resume score"""
        scores = {}
        details = {}
        
         
        scores['Contact Details'], details['Contact Details'] = self.check_contact_details()
        scores['Structure'], details['Structure'] = self.check_structure()
        scores['Work Experience'], details['Work Experience'] = self.check_work_experience()
        scores['Skills'], details['Skills'] = self.check_skills()
        scores['Education'], details['Education'] = self.check_education()
        scores['Projects'], details['Projects'] = self.check_projects()
        scores['Achievements'], details['Achievements'] = self.check_achievements()
        scores['Formatting'] = self.check_formatting()
        
         
        total_score = sum(scores.values())
        max_score = 33  
        percentage = (total_score / max_score) * 100
        
         
        details['Overall Rating'] = self.get_overall_rating(percentage)
        
        return percentage, scores, details
