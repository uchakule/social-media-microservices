# social-media-microservices
Social Media Microservices using Flask and python


1. User Service
Responsible for managing user accounts, including registration, login, and profile management.

Endpoints:
/register: Register a new user.
/login: Log in an existing user.
2. Post Service
Manages posts, including creating, editing, and deleting posts.

Endpoints:
/create_post: Create a new post.
/get_posts: Retrieve all posts.
3. Social Graph Service
Tracks user relationships, such as who follows whom.

Endpoints:
/follow: Follow another user.
/get_followers: Retrieve followers for a user.


4. Verify that the services are running:

User Service: http://localhost:5001
Post Service: http://localhost:5002
Social Graph Service: http://localhost:5003
