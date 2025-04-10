
import streamlit as st
from streamlit_drawable_canvas import st_canvas
import random

st.set_page_config(page_title="AI Doodle Critic", layout="centered")
st.title("🎨 AI Doodle Critic")
st.write("Draw anything you like and let our AI Critic give you some hilarious feedback!")

canvas_result = st_canvas(
    fill_color="rgba(255, 255, 255, 0.5)",
    stroke_width=5,
    stroke_color="#000000",
    background_color="#ffffff",
    height=300,
    width=400,
    drawing_mode="freedraw",
    key="canvas",
)

funny_comments = [
    "🧐 Is it a bird? Is it a cloud? Whatever it is, it’s magnificent!",
    "🎩 Picasso would definitely want your autograph.",
    "😲 This belongs in a museum... or maybe outer space!",
    "😂 I’ve never seen anything like it. 12/10 for creativity!",
    "🎉 That doodle just cured my boredom. You’re a genius!",
    "🌈 It’s so mysterious, I want to hang it on my wall!",
    "🔥 This doodle is on fire! (Metaphorically... I hope.)",
    "💡 Did you just invent a new art style? I think you did!",
    "🐒 Even monkeys would stop to admire this!",
    "👑 Royalty should see this masterpiece!"
]

if st.button("🧠 Get Critique"):
    if canvas_result.image_data is not None:
        comment = random.choice(funny_comments)
        st.subheader("AI Critic Says:")
        st.success(comment)
    else:
        st.warning("Please draw something first!")
