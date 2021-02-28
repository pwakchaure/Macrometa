import json
import requests
import responses
import logging

from util import *


@responses.activate
def test_create_conversation(jwt_auth_header):
    logging.info(f"Creating the conversation")
    stub(
        responses.POST,
        "https://api.nexmo.com/v0.1/conversations",
        fixture_path="conversation/create_conversation.json",
    )

    params = { "name": "customer_chat_test", "display_name": "Customer Chat Test", \
    "image_url": "https://example.com/image.png", "properties": {"ttl": 60}}
    
    response = requests.post("https://api.nexmo.com/v0.1/conversations", headers=jwt_auth_header, \
        data=json.dumps(params))

    logging.info(f"Checking POST request response is 200")
    assert response.status_code == 200
    logging.info(f"Checking id from POST request response")
    response_body = response.json()
    assert response_body["id"] == "CON-63f61863-4a51-4f6b-86e1-46edebio0391"
    logging.info(f"Creation of conversation completed successfully")


@responses.activate
def test_list_conversations(jwt_auth_header):
    logging.info(f"Listing the conversations")
    stub(        
        responses.GET,
        "https://api.nexmo.com/v0.1/conversations",
        fixture_path="conversation/list_conversations.json",
    )

    response = requests.get("https://api.nexmo.com/v0.1/conversations", headers=jwt_auth_header)

    logging.info(f"Checking GET request response is 200")
    assert response.status_code == 200
    response_body = response.json()
    logging.info(f"Checking 'count' from response json")
    assert response_body["count"] == "100"
    logging.info(f"Listing of conversations completed successfully")


@responses.activate
def test_update_conversation(jwt_auth_header):
    logging.info(f"Updating the conversation")
    stub(        
        responses.PUT,
        "https://api.nexmo.com/v0.1/conversations/xx-xx-xx-xx",
        fixture_path="conversation/update_conversation.json",
    )  

    params = {"name": "customer_chat_test", "display_name": "Customer Chat Test", \
        "image_url": "https://example.com/image.png", "properties": {"ttl": 60}}

    response = requests.put("https://api.nexmo.com/v0.1/conversations/xx-xx-xx-xx", headers=jwt_auth_header, \
        data=json.dumps(params))
    
    logging.info(f"Checking PUT request response is 200")
    assert response.status_code == 200
    logging.info(f"Checking 'id' from response json")
    response_body = response.json()
    assert response_body["id"] == "CON-63f61863-4a51-4f6b-86e1-46edebio0391"
    logging.info(f"Updation of conversation completed successfully")


@responses.activate
def test_retrieve_conversation(jwt_auth_header):
    logging.info(f"Retrieving the conversation")
    stub(
        responses.GET,
        "https://api.nexmo.com/v0.1/conversations/xx-xx-xx-xx",
        fixture_path="conversation/get_conversation.json",
    )

    response = requests.get("https://api.nexmo.com/v0.1/conversations/xx-xx-xx-xx", headers=jwt_auth_header)

    logging.info(f"Checking GET request response is 200")
    assert response.status_code == 200
    logging.info(f"Checking the 'name' of the conversation in response json")
    response_body = response.json()
    assert response_body["name"] == "customer_chat_test"
    logging.info(f"Retrieving of the conversation completed successfully")


@responses.activate
def test_delete_conversation(jwt_auth_header):
    logging.info(f"Deleting the conversation")
    stub(
        responses.DELETE,
        "https://api.nexmo.com/v0.1/conversations/xx-xx-xx-xx",
    )

    response = requests.delete("https://api.nexmo.com/v0.1/conversations/xx-xx-xx-xx", headers=jwt_auth_header)
    
    logging.info(f"Checking DELETE request response is 200")
    assert response.status_code == 200
    logging.info(f"Successfully deleted the conversation")


