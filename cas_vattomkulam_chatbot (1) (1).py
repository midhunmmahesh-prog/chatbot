import re
import random
from datetime import datetime

class CASVattamkulamChatbot:
    def __init__(self):
        self.bot_name = "CAS Vattamkulam Chatbot"
        self.conversation_history = []
        
        # Comprehensive college data
        self.college_data = {
            'basic_info': {
                'name': 'College of Applied Science, Vattamkulam',
                'established': '2005',
                'affiliation': 'University of Calicut',
                'management': 'IHRD (Institute of Human Resource and Development)',
                'location': 'Vattamkulam, Nellissery, Sukapuram (P.O.), Edappal',
                'district': 'Malappuram',
                'state': 'Kerala',
                'pin': '679576',
                'phone': ['0494-2689655', '8547006802'],
                'email': 'casvattamkulam@gmail.com',
                'website': 'https://casvattamkulam.ihrd.ac.in',
                'faculty_count': '26',
                'academic_session': 'June - May'
            },
            
            'courses': {
                'ug': {
                    'BSc Computer Science': {
                        'duration': '3 years',
                        'eligibility': '+2 with Mathematics/Computer Science',
                        'seats': 'As per University norms',
                        'career': 'Software Developer, Web Developer, System Analyst, Database Administrator'
                    },
                    'BSc Electronics': {
                        'duration': '3 years',
                        'eligibility': '+2 with Physics/Mathematics',
                        'seats': 'As per University norms',
                        'career': 'Electronics Engineer, Hardware Engineer, Embedded Systems Developer'
                    },
                    'BCA (Bachelor of Computer Applications)': {
                        'duration': '3 years',
                        'eligibility': '+2 in any stream',
                        'seats': 'As per University norms',
                        'career': 'Software Engineer, App Developer, IT Consultant, System Administrator'
                    },
                    'BCom with Computer Application': {
                        'duration': '3 years',
                        'eligibility': '+2 Commerce/Any stream',
                        'seats': 'As per University norms',
                        'career': 'Accountant, Financial Analyst, Tax Consultant, Business Analyst'
                    },
                    'BBA Logistics Honours': {
                        'duration': '3 years',
                        'eligibility': '+2 in any stream',
                        'seats': 'As per University norms',
                        'career': 'Logistics Manager, Supply Chain Analyst, Operations Manager'
                    }
                },
                'pg': {
                    'MSc Computer Science': {
                        'duration': '2 years',
                        'eligibility': 'BSc Computer Science/BCA or equivalent',
                        'seats': 'As per University norms',
                        'career': 'Research Scientist, Senior Developer, Data Scientist, AI/ML Engineer'
                    },
                    'MCom Finance': {
                        'duration': '2 years',
                        'eligibility': 'BCom or equivalent',
                        'seats': 'As per University norms',
                        'career': 'Financial Advisor, Investment Banker, Finance Manager, Chartered Accountant'
                    }
                }
            },
            
            'admission': {
                'academic_year': '2025-26',
                'status': 'Open',
                'registration_period': 'Open till June 9, 2025, 5:00 PM',
                'registration_links': {
                    'IHRD Direct (50% seats)': 'https://ihrdadmissions.org',
                    'University of Calicut': 'https://admission.uoc.ac.in/admission'
                },
                'application_fee': {
                    'SC/ST': '₹205',
                    'General': '₹495'
                },
                'admission_process': [
                    'Step 1: Visit the admission portal (IHRD or University)',
                    'Step 2: Complete online registration with valid documents',
                    'Step 3: Pay application fee online',
                    'Step 4: Download and print the application form',
                    'Step 5: Attend counseling as per schedule',
                    'Step 6: Complete document verification',
                    'Step 7: Pay fees and confirm admission'
                ],
                'required_documents': [
                    'SSLC Certificate and Mark List',
                    '+2 Certificate and Mark List',
                    'Transfer Certificate',
                    'Community Certificate (if applicable)',
                    'Income Certificate (if applicable)',
                    'Aadhaar Card',
                    'Passport size photographs',
                    'Migration Certificate (for other universities)'
                ],
                'seats_distribution': '50% IHRD Direct Admission, 50% University Allotment',
                'contact_admission': 'Call: 0494-2689655, 8547006802'
            },
            
            'departments': {
                'Computer Science': {
                    'courses': ['BSc Computer Science', 'MSc Computer Science', 'BCA'],
                    'facilities': 'State-of-the-art Computer Lab, Latest Software, High-Speed Internet',
                    'activities': 'Coding competitions, Tech fests, Industry workshops'
                },
                'Electronics': {
                    'courses': ['BSc Electronics'],
                    'facilities': 'Well-equipped Electronics Lab, Modern equipment',
                    'activities': 'Circuit design, Robotics, Project exhibitions'
                },
                'Commerce': {
                    'courses': ['BCom with Computer Application', 'MCom Finance', 'BBA Logistics Honours'],
                    'facilities': 'Commerce Lab, Computer facilities',
                    'activities': 'Business seminars, Financial workshops, Industry visits'
                },
                'General': {
                    'courses': 'Support courses for all programs',
                    'subjects': 'English, Mathematics, Physics, Statistics',
                    'activities': 'Inter-departmental events'
                },
                'Physical Education': {
                    'facilities': 'Open Gym, Volleyball Court, Sports Ground',
                    'activities': 'Sports competitions, Fitness programs, Inter-college tournaments'
                }
            },
            
            'facilities': {
                'Academic': [
                    'Smart Classrooms with Interactive Smartboards',
                    'Audio-Visual Teaching Systems',
                    'Digital Learning Resources',
                    'Wi-Fi Enabled Campus',
                    'Online Learning Management System (LMS)'
                ],
                'Laboratory': [
                    'Computer Lab - Latest hardware and software',
                    'Electronics Lab - Advanced equipment',
                    'Commerce Lab - Business simulation software',
                    'Internet facility with high-speed connectivity'
                ],
                'Library': [
                    'Comprehensive collection of books',
                    'Digital library with e-resources',
                    'Reference section',
                    'Reading rooms',
                    'Journal and magazine subscriptions',
                    'INFLIBNET access'
                ],
                'Sports': [
                    'Modern Gym with latest equipment',
                    'Volleyball Court',
                    'Open Gym',
                    'Indoor games facility',
                    'Sports equipment for various games'
                ],
                'Other': [
                    'Auditorium for events',
                    'Cafeteria',
                    'First Aid facility',
                    'Parking area',
                    'Generator backup'
                ]
            },
            
            'nss': {
                'full_name': 'National Service Scheme',
                'objective': 'Develop student personality through community service',
                'activities': [
                    'Village adoption and development programs',
                    'Health and hygiene awareness camps',
                    'Blood donation camps',
                    'Tree plantation drives',
                    'Literacy programs',
                    'Clean India campaigns',
                    'Road safety awareness',
                    'Women empowerment programs',
                    'Environmental conservation',
                    'Disaster relief work'
                ],
                'special_camps': '7-day special camping programs in adopted villages',
                'regular_activities': '120 hours of community service per year',
                'achievements': [
                    'Best NSS Volunteer Awards',
                    'State Level Leadership Camps participation',
                    'Community development projects',
                    'IHRD received Best NSS Directorate from Kerala State (2021-22)'
                ],
                'benefits': [
                    'Certificate from University',
                    'Weightage in higher studies and jobs',
                    'Leadership development',
                    'Social awareness',
                    'Community connect'
                ]
            },
            
            'clubs': {
                'Computer Association': {
                    'activities': [
                        'Coding competitions and hackathons',
                        'Technical workshops and seminars',
                        'Project exhibitions',
                        'Industry expert sessions',
                        'Software development projects',
                        'Tech talks and webinars',
                        'Coding bootcamps'
                    ],
                    'events': 'TECHNOVATION 2K23 - Annual tech fest',
                    'benefits': 'Skill enhancement, Industry exposure, Networking'
                },
                'Electronics Association': {
                    'activities': [
                        'Circuit design workshops',
                        'Robotics projects',
                        'Microcontroller programming',
                        'Electronics project exhibitions',
                        'Technical seminars',
                        'Industry visits',
                        'Innovation challenges'
                    ],
                    'focus': 'Hands-on experience and practical learning',
                    'benefits': 'Technical skills, Problem-solving, Innovation'
                },
                'Commerce Association': {
                    'activities': [
                        'Business plan competitions',
                        'Financial literacy programs',
                        'Stock market simulations',
                        'Entrepreneurship workshops',
                        'Guest lectures by industry experts',
                        'Business case studies',
                        'Marketing competitions'
                    ],
                    'benefits': 'Business acumen, Financial knowledge, Leadership'
                },
                'BMC (Business Management Club)': {
                    'activities': [
                        'Management games',
                        'Leadership workshops',
                        'Team building activities',
                        'Business simulations',
                        'Industry interactions'
                    ]
                },
                'Literary Club': {
                    'activities': [
                        'Debates and discussions',
                        'Creative writing competitions',
                        'Book reviews',
                        'Poetry sessions',
                        'Public speaking events',
                        'Magazine publication',
                        'Quiz competitions'
                    ]
                }
            },
            
            'placement': {
                'coordinator': 'Gopalakrishnan U.K., Lecturer, Department of Computer Science',
                'email': 'placementcell.cas@gmail.com',
                'phone': '9495561967',
                'training': [
                    'Aptitude training from 5th semester',
                    'Verbal ability training',
                    'Group discussion practice',
                    'Mock interviews',
                    'Resume building workshops',
                    'Industry-oriented training by professionals',
                    'Soft skills development',
                    'Technical interview preparation'
                ],
                'top_recruiters': [
                    'TCS (Tata Consultancy Services)',
                    'Wipro',
                    'Infosys',
                    'Tech Mahindra',
                    'HP',
                    'iGATE',
                    'Various IT and non-IT companies'
                ],
                'placement_rate': '50% average placement rate',
                'activities': [
                    'Campus recruitment drives',
                    'Job fairs',
                    'Industry tie-ups',
                    'Internship opportunities',
                    'Career counseling',
                    'TCS Affirmation Action Programme'
                ],
                'highlights': [
                    'Regular campus placements',
                    'Industry partnerships',
                    'Professional training programs',
                    'Placement assistance for all students'
                ]
            },
            
            'other_cells': {
                'Women Cell': {
                    'purpose': 'Women empowerment and safety',
                    'activities': [
                        'Awareness programs on women rights',
                        'Self-defense training',
                        'Health and hygiene workshops',
                        'Gender sensitization programs',
                        'Grievance redressal'
                    ]
                },
                'Anti-Ragging Cell': {
                    'purpose': 'Ensure ragging-free campus',
                    'activities': [
                        'Anti-ragging awareness',
                        'Strict monitoring',
                        '24/7 helpline',
                        'Anonymous complaint mechanism',
                        'Disciplinary actions'
                    ],
                    'policy': 'Zero tolerance for ragging'
                },
                'IQAC (Internal Quality Assurance Cell)': {
                    'purpose': 'Maintain and enhance quality of education',
                    'functions': [
                        'Academic quality monitoring',
                        'Faculty development programs',
                        'Student feedback analysis',
                        'Accreditation preparation',
                        'Quality initiatives implementation'
                    ]
                },
                'PTA (Parent Teacher Association)': {
                    'purpose': 'Bridge between parents and college',
                    'activities': [
                        'Regular parent meetings',
                        'Academic progress discussions',
                        'Student welfare programs',
                        'Feedback mechanism'
                    ]
                },
                'Student Grievance Cell': {
                    'purpose': 'Address student concerns',
                    'features': [
                        'Online complaint registration',
                        'Quick resolution mechanism',
                        'Confidential handling',
                        'Regular follow-up'
                    ]
                }
            },
            
            'college_union': {
                'purpose': 'Student representation and leadership',
                'positions': [
                    'Chairperson',
                    'Vice Chairperson',
                    'General Secretary',
                    'Arts Club Secretary',
                    'Magazine Editor',
                    'University Union Councillor'
                ],
                'activities': [
                    'Organize college events',
                    'Represent student issues',
                    'Cultural programs',
                    'Sports events',
                    'Social initiatives'
                ],
                'recent': 'College Union 2024-25 active'
            },
            
            'events': {
                'TECHNOVATION 2K23': {
                    'type': 'Annual techno-cultural fest',
                    'description': 'IHRD premier tech fest showcasing technical, cultural and entrepreneurial skills',
                    'activities': 'Technical competitions, cultural programs, workshops, exhibitions',
                    'connection': 'Part of THARANG - IHRD annual entrepreneurship fest'
                },
                'Job Fair': {
                    'frequency': 'Annual',
                    'purpose': 'Connect students with employers',
                    'participants': 'Multiple companies and recruiters'
                },
                'Run Kerala Run': {
                    'type': 'State-wide fitness initiative',
                    'participation': 'Active student and staff participation'
                },
                'Blood Donation Camps': {
                    'frequency': 'Regular',
                    'partners': 'Blood banks and hospitals',
                    'impact': 'Social service and community health'
                },
                'Sports Events': {
                    'activities': 'Inter-college tournaments, intra-college competitions',
                    'sports': 'Volleyball, athletics, indoor games'
                }
            },
            
            'vision': 'To develop into a contributing Centre of excellence in knowledge and technology creating globally competitive professionals who would contribute positively to the society.',
            
            'mission': 'To impart quality education and create professionals with high competency and values who can make indelible mark in their respective fields.',
            
            'accreditation': {
                'status': 'Accredited by leading educational bodies',
                'affiliations': 'University of Calicut',
                'recognitions': 'Quality education standards maintained'
            }
        }
        
        print("✓ CAS Vattamkulam Chatbot loaded with complete college information!\n")
    
    def search_query(self, query):
        """Intelligent query matching"""
        q = query.lower()
        matched = []
        
        # Pattern matching
        if re.search(r'\b(course|courses|program|degree|bsc|msc|bca|bcom|mcom|bba|ug|pg)\b', q):
            matched.append('courses')
        if re.search(r'\b(admission|apply|application|enroll|join|register|eligibility|seat|how to)\b', q):
            matched.append('admission')
        if re.search(r'\b(fee|fees|cost|payment|charge)\b', q):
            matched.append('fees')
        if re.search(r'\b(nss|national service)\b', q):
            matched.append('nss')
        if re.search(r'\b(club|clubs|association|computer association|electronics association|commerce|literary|bmc)\b', q):
            matched.append('clubs')
        if re.search(r'\b(placement|job|career|recruit|company|training)\b', q):
            matched.append('placement')
        if re.search(r'\b(facility|facilities|infrastructure|lab|library|gym|campus)\b', q):
            matched.append('facilities')
        if re.search(r'\b(department|faculty|teacher|staff)\b', q):
            matched.append('departments')
        if re.search(r'\b(contact|phone|email|address|location|where|reach)\b', q):
            matched.append('contact')
        if re.search(r'\b(about|history|vision|mission|established|ihrd)\b', q):
            matched.append('about')
        if re.search(r'\b(event|fest|technovation|cultural|sports|blood)\b', q):
            matched.append('events')
        if re.search(r'\b(women cell|anti.?ragging|iqac|pta|grievance|student welfare)\b', q):
            matched.append('cells')
        if re.search(r'\b(union|college union|student council)\b', q):
            matched.append('union')
        
        return matched if matched else ['general']
    
    def generate_response(self, query):
        """Generate comprehensive response"""
        topics = self.search_query(query)
        responses = []
        
        for topic in topics:
            if topic == 'courses':
                responses.append(self.get_courses_info(query))
            elif topic == 'admission':
                responses.append(self.get_admission_info())
            elif topic == 'fees':
                responses.append(self.get_fees_info())
            elif topic == 'nss':
                responses.append(self.get_nss_info())
            elif topic == 'clubs':
                responses.append(self.get_clubs_info(query))
            elif topic == 'placement':
                responses.append(self.get_placement_info())
            elif topic == 'facilities':
                responses.append(self.get_facilities_info())
            elif topic == 'departments':
                responses.append(self.get_departments_info())
            elif topic == 'contact':
                responses.append(self.get_contact_info())
            elif topic == 'about':
                responses.append(self.get_about_info())
            elif topic == 'events':
                responses.append(self.get_events_info())
            elif topic == 'cells':
                responses.append(self.get_cells_info())
            elif topic == 'union':
                responses.append(self.get_union_info())
        
        if not responses:
            return self.get_help_menu()
        
        return "\n\n".join(responses)
    
    def get_courses_info(self, query):
        """Course information"""
        q = query.lower()
        
        # Specific course
        if 'computer science' in q or 'cs' in q:
            info = "💻 *Computer Science Programs:*\n\n"
            for name, details in {**self.college_data['courses']['ug'], **self.college_data['courses']['pg']}.items():
                if 'Computer Science' in name:
                    info += f"*{name}*\n"
                    info += f"  Duration: {details['duration']}\n"
                    info += f"  Eligibility: {details['eligibility']}\n"
                    info += f"  Careers: {details['career']}\n\n"
            return info.strip()
        
        if 'electronics' in q:
            details = self.college_data['courses']['ug']['BSc Electronics']
            return f"⚡ *BSc Electronics*\nDuration: {details['duration']}\nEligibility: {details['eligibility']}\nCareers: {details['career']}"
        
        if 'bca' in q:
            details = self.college_data['courses']['ug']['BCA (Bachelor of Computer Applications)']
            return f"💼 *BCA (Bachelor of Computer Applications)*\nDuration: {details['duration']}\nEligibility: {details['eligibility']}\nCareers: {details['career']}"
        
        if 'commerce' in q or 'bcom' in q or 'mcom' in q:
            info = "📊 *Commerce Programs:*\n\n"
            for name, details in {**self.college_data['courses']['ug'], **self.college_data['courses']['pg']}.items():
                if 'Com' in name:
                    info += f"*{name}*\n"
                    info += f"  Duration: {details['duration']}\n"
                    info += f"  Careers: {details['career']}\n\n"
            return info.strip()
        
        # All courses
        info = "📚 *All Courses at CAS Vattamkulam:*\n\n"
        info += "*UNDERGRADUATE PROGRAMS:*\n"
        for name, details in self.college_data['courses']['ug'].items():
            info += f"\n• {name} ({details['duration']})\n"
            info += f"  Eligibility: {details['eligibility']}\n"
        
        info += "\n\n*POSTGRADUATE PROGRAMS:*\n"
        for name, details in self.college_data['courses']['pg'].items():
            info += f"\n• {name} ({details['duration']})\n"
            info += f"  Eligibility: {details['eligibility']}\n"
        
        info += f"\n\n✓ Affiliated to {self.college_data['basic_info']['affiliation']}"
        return info
    
    def get_admission_info(self):
        """Admission information"""
        adm = self.college_data['admission']
        info = "📝 *ADMISSION GUIDE 2025-26*\n\n"
        info += f"*Status:* {adm['status']}\n"
        info += f"*Last Date:* {adm['registration_period']}\n"
        info += f"*Seats:* {adm['seats_distribution']}\n\n"
        
        info += "*ADMISSION PROCESS:*\n"
        for step in adm['admission_process']:
            info += f"{step}\n"
        
        info += "\n*REQUIRED DOCUMENTS:*\n"
        for doc in adm['required_documents']:
            info += f"• {doc}\n"
        
        info += f"\n*APPLY ONLINE:*\n"
        for portal, link in adm['registration_links'].items():
            info += f"• {portal}: {link}\n"
        
        info += f"\n*Contact:* {adm['contact_admission']}"
        return info
    
    def get_fees_info(self):
        """Fee information"""
        adm = self.college_data['admission']
        info = "💰 *FEE STRUCTURE*\n\n"
        info += "*Application Fee:*\n"
        for category, amount in adm['application_fee'].items():
            info += f"• {category}: {amount}\n"
        info += "\n*Note:* Course fees will be as per University of Calicut norms.\n"
        info += "Contact college office for detailed fee structure."
        return info
    
    def get_nss_info(self):
        """NSS information"""
        nss = self.college_data['nss']
        info = "🌟 *NATIONAL SERVICE SCHEME (NSS)*\n\n"
        info += f"*Objective:* {nss['objective']}\n\n"
        
        info += "*KEY ACTIVITIES:*\n"
        for activity in nss['activities'][:8]:
            info += f"• {activity}\n"
        
        info += f"\n*Special Programs:*\n"
        info += f"• {nss['special_camps']}\n"
        info += f"• {nss['regular_activities']}\n"
        
        info += "\n*ACHIEVEMENTS:*\n"
        for achievement in nss['achievements']:
            info += f"• {achievement}\n"
        
        info += "\n*BENEFITS:*\n"
        for benefit in nss['benefits']:
            info += f"✓ {benefit}\n"
        
        return info
    
    def get_clubs_info(self, query):
        """Clubs information"""
        q = query.lower()
        clubs = self.college_data['clubs']
        
        # Specific club
        if 'computer' in q:
            club = clubs['Computer Association']
            info = "💻 *COMPUTER ASSOCIATION*\n\n"
            info += "*Activities:*\n"
            for act in club['activities']:
                info += f"• {act}\n"
            info += f"\n*Major Event:* {club['events']}\n"
            info += f"*Benefits:* {club['benefits']}"
            return info
        
        if 'electronics' in q:
            club = clubs['Electronics Association']
            info = "⚡ *ELECTRONICS ASSOCIATION*\n\n"
            info += "*Activities:*\n"
            for act in club['activities']:
                info += f"• {act}\n"
            info += f"\n*Focus:* {club['focus']}\n"
            info += f"*Benefits:* {club['benefits']}"
            return info
        
        if 'commerce' in q:
            club = clubs['Commerce Association']
            info = "📊 *COMMERCE ASSOCIATION*\n\n"
            info += "*Activities:*\n"
            for act in club['activities']:
                info += f"• {act}\n"
            info += f"\n*Benefits:* {club['benefits']}"
            return info
        
        # All clubs
        info = "🎯 *CLUBS & ASSOCIATIONS*\n\n"
        for club_name, club_data in clubs.items():
            info += f"*{club_name}*\n"
            activities = club_data.get('activities', [])
            if activities:
                info += f"  Key Activities: {', '.join(activities[:3])}\n\n"
        
        info += "✓ Active student participation\n"
        info += "✓ Skill development focus\n"
        info += "✓ Industry exposure"
        return info
    
    def get_placement_info(self):
        """Placement information"""
        pl = self.college_data['placement']
        info = "💼 *PLACEMENT CELL*\n\n"
        info += f"*Coordinator:* {pl['coordinator']}\n"
        info += f"*Contact:* {pl['email']}, {pl['phone']}\n\n"
        
        info += "*TRAINING PROGRAMS:*\n"
        for training in pl['training']:
            info += f"• {training}\n"
        
        info += "\n*TOP RECRUITERS:*\n"
        for company in pl['top_recruiters']:
            info += f"• {company}\n"
        
        info += f"\n*Placement Rate:* {pl['placement_rate']}\n\n"
        
        info += "*PLACEMENT ACTIVITIES:*\n"
        for activity in pl['activities']:
            info += f"• {activity}\n"
        
        return info
    
    def get_facilities_info(self):
        """Facilities information"""
        fac = self.college_data['facilities']
        info = "🏫 *CAMPUS FACILITIES*\n\n"
        
        info += "*Academic Facilities:*\n"
        for f in fac['Academic']:
            info += f"• {f}\n"
        
        info += "\n*Laboratory Facilities:*\n"
        for f in fac['Laboratory']:
            info += f"• {f}\n"
        
        info += "\n*Library Facilities:*\n"
        for f in fac['Library']:
            info += f"• {f}\n"
        
        info += "\n*Sports Facilities:*\n"
        for f in fac['Sports']:
            info += f"• {f}\n"
        
        info += "\n*Other Facilities:*\n"
        for f in fac['Other']:
            info += f"• {f}\n"
        
        return info
    
    def get_departments_info(self):
        """Department information"""
        dept = self.college_data['departments']
        info = "🏛️ *ACADEMIC DEPARTMENTS*\n\n"
        
        for name, details in dept.items():
            info += f"*Department of {name}*\n"
            if isinstance(details, dict):
                courses = details.get('courses')
                if isinstance(courses, list):
                    info += f"  Courses: {', '.join(courses)}\n"
                else:
                    info += f"  Courses: {courses}\n"
            info += "\n"
        
        return info
    
    def get_contact_info(self):
        """Contact information"""
        info = self.college_data['basic_info']
        contact = "📞 *CONTACT INFORMATION*\n\n"
        contact += f"*{info['name']}*\n\n"
        contact += f"*Address:*\n"
        contact += f"{info['location']}\n"
        contact += f"{info['district']}, {info['state']}\n"
        contact += f"PIN: {info['pin']}\n\n"
        contact += f"*Phone:* {', '.join(info['phone'])}\n"
        contact += f"*Email:* {info['email']}\n"
        contact += f"*Website:* {info['website']}\n\n"
        contact += f"*Academic Session:* {info['academic_session']}\n"
        contact += "*Office Hours:* Mon-Sat, 9:00 AM - 5:00 PM"
        return contact
    
    def get_about_info(self):
        """About information"""
        info_data = self.college_data['basic_info']
        info = "🎓 *ABOUT CAS VATTAMKULAM*\n\n"
        info += f"*Established:* {info_data['established']}\n"
        info += f"*Management:* {info_data['management']}\n"
        info += f"*Affiliation:* {info_data['affiliation']}\n"
        info += f"*Faculty:* {info_data['faculty_count']} qualified teachers\n\n"
        
        info += f"*VISION:*\n{self.college_data['vision']}\n\n"
        info += f"*MISSION:*\n{self.college_data['mission']}\n\n"
        
        info += "*KEY FEATURES:*\n"
        info += "• Quality education with modern infrastructure\n"
        info += "• Industry-oriented curriculum\n"
        info += "• Strong placement support\n"
        info += "• Active student clubs and activities\n"
        info += "• Holistic development focus"
        return info
    
    def get_events_info(self):
        """Events information"""
        events = self.college_data['events']
        info = "🎉 *COLLEGE EVENTS & ACTIVITIES*\n\n"
        
        for event_name, event_data in events.items():
            info += f"*{event_name}*\n"
            if isinstance(event_data, dict):
                for key, value in event_data.items():
                    if key != 'type':
                        info += f"  {key.title()}: {value}\n"
            info += "\n"
        
        return info
    
    def get_cells_info(self):
        """Other cells information"""
        cells = self.college_data['other_cells']
        info = "🛡️ *STUDENT WELFARE CELLS*\n\n"
        
        for cell_name, cell_data in cells.items():
            info += f"*{cell_name}*\n"
            info += f"Purpose: {cell_data['purpose']}\n"
            
            activities = cell_data.get('activities', cell_data.get('functions', cell_data.get('features', [])))
            if activities:
                info += "Activities:\n"
                for act in activities[:5]:
                    info += f"  • {act}\n"
            
            if 'policy' in cell_data:
                info += f"Policy: {cell_data['policy']}\n"
            info += "\n"
        
        return info
    
    def get_union_info(self):
        """College union information"""
        union = self.college_data['college_union']
        info = "🏆 *COLLEGE UNION*\n\n"
        info += f"*Purpose:* {union['purpose']}\n\n"
        
        info += "*Positions:*\n"
        for pos in union['positions']:
            info += f"• {pos}\n"
        
        info += "\n*Activities:*\n"
        for act in union['activities']:
            info += f"• {act}\n"
        
        info += f"\n*Current:* {union['recent']}"
        return info
    
    def get_help_menu(self):
        """Help menu"""
        menu = "🎓 *CAS VATTAMKULAM CHATBOT - HELP MENU*\n\n"
        menu += "I can help you with:\n\n"
        menu += "📚 *ACADEMICS*\n"
        menu += "  • Courses & Programs\n"
        menu += "  • Admission Process & Fees\n"
        menu += "  • Departments & Faculty\n\n"
        menu += "🏫 *FACILITIES*\n"
        menu += "  • Campus Infrastructure\n"
        menu += "  • Labs & Library\n"
        menu += "  • Sports Facilities\n\n"
        menu += "🌟 *ACTIVITIES*\n"
        menu += "  • NSS Programs\n"
        menu += "  • Clubs & Associations\n"
        menu += "  • Events & Fests\n"
        menu += "  • College Union\n\n"
        menu += "💼 *PLACEMENT*\n"
        menu += "  • Training Programs\n"
        menu += "  • Recruiters & Jobs\n"
        menu += "  • Career Support\n\n"
        menu += "🛡️ *STUDENT WELFARE*\n"
        menu += "  • Women Cell\n"
        menu += "  • Anti-Ragging Cell\n"
        menu += "  • Grievance Cell\n\n"
        menu += "📞 *CONTACT & LOCATION*\n\n"
        menu += "*Try asking:*\n"
        menu += "  'What courses are available?'\n"
        menu += "  'How to apply for admission?'\n"
        menu += "  'Tell me about NSS activities'\n"
        menu += "  'What clubs are there?'\n"
        menu += "  'Placement details'\n"
        menu += "  'Campus facilities'\n"
        return menu
    
    def chat(self):
        """Main chat interface"""
        print("="*70)
        print(f"       🎓 {self.bot_name} 🎓")
        print("="*70)
        print("\n✓ Loaded with COMPLETE college information!")
        print("  • All Courses & Admission Details")
        print("  • NSS & All Clubs")
        print("  • Placement Information")
        print("  • Events & Activities")
        print("  • All Facilities & Contact Info\n")
        print("Type 'help' for menu or 'quit' to exit.\n")
        print("-"*70 + "\n")
        
        while True:
            try:
                user_input = input("You: ").strip()
                
                if not user_input:
                    continue
                
                if user_input.lower() in ['quit', 'exit', 'q', 'bye', 'goodbye']:
                    print(f"\n{self.bot_name}: Thank you for visiting CAS Vattamkulam!")
                    print("🌐 Website: https://casvattamkulam.ihrd.ac.in")
                    print("📞 Call: 0494-2689655, 8547006802\n")
                    break
                
                if user_input.lower() in ['help', 'menu']:
                    response = self.get_help_menu()
                else:
                    response = self.generate_response(user_input)
                
                self.conversation_history.append(('user', user_input))
                self.conversation_history.append(('bot', response))
                
                print(f"\n{self.bot_name}:\n{response}\n")
                print("-"*70 + "\n")
                
            except KeyboardInterrupt:
                print("\n\nGoodbye!")
                break
            except Exception as e:
                print(f"\n{self.bot_name}: Sorry, I encountered an error. Please try again.\n")

if __name__ == "__main__":
    try:
        bot = CASVattamkulamChatbot()
        bot.chat()
    except Exception as e:
        print(f"Error: {e}")
