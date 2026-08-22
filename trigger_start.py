import state_manager as sm

id_list = []
for user_id in sm.state[sm.SM_USERS]:
    # Create list
    id_list.append(user_id)
    # Initialize synt_rot
    sm.state[sm.SM_USERS][user_id][sm.USR_SYNT_ROT] = 0
    sm.state[sm.SM_USERS][user_id][sm.USR_SYNT_MAX] = 6

# Link last to first
sm.state[sm.SM_USERS][id_list[len(id_list)-1]][sm.USR_TARGET] = sm.state[sm.SM_USERS][id_list[0]][sm.USR_FAKE_ID]
for i in range(len(id_list)-1):
    # Link one to the next
    sm.state[sm.SM_USERS][id_list[i]][sm.USR_TARGET] = sm.state[sm.SM_USERS][id_list[i+1]][sm.USR_FAKE_ID]

sm.save_state()