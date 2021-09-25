import streamlit as st
import streamlit.server.server as streamlit_server
x = st.slider('Select a value')
st.write(x, 'squared is', x * x)
# st.
# if __name__ == "__main__":
#     pass


# from streamlit.cli import main
# from tornado.wsgi import WSGIContainer
# from tornado.web import FallbackHandler

# from dtale.app import build_app


# orig_start_listening = streamlit_server.start_listening


# def _override_start_listening(app):
#     dtale_app_obj = build_app(reaper_on=False)
#
#     tr = WSGIContainer(dtale_app_obj)
#     app.add_handlers(r".*", [(".*dtale.*", FallbackHandler, dict(fallback=tr))])
#     orig_start_listening(app)


# streamlit_server.start_listening = _override_start_listening