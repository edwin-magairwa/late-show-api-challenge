# My Python Server

## Overview
This project is a Python-based server application designed to manage guests and episodes. It provides a RESTful API for interacting with guest and episode data, as well as user authentication.

## Project Structure
```
my-python-server
├── server
│   ├── app.py
│   ├── config.py
│   ├── seed.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── guest.py
│   │   ├── episode.py
│   │   ├── appearance.py
│   │   └── user.py
│   ├── controllers
│   │   ├── __init__.py
│   │   ├── guest_controller.py
│   │   ├── episode_controller.py
│   │   ├── appearance_controller.py
│   │   └── auth_controller.py
├── migrations
├── challenge-4-lateshow.postman_collection.json
└── README.md
```

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   cd my-python-server
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

5. Configure the application settings in `server/config.py`.

## Usage
To start the server, run:
```
python server/app.py
```

## API Endpoints
- **Guests**
  - `GET /guests`: Retrieve all guests
  - `POST /guests`: Create a new guest
  - `PUT /guests/{id}`: Update a guest
  - `DELETE /guests/{id}`: Delete a guest

- **Episodes**
  - `GET /episodes`: Retrieve all episodes
  - `POST /episodes`: Create a new episode
  - `PUT /episodes/{id}`: Update an episode
  - `DELETE /episodes/{id}`: Delete an episode

- **Authentication**
  - `POST /auth/login`: User login
  - `POST /auth/register`: User registration

## Database Migrations
Database migrations are managed in the `migrations` directory. Use the appropriate migration tool to apply changes to the database schema.

## Postman Collection
A Postman collection for testing the API endpoints is included in `challenge-4-lateshow.postman_collection.json`.

## License
This project is licensed under the MIT License. See the LICENSE file for details.