@responses.activate
def test_record_conversation(jwt_auth_header):
    logging.info(f"Recording the conversation")
    stub(
        responses.PUT,
        "https://api.nexmo.com/v1/conversations/xx-xx-xx-xx/record",
    )

    params = {"action": "start"}
    response = requests.put("https://api.nexmo.com/v1/conversations/xx-xx-xx-xx/record", headers=jwt_auth_header, \
        data=json.dumps(params))
    
    logging.info(f"Checking PUT request response is 200/404/400")
    assert response.status_code == 200
    if response.status_code == 404:
        pytest.fail(f"This endpoint does not support application/json")
    elif response.status_code == 400:
        pytest.fail(f"This endpoint does not support application/json")
    logging.info(f"Successfully recorded conversation")


@responses.activate
def test_list_users(jwt_auth_header):
    logging.info(f"Listing the users")
    stub(
        responses.GET,
        "https://api.nexmo.com/v0.1/users",
        fixture_path="users/list_users.json",
    )

    response = requests.get("https://api.nexmo.com/v0.1/users", headers=jwt_auth_header)

    logging.info(f"Checking GET request response is 200")
    assert response.status_code == 200
    logging.info(f"Checking 'my_user_name' in response json")
    response_body = response.json()
    assert "my_user_name" in str(response_body)
    logging.info(f"Lising of users completed successfully")


@responses.activate
def test_create_user(jwt_auth_header):
    logging.info(f"Creating the user")
    stub(
        responses.POST,
        "https://api.nexmo.com/v0.1/users",
        fixture_path="users/create_user.json",
    )

    params = {"name": "my_user_name", "display_name": "My User Name", "image_url": "https://example.com/image.png"}
    response = requests.post("https://api.nexmo.com/v0.1/users", headers=jwt_auth_header, params=json.dumps(params))

    logging.info(f"Checking POST request response is 200")
    assert response.status_code == 200
    logging.info(f"Checking 'id' in response json")
    response_body = response.json()
    assert response_body["id"] == "USR-63f61863-4a51-4f6b-86e1-46edebio0391"
    logging.info(f"User creation completed successfully")


@responses.activate
def test_retrieve_user(jwt_auth_header):
    logging.info(f"Retrieving user information")
    stub(
        responses.GET,
        "https://api.nexmo.com/v0.1/users/xx-xx-xx-xx",
        fixture_path="users/get_user.json",
    )

    response = requests.get("https://api.nexmo.com/v0.1/users/xx-xx-xx-xx", headers=jwt_auth_header)

    logging.info(f"Checking GET request response is 200")
    assert response.status_code == 200
    logging.info(f"Checking 'name' in response json")
    response_body = response.json()
    assert response_body["name"] == "my_user_name"
    logging.info(f"Successfully retrieved user information")


@responses.activate
def test_update_user(jwt_auth_header):
    logging.info(f"Updating the user information")
    stub(
        responses.PUT,
        "https://api.nexmo.com/v0.1/users/xx-xx-xx-xx",
        fixture_path="users/update_user.json",
    )

    params = {"name": "my_user_name", "display_name": "My User Name", "image_url": "https://example.com/image.png", \
        "channels": {"type": "phone","leg_id": "a595959595959595995","leg_ids": [{"leg_id": "a595959595959595995"}]}}
    response = requests.put("https://api.nexmo.com/v0.1/users/xx-xx-xx-xx", headers=jwt_auth_header, data=json.dumps(params))

    logging.info(f"Checking the PUT request response is 200")
    assert response.status_code == 200
    logging.info(f"Checking 'id' in request response json")
    response_body = response.json()
    assert response_body["id"] == "USR-63f61863-4a51-4f6b-86e1-46edebio0391"
    logging.info(f"Successfully updated the user information")


@responses.activate
def test_delete_user(jwt_auth_header):
    logging.info(f"Deleting the user")
    stub(
        responses.DELETE,
        "https://api.nexmo.com/v0.1/users/xx-xx-xx-xx",
    ) 

    response = requests.delete("https://api.nexmo.com/v0.1/users/xx-xx-xx-xx", headers=jwt_auth_header)

    logging.info(f"Checking DELETE request response is 200")
    assert response.status_code == 200   
    logging.info(f"Successfully deleted the user")


