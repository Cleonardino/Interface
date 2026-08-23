from discord import Message
import state_manager as sm
from id_manager import create_unique_fake_id
from synthetize import synthetize
from sending import try_send_order

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
    
    output_message : str = "`ERROR:UNRECOGNIZED COMMAND////////////\nTYPE HELP TO GET LIST OF COMMANDS`"
    
    # Synthetize
    if content.startswith("synt"):
        output_message = synthetize(user_id=user_id)
    
    # Help
    if content.startswith("help"):
        if "tune" in content:
            output_message = """`////////////TUNING HELP==`
`Tuning is the final step for completing the interface. When every user`
`is tuned to the interface, all will be over`       
`help tune             --- print this message`
`tune(FREQ) PHASE      --- tune with user with id USER_ID using`
`                          frequency FREQ`
`freq                  --- get frequency information`
`                          be used by other users to tune with you.`
`                          The tuning frequency is updated every 3 minutes`
"""
        else:
            output_message = """`////////////HELP==`
`help                  --- print this message`
`send(USER_ID) MESSAGE --- send a message to the user with id USER_ID`
`synt                  --- synthetize a piece of information`
`stabilize(USER_ID)    --- stabilize message sending device of user`
`                          with id USER_ID`
`help tune             --- print the tuning help message`
"""
            
    
    # Sending
    if content.startswith("send"):
        open_par : int = content.find("(")
        close_par : int = content.find(")")
        if open_par < 0 or close_par < 0 or open_par >= close_par:
            output_message = "`ERROR:SEND SYNTAX IS 'SEND(TARGET_ID) MESSAGE'`"
        else:
            output_message = try_send_order(
                source=sm.state[sm.SM_USERS][user_id][sm.USR_FAKE_ID],
                target=content[open_par+1:close_par],
                content=content[close_par+1:],
                stabilized=sm.state[sm.SM_USERS][user_id][sm.USR_STABLE]
            )
    
    await message.author.send(output_message)