import streamlit as st

# Quiz questions
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": "Mars"
    },
    {
        "question": "What is 2 + 2?",
        "options": ["3", "4", "5", "6"],
        "answer": "4"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["Charles Dickens", "William Shakespeare", "Mark Twain", "Jane Austen"],
        "answer": "William Shakespeare"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
        "answer": "Pacific Ocean"
    }
]

# Initialize session state for score and current question
if "score" not in st.session_state:
    st.session_state.score = 0
if "current_question" not in st.session_state:
    st.session_state.current_question = 0

# Display the current question
def display_question():
    question_data = questions[st.session_state.current_question]
    st.write(f"**Question {st.session_state.current_question + 1}:** {question_data['question']}")
    
    # Display options as buttons
    user_answer = st.radio("Select your answer:", question_data["options"], key=f"question_{st.session_state.current_question}")
    
    # Submit button
    if st.button("Submit"):
        if user_answer == question_data["answer"]:
            st.session_state.score += 1
            st.success("Correct! 🎉")
        else:
            st.error(f"Wrong! The correct answer is: {question_data['answer']}")
        
        # Move to the next question
        st.session_state.current_question += 1
        
        # Reset the radio button selection
        st.session_state[f"question_{st.session_state.current_question}"] = None

# Check if the quiz is finished
def quiz_finished():
    if st.session_state.current_question >= len(questions):
        st.write("## Quiz Finished!🎉")
        st.write(f"### Your final score is: {st.session_state.score}/{len(questions)}")
        if st.button("Restart Quiz"):
            st.session_state.score = 0
            st.session_state.current_question = 0
        return True
    return False

# Main app logic
def main():
    st.title("Python Quiz App 🐍")
    st.write("Test your knowledge with this fun quiz!")
    
    if not quiz_finished():
        display_question()

# Run the app
if __name__ == "__main__":
    main()