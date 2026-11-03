
import streamlit as st
from PIL import Image, ImageDraw
from io import BytesIO
import random

# Page configuration
st.set_page_config(
    page_title="Lyric2Poster",
    page_icon="🎵",
    layout="wide"
)

# Sidebar
with st.sidebar:
    st.header("Access")
    st.info("Demo mode - No API key required")
    st.write("Briefs left: 10")
    st.write("Posters left: 6")

# Main page
st.title("🎵 Lyric2Poster")
st.write("Turn your favorite song into a poster!")

# Step 1: Choose a song
st.header("Step 1: Choose a Song")

chart = st.selectbox(
    "Chart",
    [
        "Top Tracks: Korea",
        "Top Tracks: Global"
    ]
)

songs = [
    "Ditto - NewJeans",
    "You're Under Arrest - ILLIT",
    "Looks Can Kill - IVE",
    "Pop - ILLIT",
    "Other Song"
]

song = st.selectbox("Song", songs)

if song == "Other Song":
    title = st.text_input("Song Title")
    artist = st.text_input("Artist")
else:
    title, artist = song.rsplit(" - ", 1)

# Step 2: Write the art brief
st.header("Step 2: Write the Art Brief")

lyrics = st.text_area(
    "Paste Lyrics Here",
    placeholder="Enter the song lyrics...",
    height=180
)

if st.button("Generate Art Brief"):
    if lyrics.strip():
        st.session_state["brief"] = True
        st.success("Art brief generated successfully!")
    else:
        st.warning("Please enter the lyrics first.")

if st.session_state.get("brief", False):
    st.subheader("Art Brief")

    st.write("**Mood:** Dreamy and Emotional")
    st.write("**Imagery:** Light, Stars, and Motion")
    st.write("**Color Palette:** Purple, Pink, and Blue")
    st.write("**Style:** Abstract and Atmospheric")

    st.caption(
        "Demo mode: This is a preset art brief, "
        "not an AI analysis of the lyrics."
    )

# Step 3: Generate the poster
st.header("Step 3: Make the Poster")

style = st.selectbox(
    "Poster Style",
    [
        "Dreamy",
        "Minimal",
        "Retro",
        "Cyberpunk"
    ]
)

if st.button("Generate Poster"):

    if not title.strip():
        st.warning("Please enter a song title.")

    else:
        # Define poster background colors
        colors = {
            "Dreamy": "#9575CD",
            "Minimal": "#777777",
            "Retro": "#D88C45",
            "Cyberpunk": "#253A80"
        }

        # Create a blank poster
        img = Image.new(
            "RGB",
            (800, 1000),
            colors[style]
        )

        draw = ImageDraw.Draw(img)

        # Add decorative circles
        rng = random.Random(42)

        for i in range(25):
            x = rng.randint(0, 800)
            y = rng.randint(0, 1000)
            r = rng.randint(20, 120)

            draw.ellipse(
                (x - r, y - r, x + r, y + r),
                outline="white",
                width=3
            )

        # Add song title
        draw.text(
            (50, 790),
            title[:30],
            fill="white"
        )

        # Add artist name
        draw.text(
            (50, 850),
            artist[:40],
            fill="white"
        )

        # Display the generated poster
        st.subheader("Your Generated Poster")

        st.image(
            img,
            width=450
        )

        # Convert image to PNG
        buffer = BytesIO()
        img.save(buffer, format="PNG")

        # Download button
        st.download_button(
            label="Download Poster",
            data=buffer.getvalue(),
            file_name="lyric2poster.png",
            mime="image/png"
        )

        st.success("Poster generated successfully!")
