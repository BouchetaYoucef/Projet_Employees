# # https://gist.github.com/FranzDiebold/898396a6be785d9b5ca6f3706ef9b0bc
# """Hack to add per-session state to Streamlit.
# Works for Streamlit >= v0.65
# Usage
# -----
# import SessionState

# session_state = SessionState.get(user_name='', favorite_color='black')
# session_state.user_name
# ''
# session_state.user_name = 'Mary'
# session_state.favorite_color
# 'black'
# Since you set user_name above, next time your script runs this will be the
# result:
# session_state = get(user_name='', favorite_color='black')
# session_state.user_name
# 'Mary'
# """

# import streamlit.report_thread as ReportThread
# from streamlit.server.server import Server


# class SessionState():
#     """SessionState: Add per-session state to Streamlit."""
#     def __init__(self, **kwargs):
#         """A new SessionState object.
#         Parameters
#         ----------
#         **kwargs : any
#             Default values for the session state.
#         Example
#         -------
#          session_state = SessionState(user_name='', favorite_color='black')
#          session_state.user_name = 'Mary'
#         ''
#         session_state.favorite_color
#         'black'
#         """
#         for key, val in kwargs.items():
#             setattr(self, key, val)


# def get(**kwargs):
#     """Gets a SessionState object for the current session.
#     Creates a new object if necessary.
#     Parameters
#     ----------
#     **kwargs : any
#         Default values you want to add to the session state, if we're creating a
#         new one.
#     Example
#     -------
#      session_state = get(user_name='', favorite_color='black')
#      session_state.user_name
#     ''
#      session_state.user_name = 'Mary'
#      session_state.favorite_color
#     'black'
#     Since you set user_name above, next time your script runs this will be the
#     result:
#      session_state = get(user_name='', favorite_color='black')
#      session_state.user_name
#     'Mary'
#     """
#     # Hack to get the session object from Streamlit.

#     session_id = ReportThread.get_report_ctx().session_id
#     session_info = Server.get_current()._get_session_info(session_id)

#     if session_info is None:
#         raise RuntimeError('Could not get Streamlit session object.')

#     this_session = session_info.session

#     # Got the session object! Now let's attach some state into it.

#     if not hasattr(this_session, '_custom_session_state'):
#         this_session._custom_session_state = SessionState(**kwargs)

#     return this_session._custom_session_state















import json

import requests
import streamlit as st

# def run():
#     img1 = open('Employees.jpg')
#     img1 = img1.resize((150,150))
#     st.image(img1,use_column_width=False)
# run()

def get_inputs():
    """Get inputs from users on streamlit"""
    st.title("Predict employee future")

    data = {}

    data["City"] = st.selectbox(
        "City Office Where Posted",
        options=["Bangalore", "Pune", "New Delhi"],
    )
    data["PaymentTier"] = st.selectbox(
        "Payment Tier",
        options=[1, 2, 3],
        help="payment tier: 1: highest 2: mid level 3:lowest",
    )
    data["Age"] = st.number_input(
        "Current Age", min_value=15, step=1, value=20
    )
    data["Gender"] = st.selectbox("Gender", options=["Male", "Female"])
    data["EverBenched"] = st.selectbox(
        "Ever Kept Out of Projects for 1 Month or More", options=["No", "Yes"]
    )
    data["ExperienceInCurrentDomain"] = st.number_input(
        "Experience in Current Field", min_value=0, step=1, value=1
    )
    return data


def write_predictions(data: dict):
    if st.button("Will this employee leave in 2 years?"):
        data_json = json.dumps(data)

        prediction = requests.post(
            # "https://employee-predict-1.herokuapp.com/predict",
            headers={"content-type": "application/json"},
            data=data_json,
        ).text[0]

        if prediction == "0":
            st.write("This employee is predicted stay more than two years.")
        else:
            st.write("This employee is predicted to leave in two years.")


def main():
    data = get_inputs()
    write_predictions(data)


if __name__ == "__main__":
    main()