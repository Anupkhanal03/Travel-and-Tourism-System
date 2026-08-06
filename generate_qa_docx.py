import docx
from docx.shared import Pt, RGBColor

def add_heading(doc, text, level=1):
    heading = doc.add_heading(text, level=level)
    run = heading.runs[0]
    run.font.color.rgb = RGBColor(0, 0, 0)
    run.font.name = 'Arial'
    if level == 1:
        run.font.size = Pt(14)
        run.bold = True
    elif level == 2:
        run.font.size = Pt(12)
        run.bold = True

def add_qa(doc, q, a):
    p_q = doc.add_paragraph()
    run_q = p_q.add_run(q)
    run_q.bold = True
    run_q.font.name = 'Arial'
    run_q.font.size = Pt(11)

    p_a = doc.add_paragraph()
    run_a = p_a.add_run(a)
    run_a.font.name = 'Arial'
    run_a.font.size = Pt(11)

def generate_qa_doc(output_file):
    doc = docx.Document()
    
    title = doc.add_heading('Project Defense Q&A Preparation', 0)
    title.runs[0].font.color.rgb = RGBColor(0, 0, 0)

    # Roles
    add_heading(doc, 'Preparation for project')
    add_heading(doc, 'Role of individual in project', level=2)
    doc.add_paragraph('Frontend = Anup Chhetri, Ashim Thapa')
    doc.add_paragraph('Backend = Anup Khanal, Sangam Bagale Regmi')

    # UI/Frontend
    add_heading(doc, 'UI (Frontend)')
    add_qa(doc, '1. Kun kun technology', 'Answer: We used HTML, CSS, JavaScript, and Bootstrap for styling.')
    add_qa(doc, '2. UI ko part kasle gareyko?', 'Answer: The UI part was primarily handled by Anup Chhetri and Ashim Thapa.')
    add_qa(doc, '3. Website responsive xa? K tool use garera responsive garako', 'Answer: Yes, the website is responsive. We used the Bootstrap grid system and CSS media queries to ensure it works on all screen sizes.')
    add_qa(doc, '4. Kun existing system bata frontend inspire xa', 'Answer: The frontend was inspired by modern travel websites like MakeMyTrip and Booking.com, focusing on a clean and user-friendly interface.')
    add_qa(doc, '5. Client side validation xa?', 'Answer: Yes, we used HTML5 attributes (like required, type="email") and custom JavaScript for client-side form validation before submitting data.')

    # Backend
    add_heading(doc, 'Backend')
    add_qa(doc, '1. What backend framework did you use and why?', 'Answer: We used Flask (Python). We chose Flask because it is lightweight, flexible, and makes it easy to integrate with our AI components (chatbot and recommender system).')
    add_qa(doc, '2. Explain how the booking process works.', 'Answer: Users browse packages and click "Book". Upon form submission, the booking details are saved in our database with a "Pending" status until payment is processed.')
    add_qa(doc, '3. What happens after a booking is confirmed?', 'Answer: The booking status in the database changes to "Confirmed", and the user can view and download a receipt for their trip.')
    add_qa(doc, '4. Explain your dummy payment system.', 'Answer: Since we don\'t have a live merchant account, we implemented a simulated payment gateway. When the user clicks pay, it simulates processing and updates the database record.')
    add_qa(doc, '5. Why did you use a dummy payment instead of a real payment gateway?', 'Answer: Getting a real payment gateway API (like eSewa) requires a registered business. For academic purposes, a dummy system demonstrates the flow without needing real credentials.')
    add_qa(doc, '6. How is receipt information stored?', 'Answer: The receipt details are generated dynamically from the booking records stored in our database.')
    add_qa(doc, '7. How would you integrate a real payment gateway in the future?', 'Answer: We would obtain API keys from the provider, send the payload with the booking amount to their endpoint, and handle the callback URL to update our booking status.')
    add_qa(doc, '8. What bugs did you encounter and how did you solve them?', 'Answer: We faced issues with database routing in Flask. We solved them by modularizing our code and structuring our database connections properly.')
    add_qa(doc, '9. How does the chatbot system works?', 'Answer: The chatbot uses the Google Gemini API. The user\'s query is sent to the backend, processed by the AI with our travel context, and the response is sent back.')
    add_qa(doc, '10. What security tools are used to protect website from unauthorized users?', 'Answer: We implemented session management and route protection. Users must be logged in to access booking features, and the admin panel requires separate authentication.')
    add_qa(doc, '11. Any encryption techniques used?', 'Answer: Yes, we used password hashing (Werkzeug security helpers) to hash user passwords before storing them in the database.')
    add_qa(doc, '12. How did you test your project?', 'Answer: We performed manual testing for UI/UX and unit testing for critical backend functions.')

    # General Questions
    add_heading(doc, 'General questions')
    add_qa(doc, '1. What makes your system different from existing travel booking websites?', 'Answer: Our system integrates an intelligent AI chatbot for instant support and a personalized recommendation engine tailored specifically for Nepal.')
    add_qa(doc, '2. What technologies and tools did you use?', 'Answer: HTML/CSS/JS/Bootstrap (Frontend), Python/Flask (Backend), SQLite/MySQL (Database), Scikit-learn/Gemini API (AI).')
    add_qa(doc, '3. What did each member contribute?', 'Answer: Anup Khanal: Backend API and Chatbot. Anup Chhetri: UI/UX design. Ashim Thapa: Frontend logic. Sangam Bagale Regmi: Database and recommendation engine.')
    add_qa(doc, '4. How long did the project take to complete?', 'Answer: The project took approximately 6-8 weeks from planning to testing.')
    add_qa(doc, '5. How would your system support thousands of users?', 'Answer: We can scale by using a robust production server like Gunicorn, optimizing database queries, and using cloud hosting.')
    add_qa(doc, '6. How is the receipt generated and downloaded automatically?', 'Answer: We use a Python library (like ReportLab) to generate a PDF file on the fly based on the user\'s booking data.')
    add_qa(doc, '7. How do you prevent unauthorized users from accessing the admin panel?', 'Answer: We enforce role-based access control. Only users with an "admin" flag can access the /admin routes.')
    add_qa(doc, '8. If you were to deploy this project, what changes would you make?', 'Answer: I would use a robust database like PostgreSQL, set up proper SSL/HTTPS, and use environment variables for API keys.')
    add_qa(doc, '9. What software development methodology did you follow?', 'Answer: We followed an Agile methodology, with iterative development allowing us to continuously integrate new features.')

    # Technical Questions
    add_heading(doc, 'Technical question that can be asked')
    add_qa(doc, '1. What is hashing?', 'Answer: Hashing is the process of converting data into a fixed-size string of characters, which is a one-way function used to securely store passwords.')
    add_qa(doc, '2. Why did you choose your framework over other frameworks?', 'Answer: We chose Flask because it is a micro-framework that is easy to learn and integrates seamlessly with Python AI libraries.')
    add_qa(doc, '3. What is API?', 'Answer: API stands for Application Programming Interface. It is a set of rules that allows different software applications to communicate with each other.')
    add_qa(doc, '4. What is the difference between HTTP and HTTPS?', 'Answer: HTTP transmits data in plain text, whereas HTTPS encrypts the data using SSL/TLS, making it secure.')
    add_qa(doc, '5. What is the difference between synchronous and asynchronous programming?', 'Answer: Synchronous programming executes tasks sequentially (blocking), while asynchronous programming allows multiple tasks to run concurrently without blocking the main thread.')

    doc.save(output_file)
    print(f"Docx QA file generated successfully at {output_file}")

if __name__ == "__main__":
    generate_qa_doc("Project_QA.docx")
