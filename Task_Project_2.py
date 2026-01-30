# Import Streamlit library
import streamlit as st


# -----------------------------
# Page Configuration
# -----------------------------

# Set page title and layout
st.set_page_config(
    page_title="Owl AI Web Interface",
    layout="centered"
)


# -----------------------------
# Sidebar Navigation
# -----------------------------

# Sidebar title
st.sidebar.title("Owl AI Menu")

# Sidebar navigation options
page = st.sidebar.radio(
    "Navigate",
    ["Home", "About Owl AI", "Interact with Owl AI", "Feedback"]
)


# -----------------------------
# HOME PAGE
# -----------------------------

if page == "Home":

    # Main heading
    st.title("Owl AI")

    # Introduction content
    st.write(
        "Owl AI is an intelligent assistant designed to help users "
        "with learning, problem-solving, and daily productivity."
    )

    # Additional descriptive content
    st.write(
        "This web interface is built as part of Task 2 using Streamlit. "
        "It demonstrates a clean layout, user interaction, and navigation."
    )

    # Highlight section
    st.subheader("Key Features")
    st.write("- Simple and clean user interface")
    st.write("- Interactive input and output")
    st.write("- Sidebar-based navigation")
    st.write("- Beginner-friendly implementation")

    # Divider
    st.write("---")

    # Call-to-action text
    st.info("Use the menu on the left to explore different sections.")


# -----------------------------
# ABOUT PAGE
# -----------------------------

elif page == "About Owl AI":

    # Page title
    st.title("About Owl AI")

    # Detailed description
    st.write(
        "Owl AI is designed to act as a smart assistant that can interact "
        "with users through text-based input. The goal of Owl AI is to "
        "provide helpful responses in a simple and accessible way."
    )

    st.write(
        "This project focuses on building a basic web interface rather "
        "than implementing advanced AI logic. The emphasis is on UI, "
        "navigation, and user interaction."
    )

    # Section header
    st.subheader("Technologies Used")

    # Technology list
    st.write("- Python")
    st.write("- Streamlit")
    st.write("- Command-Line and Web Interface Concepts")

    # Divider
    st.write("---")

    st.success("This interface can be extended with real AI logic later.")


# -----------------------------
# INTERACTION PAGE
# -----------------------------

elif page == "Interact with Owl AI":

    # Page title
    st.title("Interact with Owl AI")

    # Instructions for users
    st.write("Enter your details and message below to interact with Owl AI.")

    # Input field for user name
    user_name = st.text_input("Enter your name")

    # Input field for user query or message
    user_query = st.text_area("Enter your question or message")

    # Submit button
    if st.button("Send to Owl AI"):

        # Validate input
        if user_name and user_query:

            # Display user input as response
            st.subheader("Owl AI Response")
            st.write(f"Hello {user_name},")
            st.write(
                "Thank you for your message. "
                "Owl AI has received your query successfully."
            )

            # Display the user's message
            st.write("Your message:")
            st.write(user_query)

        else:
            # Warning for missing input
            st.warning("Please enter both your name and message.")


# -----------------------------
# FEEDBACK PAGE
# -----------------------------

elif page == "Feedback":

    # Page title
    st.title("Feedback")

    # Feedback instructions
    st.write(
        "We value your feedback. Please share your experience "
        "using the Owl AI web interface."
    )

    # Rating input
    rating = st.selectbox(
        "Rate your experience",
        ["Excellent", "Good", "Average", "Needs Improvement"]
    )

    # Feedback text area
    feedback_text = st.text_area("Write your feedback here")

    # Submit feedback button
    if st.button("Submit Feedback"):

        # Check if feedback is provided
        if feedback_text:
            st.success("Thank you for your feedback!")
            st.write("Your Rating:", rating)
            st.write("Your Feedback:")
            st.write(feedback_text)
        else:
            st.warning("Please write some feedback before submitting.")


# -----------------------------
# Footer (Visible on all pages)
# -----------------------------

st.write("---")
st.write("Owl AI Web Interface | Built using Streamlit")
