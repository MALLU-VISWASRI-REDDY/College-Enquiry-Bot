
import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

# --------------------------------------------------
# 1. PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="RGMCET College Chatbot",
    page_icon="🎓",
    layout="centered"
)

# --------------------------------------------------
# 2. LOAD ENVIRONMENT VARIABLES
# --------------------------------------------------

load_dotenv()

# Read the API key from .env or Streamlit secrets
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    try:
        GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
    except Exception:
        GROQ_API_KEY = None

# --------------------------------------------------
# 3. INITIALIZE GROQ CLIENT
# --------------------------------------------------

if not GROQ_API_KEY:
    st.error(
        "Groq API key not found. Add GROQ_API_KEY to your .env file."
    )
    st.stop()

try:
    client = Groq(api_key=GROQ_API_KEY)
except Exception as e:
    st.error(f"Unable to initialize Groq: {e}")
    st.stop()

# --------------------------------------------------
# 4. COLLEGE KNOWLEDGE BASE
# --------------------------------------------------

COLLEGE_KNOWLEDGE = """
COLLEGE NAME:
Rajeev Gandhi Memorial College of Engineering and Technology (RGMCET)

LOCATION:
Nandyal, Andhra Pradesh, India.

CHAIRMAN:
Dr. M. Santhiramudu.
For current official information, refer to the college website.

OFFICIAL WEBSITE:
https://www.rgmcet.edu.in/

COMPUTER SCIENCE AND ENGINEERING (CSE):

Head of Department:
Dr. K. Subba Reddy - Professor and Head of the Department (HOD),
according to the CSE faculty page.

Official CSE faculty page:
https://www.rgmcet.edu.in/cse_faculty.php

Faculty names listed on the CSE faculty page include:
1. Dr. K. Subba Reddy
2. Dr. Rajaboina Raja Kumar
3. Dr. M. Sravan Kumar Reddy
4. Dr. K. Narsimhulu
5. Dr. P. Sreedevi
6. Dr. M. Ayyavaraiah
7. P. Naveen Sundar Kumar
8. Hrishikesava Reddy C
9. K. Janardhan
10. Vaka Ravikanth
11. D. Sravanthi
12. D. Karishma

IMPORTANT:
This list is based on information previously available on the official
CSE faculty page. Faculty positions and staff lists can change.
Users should check the official faculty page for the latest details.

CSE DEPARTMENT:
Official department page:
https://www.rgmcet.edu.in/department-of-cse

The department page has information about the CSE programme,
department facilities, faculty, and intake.

COURSES OFFERED:

Undergraduate engineering programmes listed on the college website
include the following:

1. Civil Engineering
2. Electrical and Electronics Engineering (EEE)
3. Mechanical Engineering
4. Electronics and Communication Engineering (ECE)
5. Computer Science and Engineering (CSE)
6. CSE - Data Science
7. CSE - Artificial Intelligence and Machine Learning
8. CSE - Cyber Security
9. CSE and Business Systems

The exact availability and intake of each programme may change.
Check the official website for the latest approved list.

Official courses page:
https://www.rgmcet.edu.in/courses_offered

Additional courses page:
https://rgmcet.edu.in/courses_offered1

POSTGRADUATE PROGRAMMES:

The college website has listed postgraduate programmes in areas
including engineering, computer science, management, and computer
applications.

Examples listed on the website include:
- Computer Aided and Structural Engineering
- Electrical Drives and Control
- Energy Engineering
- VLSI Design
- Computer Science
- MBA
- MCA

Check the official courses page to verify current programme availability.

FEE STRUCTURE:

The official fee information previously available for academic years
2023-24 through 2025-26 listed the following tuition fees:

- B.Tech: Rs. 59,400
- M.Tech: Rs. 50,000
- MBA: Rs. 51,300
- MCA: Rs. 60,000

IMPORTANT FEE NOTICE:
These are historical figures for the academic years stated above.
They are NOT confirmed fees for 2026-27.

The final amount payable may differ depending on the programme,
admission category, government rules, and other applicable charges.

Official fee page:
https://rgmcet.edu.in/feestructure

PLACEMENTS:

The official placement records page previously listed:

Academic year 2025-26:
- 597 student offers
- 63 companies visited
- Placement cycle marked as in progress at the time of the published data.

Academic year 2024-25:
- 471 offers
- 20 companies visited.

Academic year 2023-24:
- 900 offers
- 44 companies visited.

IMPORTANT:
Offers are not necessarily the same as the number of unique students placed.
Placement statistics can change as the placement cycle progresses.

Official placement records:
https://www.rgmcet.edu.in/Placement_Records

OFFICIAL CONTACT AND INFORMATION:

For current admissions, fee details, faculty information, course
availability, and other official announcements, visit:

https://www.rgmcet.edu.in/
"""

# --------------------------------------------------
# 5. SYSTEM PROMPT
# --------------------------------------------------

