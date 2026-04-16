import streamlit as st

st.title("Note Summay and Quiz Generator")
st.markdown("Upload upto 3 images to generate Note summary and Quizzes")
st.divider()


with st.sidebar:
    st.header("Controls")
    images = st.file_uploader(
        "UPload the photos of your note",
        type=['jpg','jpeg','png'],
        accept_multiple_files=True
    )

    if images:
        if len(images)>3:
            st.error("Upload at max 3 images")
        else:
            col = st.columns(len(images))
            
            st.subheader("Uploaded images")

            for i,img in enumerate(images):
                with col[i]:
                    st.image(img)



    # Dificluty : 
    selecte_option = st.selectbox(
        "Enter the difficulty of your quiz ",
    ("Easy","Medium","Hard"),
    index = None
    )
    if selecte_option:
        st.markdown(f"You selected **{selecte_option}** as dificulty of your quiz")
    else:
        st.error("You must select a difficulty")

    st.button("Click the button to initiate AI",type="primary")
