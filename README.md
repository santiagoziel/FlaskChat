# FlaskChat
### Proposal for a different way to handle group chats.

This chat room, allows for an user, I will refer to as user_a, to select as many online users they want to talk to, for example user_b and user_c, and talk to them, with out creating a communication channel for user_b and user_c.

Three things **will** happen.
- user_b and user_c will get notified
- messages sent by user_a will be delivered to user_b and user_c.
- messages sent by either user_b or user_c will be delivered to user_a

what **will not** happen.
- messages sent by user_b will not be delivered to user_c
- messages sent by user_c will not be delivered to user_b

### Requirements
- Python 3.9 or higher with pip enabled
- pipenv installed
  - to install run:
          pip install pipenv

## How to Use
        git clone https://github.com/santiagoziel/FlaskChat.git
        cd FlaskChat
        pipenv shell
        pipenv install
        python3 run.py
**navigate to** http://127.0.0.1:5000 and go nuts.
### TODO
- [ ] improve general look
- [ ] improve online users look
- [ ] display differentiate from diff users messages
- [ ] fix user system to have unique usernames
