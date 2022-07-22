Feature: Artist

    Scenario: Searching for an existing artist. GET:/artist/search
        Given I send a "get" request to "artist/search?name=Kendrick%20Lamar"
        Then the response code should be "200"
        And the response "artist_name" key should be "Kendrick Lamar"
        And the "hits" key in the response should have an array with length "10"

    Scenario: Searching for a non existing artist. GET:/artist/search
        Given I send a "get" request to "artist/search?name=thisdoesntexist"
        Then the response code should be "200"
        And the response "artist_name" key should be "thisdoesntexist"
        And the "hits" key in the response should have an array with length "0"
