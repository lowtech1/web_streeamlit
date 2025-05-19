import streamlit as st

from streamlit_option_menu import option_menu

import about, account, home, trending, your_post


st.set_page_config(
    page_title="Pondering",
)

class MultiApp:
    def __init__(self):
        self.apps = []
    def add_app(self, title, function):
        self.apps.append(
            {
                "title": title,
                "function": function
            }
        )
    def run():
        #thiết kế thanh trược 
        with st.sidebar:
            app = option_menu(
                menu_title="Pondering",
                options=['Home', 'Account', 'Trending', 'Your Posts', 'About'],
                icons=['house-fill', 'person-circle', 'trophy-fill', 'chat-fill', 'info-circle-fill'],
                menu_icon = 'chat-text-fill',
                default_index=1,
                styles={
                    "container":{"padding": "5!important",}
                }
            )
        if app=='Home':
            home.app() 
        if app=='Account':
            account.app()
        if app=='Trending':
            trending.app()
        if app=='About':
            about.app()
        if app=='Your Posts':
            your_post.app()
    run()


