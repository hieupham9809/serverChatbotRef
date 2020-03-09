from temp_agent_action_gen import *
from message_handler import *
from agen_response_gen import *

#TEST
if __name__ == '__main__':
    user_action = process_message_to_user_request("mình thích âm nhạc thì đi mùa hè xanh khoa máy tính được không")
    agent_act = get_agent_response(state_tracker, dqn_agent, user_action)
    print(response_craft(agent_act, state_tracker))
    state_tracker = StateTracker(database, constants)
    dqn_agent = DQNAgent(state_tracker.get_state_size(), constants)
    user_action = process_message_to_user_request("mình thích âm nhạc thì đi mùa hè xanh khoa máy tính được không")

    agent_act = get_agent_response(state_tracker, dqn_agent, user_action)
    print(response_craft(agent_act, state_tracker))
    state_tracker = StateTracker(database, constants)
    dqn_agent = DQNAgent(state_tracker.get_state_size(), constants)
    user_action = process_message_to_user_request("mình thích âm nhạc thì đi mùa hè xanh khoa máy tính được không")

    agent_act = get_agent_response(state_tracker, dqn_agent, user_action)
    print(response_craft(agent_act, state_tracker))