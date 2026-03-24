def test_unregister_removes_existing_participant(client):
    # Arrange
    activity_name = "Chess Club"
    existing_email = "michael@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity_name}/unregister", params={"email": existing_email})
    activities_response = client.get("/activities")
    activities = activities_response.json()

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Unregistered {existing_email} from {activity_name}"
    assert existing_email not in activities[activity_name]["participants"]


def test_unregister_rejects_missing_participant(client):
    # Arrange
    activity_name = "Chess Club"
    missing_email = "notfound@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity_name}/unregister", params={"email": missing_email})

    # Assert
    assert response.status_code == 400
    assert response.json()["detail"] == "Participant not found in this activity"


def test_unregister_rejects_unknown_activity(client):
    # Arrange
    missing_activity_name = "Unknown Club"
    email = "student@mergington.edu"

    # Act
    response = client.post(f"/activities/{missing_activity_name}/unregister", params={"email": email})

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"