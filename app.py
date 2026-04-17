import streamlit as st
from api_calling import note_generator,audio_transcription,quiz_generator
from PIL import Image

st.title("Note Summay and Quiz Generator")
st.markdown("Upload upto 3 images to generate Note summary and Quizzes")
st.divider()


with st.sidebar:
    st.header("Controls")
    images =st.file_uploader(
        "UPload the photos of your note",
        type=['jpg','jpeg','png'],
        accept_multiple_files=True
    )
    pil_images = []
    for img in images:
        pil_img = Image.open(img)
        pil_images.append(pil_img)


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
    selected_option = st.selectbox(
        "Enter the difficulty of your quiz ",
    ("Easy","Medium","Hard"),
    index = None
    )

    pressed = st.button("Click the button to initiate AI",type="primary")


if pressed:
    if not images: 
        st.error("You must upload atleast 1 image")
    if not selected_option:
        st.error("You must select a difficulty")

    if images and selected_option:

        # For Note: 

        with st.container(border=True):
            generated_notes = note_generator(pil_images)
            st.subheader("Your note")

            # The portion below will be replaced by api calls:
            
            with st.spinner("AI is writing notes for you"):

                # Clearing markdown : 
                generated_notes = generated_notes.replace("#","")
                generated_notes= generated_notes.replace("*","")
                generated_notes=generated_notes.replace("-","")
                generated_notes=generated_notes.replace("`","")
                generated_notes=generated_notes.replace("","")

                st.markdown(generated_notes)

# Audio Transcript : 

        with st.container(border=True):
            st.subheader("Audio Transcription")

            with st.spinner("Ai is transcripting your notes") : 
            # The portion below will be replaced by api calls:
                audio_transcript = audio_transcription(generated_notes)
                st.audio(audio_transcript)


# Quiz : 
        with st.container(border=True):
            st.subheader(f"Quiz Difficulty: {selected_option}")

            # The portion below will be replaced by api calls:

            with st.spinner("AI is generating the quizzes"):
                quizzes = quiz_generator(pil_images,selected_option)
                st.markdown(quizzes)
