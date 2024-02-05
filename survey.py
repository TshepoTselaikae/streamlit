
import streamlit as st
import pandas as pd
from datetime import datetime

# Function to save responses to a CSV file
def save_responses(responses):
    filename = 'vaal_university_library_survey_responses.csv'
    try:
        df = pd.DataFrame([responses])
        df.to_csv(filename, mode='a', header=not pd.io.parsers.read_csv(filename, nrows=0).size, index=False)
        st.success("Thank you for your responses. They have been saved successfully.")
    except Exception as e:
        st.error(f"An error occurred while saving your responses: {e}")

def main():
    st.title("New Library Project at Vaal University Survey")

    with st.form("survey_form", clear_on_submit=True):
        st.write("Please answer the following questions about the new library project at Vaal University in Gauteng:")
        
        # Questions
        q1 = st.radio("How familiar are you with the new library project at Vaal University in Gauteng?",
                      ["Not familiar at all", "Somewhat familiar", "Very familiar"])
        
        q2 = st.radio("Do you support the construction of the new library at Vaal University?",
                      ["Yes", "No", "Unsure"])
        
        q3 = st.text_input("What concerns do you have regarding the new library project? (Separate concerns with commas)")
        
        q4 = st.text_area("What benefits do you think the new library will bring to Vaal University?")
        
        submitted = st.form_submit_button("Submit")
        
        if submitted:
            responses = {
                "Timestamp": datetime.now(),
                "Familiarity with the project": q1,
                "Support for the construction": q2,
                "Concerns": q3,
                "Perceived benefits": q4
            }
            save_responses(responses)

if __name__ == "__main__":
    main()
