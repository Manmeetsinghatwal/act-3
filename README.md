# Note-Taking Application API

## Overview
This program offers a RESTful API for a simple note-taking tool. You may interact with it via HTTP requests to add, retrieve, update, and remove notes. The API was written in Python, especially the 'http.server' module from the standard library. It also makes use of a MySQL database for persistent storage.

## Prerequisites
- Docker installed on your machine.
- Basic knowledge of Docker commands and operations.
- Git for version control.

## Setup and Installation
1. **Clone the Repository**
    ```bash
    git clone https://github.com/Manmeetsinghatwal/act-3
    cd directory-name
    ```

2. **Build and Run with Docker Compose**

    Use Docker Compose to build and run the application and database services:
    ```bash
    docker-compose up --build
    ```

    This command creates the API server image, and starts the services defined in docker-compose.yml.

3. **Stopping the Services**

    To stop the services and remove the containers, use the following command:
    ```bash
    docker-compose down
    ```

## API Endpoints

The API supports the following operations:

### GET /notes - Retrieve All Notes
- **Objective**: Retrieves all the notes.
- **Method**: GET
- **URL**: `http://localhost:8080/notes`
- **Body**: None
- **Instructions**: Set the request method to GET, enter the URL, and send the request.

### POST /notes - Create a New Note
- **Objective**: Creates a new note.
- **Method**: POST
- **URL**: `http://localhost:8080/notes`
- **Body**: (application/json)
    ```json
    {
      "title": "New topic",
      "content": "Content of the new topic."
    }
    ```
 – **Instructions**: **POST** – **URL** – **Body**: ‘raw’ – **Type**: JSON – **Send**:

### PUT /notes - Update an Existing Note
- **Objective**: Updates an existing topic by ID.
- **Method**: PUT
- **URL**: `http://localhost:8080/notes?id=1` (Replace `1` with the actual note ID)
- **Body**: (application/json)
    ```json
    {
      "title": "Updated topic",
      "content": "Updated content."
    }
    ```
- **Instructions**: Set the request method to PUT, paste the URL, select Body from the tabs, set to 'raw', set the Type to 'JSON', past the JSON to edit the topic, and submit the request.

### DELETE /notes - Delete a Note
- **Objective**: Deletes an existing topic by ID.
- **Method**: DELETE
- **URL**: `http://localhost:8080/notes?id=1` (Replace `1` with the actual note ID)
- **Body**: None
- **Instructions**: Set the request method to DELETE, enter the URL, and send the request.

## Testing

The API endpoints can be accessed using a graphical user interface (GUI) such as [Postman](https://www.postman.com/) masquerading as a browser client, or by 'curl' instructions similar to those shown above.


## Additional Information

- The MySQL database is initialized with a `notes` table, which has the columns `id`, `title`, and `content`.
- The API server runs on port `8080`, and the MySQL service is exposed on the default port `3306`.
- Ensure you have the `.env` file with necessary environment variables if you have sensitive or environment-specific configurations.

## Contributors

- Manmeet Singh Atwal (https://github.com/Manmeetsinghatwal/act-3)
