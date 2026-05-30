# 🧠 ForgeBlog CMS: Secure Flask-Based JSON Blog System

<p align="center">
  <b>A lightweight, secure, file-based blog CMS built using Flask and Python.</b><br>
  Designed for simplicity, clarity, and full manual control over data persistence without a database engine.
</p>

---

<h2>📘 Project Overview</h2>

<p>
<b>ForgeBlog CMS</b> is a custom-built Flask-based blog management system developed as part of a <b><a href="https://roadmap.sh/projects" target="_blank">roadmap.sh</a></b> project. It allows a single administrator to create, edit, update, and delete blog posts through a secure authentication system.
</p>

<p>
Unlike traditional database-driven CMS platforms, ForgeBlog stores all persistent data locally using structured JSON files inside the <code>instance/</code> directory. This keeps the project lightweight, transparent, and easy to inspect without requiring external database services.
</p>

<p>
The system is built around Flask sessions, Werkzeug password hashing, and a custom route protection decorator to ensure that only authenticated administrators can access restricted functionality.
</p>

---

<h2>⚙️ Key Features</h2>

<ul>
  <li>Secure admin authentication system using Flask sessions</li>
  <li>Password hashing using Werkzeug security utilities</li>
  <li>Full CRUD functionality for blog posts (Create, Read, Update, Delete)</li>
  <li>JSON-based file storage (no database dependency)</li>
  <li>Protected admin routes using a custom decorator</li>
  <li>Dynamic post rendering using Jinja2 templates</li>
  <li>Modular helper-based architecture for separation of concerns</li>
</ul>

---

<h2>📂 Folder Structure</h2>

<pre>
.
├── app.py
├── helpers/
│   ├── auth.py
│   └── posts.py
├── instance/
│   ├── admin.json
│   └── posts.json
├── static/
│   └── media/
├── templates/
│   ├── layout.html
│   ├── pages/
│   │   ├── home.html
│   │   ├── post.html
│   │   └── admin/
│   └── partials/
│       ├── header.html
│       └── footer.html
├── requirements.txt
├── .env
└── LICENSE
</pre>

---

<h2>🚀 How to Run the Project</h2>

<ol>
  <li>Ensure Python 3.8+ is installed.</li>
  <li>Clone the repository:
    <pre>git clone https://github.com/sheikh-h/forgeblog-cms.git</pre>
  </li>
  <li>Install dependencies:
    <pre>pip install -r requirements.txt</pre>
  </li>
  <li>Create and activate a virtual environment (recommended).</li>
  <li>Run the Flask application:
    <pre>python app.py</pre>
  </li>
  <li>Open your browser:
    <pre>http://127.0.0.1:5000</pre>
  </li>
</ol>

---

<h2>🔐 Authentication System (helpers/auth.py)</h2>

<h3>login_required(f)</h3>
<p>
A Flask decorator that protects routes by checking whether <code>admin_id</code> exists in the session. If not present, the user is redirected to the admin login page.
</p>

<p><b>Purpose:</b> Prevent unauthorised access to administrative functionality such as creating, editing, or deleting posts.</p>

---

<h3>login_function(username, password)</h3>
<p>
Handles admin authentication by loading credentials from <code>admin.json</code> and verifying password hashes using Werkzeug’s <code>check_password_hash()</code>.
</p>

<p><b>Returns:</b> True if credentials are valid, otherwise False.</p>

<p><b>Error Handling:</b> Safely handles missing files and invalid credentials without crashing the application.</p>

---

<h3>register_user(username, password)</h3>
<p>
Creates a new admin user and stores the credentials securely inside <code>admin.json</code>. Passwords are hashed before being written to disk.
</p>

---

<h2>📝 Blog Post System (helpers/posts.py)</h2>

<h3>load_posts()</h3>
<p>Loads all posts from <code>posts.json</code>. If the file does not exist, it is created and an empty list is returned.</p>

<h3>load_post(_id)</h3>
<p>Returns a single post matching the given ID or <code>None</code> if no match is found.</p>

