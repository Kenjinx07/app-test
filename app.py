import streamlit as st

# Simulate fetching user data (replace with actual database or API calls)
def fetch_user(user_id):
    # Simulated user data
    return {
        "F_Name": "John",
        "M_Name": "Doe",
        "L_Name": "Smith",
        "Email": "john.doe@example.com",
        "Contact_No": "1234567890"
    }

# Page title
st.title("Edit Profile")

# User session (replace with actual session handling logic)
user_id = st.session_state.get("user_id", "12345")  # Simulated session user ID
user = fetch_user(user_id)

# Profile editing form
st.header("Update Profile")
with st.form("profile_form"):
    F_Name = st.text_input("First Name", value=user["F_Name"])
    M_Name = st.text_input("Middle Name", value=user["M_Name"])
    L_Name = st.text_input("Last Name", value=user["L_Name"])
    Email = st.text_input("Email", value=user["Email"])
    Contact_No = st.text_input("Phone Number", value=user["Contact_No"])
    Password = st.text_input("Password", type="password")
    submit = st.form_submit_button("Save Changes")

if submit:
    # Handle profile update logic here
    st.success("Profile updated successfully!")

# ID verification form
st.header("Verify Identification")
with st.form("id_verification_form"):
    front_image = st.file_uploader("Front of ID", type=["png", "jpg", "jpeg"])
    back_image = st.file_uploader("Back of ID", type=["png", "jpg", "jpeg"])
    verify = st.form_submit_button("Submit for Verification")

if verify:
    if front_image and back_image:
        # Simulate ID verification logic
        st.success("Verification successful!")
        # Example: Display uploaded images
        st.image(front_image, caption="Front of ID", use_column_width=True)
        st.image(back_image, caption="Back of ID", use_column_width=True)
    else:
        st.error("Please upload both the front and back of your ID.")

# Footer
st.markdown("---")
st.write("Thank you for updating your profile!")
