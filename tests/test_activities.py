def test_get_activities_returns_all_seeded_activities(client):
    # Arrange
    expected_activity_count = 9

    # Act
    response = client.get("/activities")
    data = response.json()

    # Assert
    assert response.status_code == 200
    assert len(data) == expected_activity_count
    assert "Chess Club" in data
    assert "Robotics Club" in data


def test_get_activities_returns_expected_activity_schema(client):
    # Arrange
    required_keys = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get("/activities")
    data = response.json()

    # Assert
    assert response.status_code == 200
    chess_club = data["Chess Club"]
    assert required_keys.issubset(chess_club.keys())
    assert isinstance(chess_club["participants"], list)