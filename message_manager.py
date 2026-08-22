from discord import Message
import state_manager as sm
from id_manager import create_unique_fake_id
from synthetize import synthetize

async def process_message(message : Message):
    user_id = str(message.author.id)
    if user_id not in sm.state[sm.SM_USERS]:
        # User not in database, add it and associate a unique id
        fake_id = create_unique_fake_id()
        # Add id to table used for indexation
        sm.state[sm.SM_FAKE_IDS][fake_id] = user_id
        # Create user
        sm.state[sm.SM_USERS][user_id] = {
		    sm.USR_FAKE_ID: fake_id
		}
        sm.save_state()
    
    # Detecting commands and valid messages
    content : str = message.content.lower()
    
    # Synthetize
    if content.startswith("synt"):
        await message.author.send(synthetize(user_id=user_id))