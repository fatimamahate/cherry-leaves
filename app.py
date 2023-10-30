
import streamlit as st
from app_pages.multi_page import MultiPage
from app_pages.hypothesis import hypothesis_ml

app = MultiPage(app_name = "Cherry Leaves")

app.app_page("Hypothesis",hypothesis_ml)

app.run()



