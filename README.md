# Authentication System - Homework 2

## Implementation Details

### Basic Requirements Implemented

1. **Server Setup**:
   - Listens on `localhost:5000`
   - Basic Express.js server with session management

2. **Authentication Flow**:
   - Login form at root URL (`/`)
   - Profile page (`/profile`) accessible only after authentication
   - Session-based authentication
   - Password hashing with bcrypt

3. **Database Integration**:
   - User credentials stored in MongoDB (or Redis)
   - Basic user schema with username and password

### How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/itmo-wad/username-hw2.git
   cd username-hw2