@responses.activate
def test_list_user_conversation(jwt_auth_header):
    logging.info(f"Listing the user conversation")
    stub(
        responses.GET,
        "https://api.nexmo.com/v0.1/users/xx-xx-xx-xx/conversations",
        fixture_path="users/list_user_conversation.json"
    )

    response = requests.get("https://api.nexmo.com/v0.1/users/xx-xx-xx-xx/conversations", headers=jwt_auth_header)

    logging.info(f"Checking GET request response is 200")
    assert response.status_code == 200
    logging.info(f"Checking the 'customer_chat_test' name in response json")
    response_body = response.json()
    assert "customer_chat_test" in str(response_body)
    logging.info(f"Successfully listed the user conversation") 


@responses.activate
def test_list_members(jwt_auth_header):
    logging.info(f"Listing the members")
    stub(
        responses.GET,
        "https://api.nexmo.com/v0.1/conversations/xx-xx-xx-xx/members",
        fixture_path="member/list_members.json",
    )

    response = requests.get("https://api.nexmo.com/v0.1/conversations/xx-xx-xx-xx/members", headers=jwt_auth_header)

    logging.info(f"Checking GET request response is 200")
    assert response.status_code == 200
    logging.info(f"Checking 'my_user_name' user name in response json")
    response_body = response.json()
    assert "my_user_name" in str(response_body)
    logging.info(f"Successfully listed members")


@responses.activate
def test_create_member(jwt_auth_header):
    logging.info(f"Creating the member")
    stub(
        responses.POST,
        "https://api.nexmo.com/v0.1/conversations/xx-xx-xx-xx/members",
        fixture_path="member/create_member.json",
    )

    params = {"user_id": "USR-63f61863-4a51-4f6b-86e1-46edebio0391"}
    response = requests.post("https://api.nexmo.com/v0.1/conversations/xx-xx-xx-xx/members", headers=jwt_auth_header, \
        data=json.dumps(params))

    logging.info(f"Checking POST request rsponse is 201")
    assert response.status_code == 201
    logging.info(f"Checking 'user_id' in response json")
    response_body = response.json()
    assert response_body["user_id"] == "USR-63f61863-4a51-4f6b-86e1-46edebio0391"
    logging.info(f"Successfully created the member")


@responses.activate
def test_retrieve_member(jwt_auth_header):
    logging.info(f"Retrieving member")
    stub(
        responses.GET,
        "https://api.nexmo.com/v0.1/conversations/xx-xx-xx-xx/members/xx-xx-xx-xx",
        fixture_path="member/get_member.json",
    )

    response = requests.get("https://api.nexmo.com/v0.1/conversations/xx-xx-xx-xx/members/xx-xx-xx-xx", headers=jwt_auth_header)

    logging.info(f"Checking GET request response is 200")
    assert response.status_code == 200
    logging.info(f"Checking 'id' in response json")
    response_body = response.json()
    assert response_body["id"] == "MEM-63f61863-4a51-4f6b-86e1-46edebio0391"
    logging.info(f"Successfully retrieved member")


@responses.activate
def test_update_member(jwt_auth_header):
    logging.info(f"Updating the member")
    stub(
        responses.PUT,
        "https://api.nexmo.com/v0.1/conversations/xx-xx-xx-xx/members/xx-xx-xx-xx",
        fixture_path="member/update_member.json",
    )

    params = {"action": "join","channel": {"type": "phone","leg_id": "a595959595959595995", \
        "leg_ids": [{"leg_id": "a595959595959595995"}]}}
    response = requests.put("https://api.nexmo.com/v0.1/conversations/xx-xx-xx-xx/members/xx-xx-xx-xx", headers=jwt_auth_header, \
        data=json.dumps(params))

    logging.info(f"Checking PUT request response is 200")
    assert response.status_code == 200
    logging.info(f"Checking id in response json")
    response_body = response.json()
    assert response_body["id"] == "MEM-63f61863-4a51-4f6b-86e1-46edebio0391"
    logging.info(f"Successfully updated the member")


@responses.activate
def test_delete_member(jwt_auth_header):
    logging.info(f"Deleting the member")
    stub(
        responses.DELETE,
        "https://api.nexmo.com/v0.1/conversations/xx-xx-xx-xx/members/xx-xx-xx-xx",
    )

    response = requests.delete("https://api.nexmo.com/v0.1/conversations/xx-xx-xx-xx/members/xx-xx-xx-xx", headers=jwt_auth_header)

    logging.info(f"Checking DELETE request response is 200")
    assert response.status_code == 200
    logging.info(f"Successfully deleted the member")


