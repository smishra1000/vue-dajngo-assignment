# API Details

## Participant List

Method: GET

url: http://127.0.0.1:8000/api/

example output

`[
    {
        "id": 1,

        "email": "testuser1@test.com",

        "first_name": "Tesr",

        "last_name": "User",

        "foundation_date": "2018-10-09T04:31:35Z",

        "participant_type": 1,

        "ranking": 62

    },
    {
        "id": 2,

        "email": "testuser2@gmail.com",

        "first_name": "test2",

        "last_name": "user2",

        "foundation_date": "2018-10-09T04:31:35Z",

        "participant_type": 1,

        "ranking": 10

    },
    {
        "id": 3,
        "email": "testuser3@tets.com",
        "first_name": "test3",
        "last_name": "user3",
        "foundation_date": "2018-10-09T04:31:35Z",
        "participant_type": 1,
        "ranking": 645
    }
]`

## Participant Details

Method: GET

url: http://127.0.0.1:8000/api/3/

example output

`{
    "id": 3,

    "email": "testuser3@test.com",

    "first_name": "test3",

    "last_name": "user3",

    "foundation_date": "2018-10-09T04:31:35Z",

    "participant_type": 1,

    "ranking": 645

}`

## Adding new Participant
Method: POST

url: http://127.0.0.1:8000/api/

example output

`{

    "email": "testuser2@test.com",

    "first_name": "test2",

    "last_name": "user2",

    "foundation_date": "2018-10-09T04:31:35Z",

    "participant_type": 1,

    "ranking": 656

}`


## Editing any Participatnt Details

Method: GET

url: http://127.0.0.1:8000/api/3/

example output

`{
    "id": 3,

    "email": "testuser1@test.com",

    "first_name": "Test",

    "last_name": "Test",

    "foundation_date": "2018-10-09T04:31:35Z",

    "participant_type": 1,

    "ranking": 600

}`