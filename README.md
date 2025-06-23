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

# Late Show API Challenge

## Setup Instructions

1. **Clone the repository**
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set environment variables:**
   - `DATABASE_URI` (e.g., postgresql://postgres:postgres@localhost/late_show_db)
   - `SECRET_KEY` and `JWT_SECRET_KEY`
4. **Run migrations:**
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```
5. **Seed the database:**
   ```bash
   python server/seed.py
   ```
6. **Run the app:**
   ```bash
   FLASK_APP=server/app.py flask run
   ```

## Auth Flow
- Register: `POST /register`
- Login: `POST /login` (returns JWT)
- Use JWT in `Authorization: Bearer <token>` for protected routes

## Routes
| Route                  | Method | Auth? | Description                       |
|------------------------|--------|-------|-----------------------------------|
| /register              | POST   | No    | Register a user                   |
| /login                 | POST   | No    | Log in, get JWT                   |
| /episodes              | GET    | No    | List episodes                     |
| /episodes/<id>         | GET    | No    | Get episode + appearances         |
| /episodes/<id>         | DELETE | Yes   | Delete episode + appearances      |
| /guests                | GET    | No    | List guests                       |
| /appearances           | POST   | Yes   | Create appearance                 |

## Postman
- Import `challenge-4-lateshow.postman_collection.json` for testing.

## GitHub
- [Your repository link here]
