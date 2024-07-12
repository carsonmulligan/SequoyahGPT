import streamlit as st

# Cherokee poem in syllabary
poem = """
ᎠᏯᏣᏓᎡᏫᏍᎩ
ᎠᏯ ᏙᏯ ᎠᏯ
ᎦᏙ ᏗᎦᏙᏯ
ᎠᏓᏙᏯ ᎠᏓᏯ
ᏓᏓᏙᏯ ᎦᏙᏯ
"""

# Function to split the poem into lines
def split_into_lines(poem):
    return poem.strip().split('\n')

# Main app
st.title("Cherokee Poem Memorization")

st.write("### Cherokee Poem in Syllabary")
st.write(poem)

lines = split_into_lines(poem)

# Interactive Flashcards
st.write("### Flashcards")
current_index = st.slider("Line number", 0, len(lines)-1, 0)
st.write(lines[current_index])

# Add tips for using memory techniques
st.write("### Memory Techniques Tips")
st.write("""
- Visualize a familiar place. - 
- Associate each line with a specific location in that place.
- Walk through the place in your mind to recall the lines in order.
""")

# Optional: Add audio support (requires audio file)
# st.write("### Listen to the Poem")
# st.audio("path_to_audio_file.mp3")
