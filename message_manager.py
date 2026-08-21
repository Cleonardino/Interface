from discord import Message
import state_manager as st
from id_manager import create_unique_fake_id


def process_message(message : Message):
    user_id = message.author.id
    if user_id not in st.state["users"]:
        # User not in database, add it and associate a unique id
        fake_id = create_unique_fake_id()
        # Add id to table used for indexation
        st.state["fake_ids"][fake_id] = user_id
        # Create user
        st.state["users"][user_id] = {
			"fake_id": fake_id
		}
        st.save_state()