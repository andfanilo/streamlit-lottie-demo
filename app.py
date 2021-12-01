import json
import time

import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner


def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_streamlit = load_lottiefile("./lottiefiles/Streamlit Logo Animation.json")
lottie_progress = load_lottiefile("./lottiefiles/44327-animated-rocket-icon.json")
lottie_success = load_lottiefile("./lottiefiles/26514-check-success-animation.json")
lottie_error = load_lottiefile("./lottiefiles/38463-error.json")

st.set_page_config(page_title="Streamlit Lottie Demo", page_icon=":tada:", initial_sidebar_state='collapsed')

st.title("Hello Lottie!")
st.markdown(
    """
[Lottie](https://airbnb.io/lottie) is a library that parses [Adobe After Effects](http://www.adobe.com/products/aftereffects.html) animations 
exported as json with [Bodymovin](https://github.com/airbnb/lottie-web) and renders them natively on mobile and on the web!

Go look at the [awesome animations](https://lottiefiles.com/) to spice your Streamlit app!
"""
)

with st.sidebar:
    st.header("Animation parameters")
    speed = st.slider("Select speed", 0.1, 2.0, 1.0)
    reverse = st.checkbox("Reverse direction", False)
st_lottie(lottie_streamlit, speed=speed, reverse=reverse, height=400, key="initial")

with st.sidebar:
    st.markdown("---")
    st.markdown(
        '<h6>Made in &nbsp<img src="https://streamlit.io/images/brand/streamlit-mark-color.png" alt="Streamlit logo" height="16">&nbsp by <a href="https://twitter.com/andfanilo">@andfanilo</a></h6>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div style="margin-top: 0.75em;"><a href="https://www.buymeacoffee.com/andfanilo" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a></div>',
        unsafe_allow_html=True
    )

c_col1, colx, c_col2, coly = st.columns((1, 0.1, 0.25, 1))
if c_col1.button("Run some heavy computation...for 5 seconds!"):
    with c_col2.empty():
        with st_lottie_spinner(lottie_progress, loop=True, key="progress"):
            time.sleep(5)
        st_lottie(lottie_success, loop=False, key="success")

st.markdown("---")
st.header("Try it yourself!")
st.markdown(
    "Choose a Lottie from [the website](https://lottiefiles.com/) and paste its 'Lottie Animation URL'"
)
lottie_url = st.text_input(
    "URL", value="https://assets5.lottiefiles.com/packages/lf20_V9t630.json"
)
downloaded_url = load_lottieurl(lottie_url)

if downloaded_url is None:
    col1, col2 = st.columns((2, 1))
    col1.warning(f"URL {lottie_url} does not seem like a valid lottie JSON file")
    with col2:
        st_lottie(lottie_error, height=100, key="error")
else:
    with st.echo("above"):
        st_lottie(downloaded_url, key="user")