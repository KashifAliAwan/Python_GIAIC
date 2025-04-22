# import streamlit as st
# from datetime import datetime

# # Configure the page
# st.set_page_config(
#     page_title="My Python Website",
#     page_icon="🚀",
#     layout="wide"
# )

# # Sidebar navigation
# st.sidebar.title("Navigation")
# page = st.sidebar.radio("Go to", ["🏠 Home", "📝 Blog", "💻 Projects", "📩 Contact"])

# # Home Page
# if page == "🏠 Home":
#     st.title("Welcome to My Python Website! 🎉")
#     st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", width=300)
#     st.write("""
#     This is a **fully functional website** built in **15 minutes** using Streamlit!
    
#     Features:
#     - ✅ **Multi-page navigation**
#     - ✅ **Blog posts**
#     - ✅ **Projects showcase**
#     - ✅ **Contact form**
#     - ✅ **Responsive design**
#     """)

# # Blog Page
# elif page == "📝 Blog":
#     st.title("📝 My Blog")
#     st.write("Here are my latest posts:")

#     # Sample blog posts
#     posts = {
#         "How I Built This Website in 15 Minutes": "Streamlit is amazing! Here's how I did it...",
#         "Python Tips for Beginners": "Top 5 Python tricks you should know.",
#         "Why I Love Data Science": "My journey into machine learning."
#     }

#     for title, content in posts.items():
#         with st.expander(title):
#             st.write(content)
#             st.caption(f"Published on {datetime.now().strftime('%B %d, %Y')}")

# # Projects Page
# elif page == "💻 Projects":
#     st.title("💻 My Projects")
#     st.write("Check out my latest work!")

#     # Project cards
#     col1, col2 = st.columns(2)
    
#     with col1:
#         st.subheader("BMI Calculator")
#         st.image("https://via.placeholder.com/300x200", width=200)
#         st.write("A simple BMI calculator app.")
#         st.code("pip install streamlit")

#     with col2:
#         st.subheader("Password Generator")
#         st.image("https://via.placeholder.com/300x200", width=200)
#         st.write("Generates secure passwords.")
#         st.code("pip install secrets")

# # Contact Page
# elif page == "📩 Contact":
#     st.title("📩 Get in Touch")
    
#     with st.form("contact_form"):
#         name = st.text_input("Name")
#         email = st.text_input("Email")
#         message = st.text_area("Message")
#         submitted = st.form_submit_button("Send")
        
#         if submitted:
#             st.success("✅ Thanks! Your message has been sent.")
#             st.balloons()  # Celebration animation!










# num_float = 3.5
# print(type(num_float))


# complex_number : complex = 3 + 5j
# print(f"Its type is : {type(complex_number)} Out Will {complex_number} ")
# print(f"its a real number {complex_number.real}")
# print(f"its a Image number {complex_number.imag}")

# foods = list()  # ✅ Using list constructor safely

# while (food := input("Please Enter Food: ")) != "quit":
#     foods.append(food)
    
# print(foods)


# num1 : int = int(input("Please Enter First Digit "))
# operator : str = input("Please Enter an Operator ")
# num2 : int = int(input("Please Enter Second Digit "))

# if operator == "+":
#  print(num1 + num2)
# elif operator == "-":
#  print(num1 - num2)
# elif operator == "*":
#  print(num1 * num2) 
# elif operator == "/":
#  print(num1 / num2)
# else:
#  print("Please Select Corect Operator")



















num1 : int = int(input("Please Enter First Digit "))
operator : str = input("Please Enter an Operator ")
num2 : int = int(input("Please Enter Second Digit "))

if operator == "+":
 print(num1 + num2)
elif operator == "-":
 print(num1 - num2)
elif operator == "*":
 print(num1 * num2) 
elif operator in ["/", "//"] and num2 == 0:
    print("Error: Cannot divide by zero.")
elif operator == "/":
 print(num1 / num2)
elif operator == "//":
 print(num1 // num2)
else:
 print("Please Select Corect Operator")