SYSTEM_PROMPT = """
You are the RGMCET College Enquiry Chatbot.

Your purpose is to answer questions about Rajeev Gandhi Memorial
College of Engineering and Technology (RGMCET), Nandyal, Andhra Pradesh.

RESPONSE RULES:

1. Answer clearly, politely, and in simple English.

2. Use the supplied COLLEGE KNOWLEDGE BASE as your primary source.

3. Answer questions about:
   - College information
   - Chairman
   - Departments
   - CSE HOD
   - CSE faculty
   - Courses offered
   - Fee structure
   - Placements
   - Admissions
   - Official college links

4. If asked who the CSE HOD is, use the name provided in the knowledge
   base and mention that the official faculty page should be checked
   for the latest information.

5. If asked about CSE faculty, provide the available names from the
   knowledge base. Do not claim that the list is necessarily complete
   or current.

6. If asked about fees, always mention the academic year associated
   with the figures. Do not present historical fees as confirmed
   2026-27 fees.

7. If a question requires information that is not present in the
   knowledge base, clearly say that the information is not available
   in your current college information.

8. When appropriate, provide the relevant official website URL from
   the knowledge base.

9. Do not invent faculty names, phone numbers, email addresses,
   admission dates, fees, eligibility criteria, or placement figures.

10. Do not claim that you visited or checked a webpage during this
    conversation. The knowledge base may contain previously collected
    information.

11. If the user asks about a topic unrelated to RGMCET, politely
    explain that you specialize in RGMCET college enquiries.

12. Use bullet points for lists of courses, faculty, fees, and
    placement information.

13. Distinguish between verified information, historical information,
    and information that needs confirmation.

14. Do not reveal API keys, environment variables, or internal
    configuration details.

15. Keep answers relevant to the user's question. Avoid unnecessarily
    repeating the entire knowledge base.
"""

# --------------------------------------------------
# 6. APPLICATION TITLE AND DESCRIPTION
# --------------------------------------------------

st.title("🎓 RGMCET College Enquiry Chatbot")

st.write(
    "Welcome! Ask me about RGMCET, Nandyal, including departments, "
    "CSE faculty, courses, fees, and placements."
)

st.caption(
    "College information assistant | Check the official website "
    "for the latest announcements."
)

st.markdown("---")

# --------------------------------------------------
# 7. SIDEBAR
# --------------------------------------------------

with st.sidebar:
    st.header("🎓 RGMCET")

    st.write("Rajeev Gandhi Memorial College of Engineering and Technology")

    st.write("📍 Nandyal, Andhra Pradesh")

    st.markdown(
        "[Official College Website](https://www.rgmcet.edu.in/)"
    )

    st.markdown(
        "[CSE Faculty](https://www.rgmcet.edu.in/cse_faculty.php)"
    )

    st.markdown(
        "[Courses Offered](https://www.rgmcet.edu.in/courses_offered)"
    )

    st.markdown(
        "[Fee Structure](https://rgmcet.edu.in/feestructure)"
    )

    st.markdown(
        "[Placement Records](https://www.rgmcet.edu.in/Placement_Records)"
    )

    st.markdown("---")

    st.subheader("💡 Try asking")

    st.write("• Who is the chairman of RGMCET?")
    st.write("• Who is the HOD of CSE?")
    st.write("• List the CSE faculty members.")
    st.write("• What courses does RGMCET offer?")
    st.write("• What is the B.Tech fee?")
    st.write("• Tell me about placements.")

    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# --------------------------------------------------
# 8. INITIALIZE CHAT HISTORY
# --------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# --------------------------------------------------
# 9. DISPLAY PREVIOUS MESSAGES
# --------------------------------------------------

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --------------------------------------------------
# 10. GET USER INPUT
# --------------------------------------------------

user_prompt = st.chat_input(
    "Ask a question about RGMCET..."
)

if user_prompt:

    # Save and display the user's question
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(user_prompt)

    # --------------------------------------------------
    # 11. GENERATE THE RESPONSE
    # --------------------------------------------------

    with st.chat_message("assistant"):

        with st.spinner("Finding an answer..."):

            try:
                # Construct the complete conversation
                api_messages = [
                    {
                        "role": "system",
                        "content": (
                            SYSTEM_PROMPT
                            + "\n\nCOLLEGE KNOWLEDGE BASE:\n"
                            + COLLEGE_KNOWLEDGE
                        )
                    }
                ]

                # Include previous conversation messages
                api_messages.extend(
                    st.session_state.messages
                )

                # Send the request to Groq
                response = client.chat.completions.create(
                    model="openai/gpt-oss-120b",
                    messages=api_messages,
                    temperature=0.2,
                    max_tokens=800
                )

                assistant_response = (
                    response.choices[0].message.content
                )

                if not assistant_response:
                    assistant_response = (
                        "Sorry, I could not generate a response. "
                        "Please try asking your question again."
                    )

                # Display the response
                st.markdown(assistant_response)

                # Save the response in chat history
                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": assistant_response
                    }
                )

            except Exception as e:
                st.error(
                    "An error occurred while generating the response."
                )

                st.info(
                    "Check your internet connection, Groq API key, "
                    "model availability, and installed packages."
                )

                # Print technical details in the terminal
                print(f"Groq API error: {e}")