@responses.activate
def test_list_events(jwt_auth_header):
    logging.info(f"Listing the events")
    stub(
        responses.GET,
        "https://api.nexmo.com/v0.1/conversations/xx-xx-xx-xx/events",
        fixture_path="events/list_events.json",
    )

    response = requests.get("https://api.nexmo.com/v0.1/conversations/xx-xx-xx-xx/events", headers=jwt_auth_header)

    logging.info(f"Checking GET request response is 200")
    assert response.status_code == 200
    logging.info(f"Checking 'text' in response json")
    response_body = response.json()
    assert "text" in str(response_body)
    logging.info(f"Successfully completed listing of the events")


@responses.activate
def test_create_event(jwt_auth_header):
    logging.info(f"Creating the event")
    stub(
        responses.POST,
        "https://api.nexmo.com/v0.1/conversations/xx-xx-xx-xx/events",
        fixture_path="events/create_event.json",
    )

    params = {"type": "text","from": "MEM-63f61863-4a51-4f6b-86e1-46edebio0391"}
    response = requests.post("https://api.nexmo.com/v0.1/conversations/xx-xx-xx-xx/events", headers=jwt_auth_header, \
        data=json.dumps(params))

    logging.info(f"Checking POST request response is 201")
    assert response.status_code == 201
    logging.info(f"Checking 'id' in response json")
    response_body = response.json()
    assert response_body["id"] == "5"
    logging.info(f"Successfully created event")


@responses.activate
def test_retrieve_event(jwt_auth_header):
    logging.info(f"Retrieving the event")
    stub(
        responses.GET,
        "https://api.nexmo.com/v0.1/conversations/xx-xx-xx-xx/events/xx-xx-xx-xx",
        fixture_path="events/get_event.json",
    )

    response = requests.get("https://api.nexmo.com/v0.1/conversations/xx-xx-xx-xx/events/xx-xx-xx-xx", headers=jwt_auth_header)

    logging.info(f"Checking GET request response is 200")
    assert response.status_code == 200
    logging.info(f"Checking 'type' in response json")
    response_body = response.json()
    response_body["type"] == "text"
    logging.info(f"Successfully retrieved the event")


@responses.activate
def test_delete_event(jwt_auth_header):
    logging.info(f"Deleting the event")
    stub(
        responses.DELETE,
        "https://api.nexmo.com/v0.1/conversations/xx-xx-xx-xx/events/xx-xx-xx-xx",
    )

    response = requests.delete("https://api.nexmo.com/v0.1/conversations/xx-xx-xx-xx/events/xx-xx-xx-xx", headers=jwt_auth_header)

    logging.info(f"Checking DELETE request response is 200")
    assert response.status_code == 200
    logging.info(f"Successfully deleted the event")


@responses.activate
def test_list_legs(jwt_auth_header):
    logging.info(f"Listing the legs")
    stub(
        responses.GET,
        "https://api.nexmo.com/v0.1/legs",
        fixture_path="legs/list_legs.json",
    )

    response = requests.get("https://api.nexmo.com/v0.1/legs", headers=jwt_auth_header)

    logging.info(f"Checking GET request response is 200")
    assert response.status_code == 200
    logging.info(f"Checking leg uuid in response json")
    response_body = response.json()
    assert "a595959595959595995" in str(response_body)
    logging.info(f"Successfully completed the listing of the legs")


@responses.activate
def test_delete_leg(jwt_auth_header):
    logging.info(f"Deleting the leg")
    stub(
        responses.DELETE,
        "https://api.nexmo.com/v0.1/legs/xx-xx-xx-xx",
    )

    response = requests.delete("https://api.nexmo.com/v0.1/legs/xx-xx-xx-xx", headers=jwt_auth_header)

    logging.info(f"Checking DELETE request response is 200")
    assert response.status_code == 200
    logging.info(f"Successfully deleted the leg")