<h3>add_new_post(title, description, content, time)</h3>
<p>Creates a new blog post, assigns an incremental ID, and stores it in JSON format.</p>

<h3>delete_post(id)</h3>
<p>Removes a post matching the given ID and updates the JSON file.</p>

<h3>update_post(id, title=None, description=None, content=None)</h3>
<p>Updates only the provided fields of a post while preserving existing values.</p>

---

<h2>🌐 Flask Application Logic (app.py)</h2>

<h3>home()</h3>
<p>Displays all blog posts on the homepage.</p>

<h3>view_post(_id)</h3>
<p>Displays a single blog post. Should ideally return a 404 if the post does not exist.</p>

<h3>admin()</h3>
<p>Handles admin login and session creation.</p>

<h3>logout()</h3>
<p>Clears the session and logs out the admin user.</p>

<h3>add_post()</h3>
<p>Creates a new blog post from form input and stores it via helper functions.</p>

<h3>delete_posts(_id)</h3>
<p>Deletes a blog post by ID and redirects to the dashboard.</p>

<h3>edit_posts(_id)</h3>
<p>Allows editing of an existing blog post.</p>

<h3>dashboard()</h3>
<p>Displays all posts in the admin control panel.</p>

---

<h2>🔐 Security Model</h2>

<ul>
  <li>Werkzeug password hashing for secure credential storage</li>
  <li>Flask session-based authentication</li>
  <li>Route protection via custom <code>login_required</code> decorator</li>
  <li>Admin-only access to all mutation routes</li>
</ul>

---

<h2>🧪 Error Handling Strategy</h2>

<ul>
  <li>Checks for missing JSON files and initialises them automatically</li>
  <li>Returns safe defaults instead of crashing (e.g. empty lists or None)</li>
  <li>Validates session state before accessing admin routes</li>
  <li>Uses controlled try/except blocks only where necessary</li>
</ul>

---

<h2>🧭 Planned Improvements</h2>

<p>
This project was built entirely independently without the use of AI-generated code or assistance.
</p>

<p>
Future improvements planned include:
</p>

<ul>
  <li>Migrating password hashing to <b>Argon2</b> for stronger modern cryptographic security</li>
  <li>Replacing manual form handling with <b>Flask-WTF</b> for validation and CSRF protection</li>
  <li>Adding full CSRF protection across all admin routes</li>
  <li>Improving input sanitisation and validation</li>
</ul>

---

<h2>📦 Environment Variables (.env)</h2>

<p>
The <code>.env</code> file is included in this project to store the Flask secret key required for session management. It is provided intentionally to make setup easier for anyone running the project locally, so users do not need to manually generate their own secret key before launching the application.
</p>

---

<h2>📄 License</h2>

<p>
This project is licensed under the MIT License.
</p>

<pre>
MIT Licence

Copyright (c) 2026 Sheikh Hussain

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

</pre>

---

## Footnote

<div align="center" style="border: 1px solid green; padding: 10px; border-radius: 5px;">
  <p>🗣️ Feel free to follow, connect, and chat!</p>
  <a class="header-badge" target="_blank" href="https://github.com/sheikh-h"><img src="https://img.shields.io/badge/GitHub-376e00?style=flat&logo=github&logoColor=white" alt="GitHub"></a>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/sheikh-hussain"><img src="https://img.shields.io/badge/LinkedIn-376e00?style=flat&logo=LinkedIn&logoColor=white" alt="LinkedIn"></a>
  <a class="header-badge" target="_blank" href="mailto:sheikh.hussain1155@gmail.com"><img src="https://img.shields.io/badge/Gmail-376e00?style=flat&logo=gmail&logoColor=white" alt="Gmail"></a>
  <a class="header-badge" target="_blank" href="https://.com"><img src="https://img.shields.io/badge/Portfolio-376e00?style=flat&logo=github&logoColor=white" alt="Portfolio"></a>
</div>

<div align="center">
  <a href="https://github.com/sheikh-h/" target="_blank">By Your Name 💚</a>  
</div>

---

<h2 align="center">⭐ If you like this project, please give it a star on GitHub!</h2>
