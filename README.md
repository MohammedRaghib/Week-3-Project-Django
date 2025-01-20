[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=17735939&assignment_repo_type=AssignmentRepo)

# Social_Media_App_Project

## Features:

<ol>
 	<li>User Registration and Authentication:
<ul>
 	<li>Users can create new accounts and log in to the application.</li>
 	<li>Passwords are securely stored using hashing techniques.</li>
 	<li>User authentication ensures that only authorized users can access protected features.</li>
</ul>
</li>
 	<li>User Profiles:
<ul>
 	<li>Each user has a profile that displays their information and activities.</li>
 	<li>Users can upload a profile picture and update their personal details.</li>
 	<li>The profile page shows the user's posts, followers, and following information.</li>
</ul>
</li>
 	<li>News Feed:
<ul>
 	<li>Users can view a personalized news feed that displays posts from users they follow.</li>
 	<li>The feed is dynamically updated to show the latest posts from followed users.</li>
 	<li>Users can like, comment on, and share posts directly from the feed.</li>
</ul>
</li>
 	<li>Creating and Editing Posts:
<ul>
 	<li>Users can create new posts with text, images, or videos.</li>
 	<li>They can edit or delete their own posts.</li>
 	<li>The posts can be tagged with relevant hashtags for easy discovery.</li>
</ul>
</li>
 	<li>Commenting and Interactions:
<ul>
 	<li>Users can comment on posts and engage in discussions.</li>
 	<li>They can like or dislike posts and comments to express their opinion.</li>
 	<li>Notifications are sent to users when someone interacts with their posts or comments.</li>
</ul>
</li>
 	<li>User Search and Discovery:
<ul>
 	<li>Users can search for other users based on their usernames or profile information.</li>
 	<li>They can follow or unfollow other users to customize their news feed.</li>
 	<li>Trending posts, popular users, or recommended profiles can be featured for user discovery.</li>
</ul>
</li>
</ol>

## Technical Requirements

<ol>
 	<li>Django Framework:
<ul>
 	<li>The latest version of Django should be installed and configured.</li>
 	<li>Use Django's project structure to organize the application components.</li>
</ul>
</li>
 	<li>Python:
<ul>
 	<li>Ensure that a compatible version of Python is installed on the development environment.</li>
 	<li>Use virtual environments to isolate project dependencies.</li>
</ul>
</li>
 	<li>Database:
<ul>
 	<li>Choose a suitable database backend such as PostgreSQL, MySQL, or SQLite.</li>
 	<li>Configure the Django settings to connect to the chosen database.</li>
 	<li>Design and create database models using Django's ORM.</li>
</ul>
</li>
  <li>Create the following endpoints using the Django REST Framework:
<ol>
 	<li>Profile Endpoints:
<ul>
 	<li><code>GET /api/profiles/{user_id}/</code>: Retrieve the profile of a specific user.</li>
 	<li><code>PUT /api/profiles/{user_id}/</code>: Update the profile of a specific user.</li>
</ul>
</li>
 	<li>Post Endpoints:
<ul>
 	<li><code>GET /api/posts/</code>: Retrieve a list of all posts.</li>
 	<li><code>GET /api/posts/{post_id}/</code>: Retrieve details of a specific post.</li>
 	<li><code>POST /api/posts/</code>: Create a new post.</li>
 	<li><code>PUT /api/posts/{post_id}/</code>: Update a specific post.</li>
 	<li><code>DELETE /api/posts/{post_id}/</code>: Delete a specific post.</li>
</ul>
</li>
 	<li>Comment Endpoints:
<ul>
 	<li><code>GET /api/posts/{post_id}/comments/</code>: Retrieve all comments for a specific post.</li>
 	<li><code>POST /api/posts/{post_id}/comments/</code>: Add a new comment to a specific post.</li>
 	<li><code>PUT /api/comments/{comment_id}/</code>: Update a specific comment.</li>
 	<li><code>DELETE /api/comments/{comment_id}/</code>: Delete a specific comment.</li>
</ul>
</li>
 	<li>Like Endpoints:
<ul>
 	<li><code>POST /api/posts/{post_id}/like/</code>: Like a specific post.</li>
 	<li><code>POST /api/comments/{comment_id}/like/</code>: Like a specific comment.</li>
 	<li><code>DELETE /api/posts/{post_id}/like/</code>: Remove a like from a specific post.</li>
 	<li><code>DELETE /api/comments/{comment_id}/like/</code>: Remove a like from a specific comment.</li>
</ul>
</li>
 	<li>Follow Endpoints:
<ul>
 	<li><code>POST /api/users/{user_id}/follow/</code>: Follow a specific user.</li>
 	<li><code>DELETE /api/users/{user_id}/follow/</code>: Unfollow a specific user.</li>
</ul>
</li>
 	<li>Search Endpoints:
<ul>
 	<li><code>GET /api/search/users/?query={search_query}</code>: Search for users based on a search query.</li>
</ul>
</li>
 	
</ol>
</ol>
