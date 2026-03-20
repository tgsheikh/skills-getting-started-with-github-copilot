def test_get_activities_returns_activity_data(client):
    response = client.get("/activities")

    assert response.status_code == 200
    payload = response.json()
    assert "Chess Club" in payload
    assert "participants" in payload["Chess Club"]


def test_get_activities_sets_no_store_cache_header(client):
    response = client.get("/activities")

    assert response.status_code == 200
    assert response.headers["cache-control"] == "no-store"
