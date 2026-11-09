import { useEffect, useState } from "react";

const API_ROOT = `http://${window.location.hostname}:8000/api/`;

function getCookie(name) {
  const cookie = document.cookie
    .split("; ")
    .find((entry) => entry.startsWith(`${name}=`));
  return cookie ? decodeURIComponent(cookie.slice(name.length + 1)) : "";
}

function messageFromBody(body, fallback) {
  if (typeof body?.detail === "string") return body.detail;
  if (body && typeof body === "object") {
    const messages = Object.values(body)
      .flat(Infinity)
      .filter((message) => typeof message === "string");
    if (messages.length) return messages.join(" ");
  }
  return fallback;
}

async function apiRequest(path, { method = "GET", body } = {}) {
  const headers = {};
  const options = { method, credentials: "include", headers };
  if (body !== undefined) {
    headers["Content-Type"] = "application/json";
    options.body = JSON.stringify(body);
  }
  if (!["GET", "HEAD", "OPTIONS"].includes(method.toUpperCase())) {
    const csrfToken = getCookie("csrftoken");
    if (!csrfToken) throw new Error("Could not verify this request. Reload and try again.");
    headers["X-CSRFToken"] = csrfToken;
  }

  const response = await fetch(`${API_ROOT}${path}`, options);
  const responseText = await response.text();
  let responseBody = null;
  if (responseText) {
    try {
      responseBody = JSON.parse(responseText);
    } catch {
      responseBody = null;
    }
  }
  if (!response.ok) {
    throw new Error(messageFromBody(responseBody, "The request failed. Please try again."));
  }
  return responseBody;
}

function App() {
  const [user, setUser] = useState(null);
  const [tasks, setTasks] = useState([]);
  const [newTitle, setNewTitle] = useState("");
  const [editingTaskId, setEditingTaskId] = useState(null);
  const [editTitle, setEditTitle] = useState("");
  const [isLoading, setIsLoading] = useState(true);
  const [isSaving, setIsSaving] = useState(false);
  const [deletingTaskId, setDeletingTaskId] = useState(null);
  const [error, setError] = useState("");
  const [authMode, setAuthMode] = useState("login");
  const [authForm, setAuthForm] = useState({ username: "", password: "" });

  useEffect(() => {
    let isCurrent = true;

    async function initialize() {
      try {
        await apiRequest("auth/csrf/");
        const session = await apiRequest("auth/user/");
        if (session.username) {
          const userTasks = await apiRequest("tasks/");
          if (isCurrent) {
            setUser({ username: session.username });
            setTasks(userTasks);
          }
        }
      } catch {
        if (isCurrent) setError("Could not connect to the server. Check that it is running.");
      } finally {
        if (isCurrent) setIsLoading(false);
      }
    }

    initialize();
    return () => {
      isCurrent = false;
    };
  }, []);

  async function handleAuth(event) {
    event.preventDefault();
    setIsSaving(true);
    setError("");
    try {
      const endpoint = authMode === "register" ? "auth/register/" : "auth/login/";
      const session = await apiRequest(endpoint, { method: "POST", body: authForm });
      const userTasks = await apiRequest("tasks/");
      setUser({ username: session.username });
      setTasks(userTasks);
      setAuthForm({ username: "", password: "" });
    } catch (authError) {
      setError(authError.message);
    } finally {
      setIsSaving(false);
    }
  }

  async function handleLogout() {
    setError("");
    try {
      await apiRequest("auth/logout/", { method: "POST" });
      setUser(null);
      setTasks([]);
      setEditingTaskId(null);
    } catch (logoutError) {
      setError(logoutError.message);
    }
  }

  async function handleAddTask(event) {
    event.preventDefault();
    const title = newTitle.trim();
    if (!title) return;
    setIsSaving(true);
    setError("");
    try {
      const task = await apiRequest("tasks/", { method: "POST", body: { title } });
      setTasks((currentTasks) => [...currentTasks, task]);
      setNewTitle("");
    } catch (saveError) {
      setError(saveError.message);
    } finally {
      setIsSaving(false);
    }
  }

  function startEditing(task) {
    setEditingTaskId(task.id);
    setEditTitle(task.title);
    setError("");
  }

  async function handleEditTask(event, taskId) {
    event.preventDefault();
    const title = editTitle.trim();
    if (!title) return;
    setIsSaving(true);
    setError("");
    try {
      const updatedTask = await apiRequest(`tasks/${taskId}/`, {
        method: "PATCH",
        body: { title },
      });
      setTasks((currentTasks) =>
        currentTasks.map((task) => (task.id === taskId ? updatedTask : task)),
      );
      setEditingTaskId(null);
      setEditTitle("");
    } catch (saveError) {
      setError(saveError.message);
    } finally {
      setIsSaving(false);
    }
  }

  async function handleDeleteTask(taskId) {
    setDeletingTaskId(taskId);
    setError("");
    try {
      await apiRequest(`tasks/${taskId}/`, { method: "DELETE" });
      setTasks((currentTasks) => currentTasks.filter((task) => task.id !== taskId));
      if (editingTaskId === taskId) setEditingTaskId(null);
    } catch (deleteError) {
      setError(deleteError.message);
    } finally {
      setDeletingTaskId(null);
    }
  }

  return (
    <main className="app-shell">
      <section className="todo-panel" aria-labelledby="page-title">
        <header className="page-header">
          <span className="eyebrow">YOUR DAY, IN FOCUS</span>
          <h1 id="page-title">To-do list</h1>
          <p>A little progress adds up. What would you like to get done?</p>
        </header>

        {error && <p className="error-message" role="alert">{error}</p>}

        {isLoading ? (
          <p className="list-message">Checking your account...</p>
        ) : !user ? (
          <section aria-label={authMode === "login" ? "Log in" : "Create account"}>
            <form className="auth-form" onSubmit={handleAuth}>
              <h2>{authMode === "login" ? "Welcome back" : "Create your account"}</h2>
              <label htmlFor="username">Username</label>
              <input
                id="username"
                name="username"
                type="text"
                autoComplete="username"
                maxLength={150}
                value={authForm.username}
                onChange={(event) =>
                  setAuthForm((current) => ({ ...current, username: event.target.value }))
                }
                required
                disabled={isSaving}
              />
              <label htmlFor="password">Password</label>
              <input
                id="password"
                name="password"
                type="password"
                autoComplete={authMode === "login" ? "current-password" : "new-password"}
                value={authForm.password}
                onChange={(event) =>
                  setAuthForm((current) => ({ ...current, password: event.target.value }))
                }
                required
                disabled={isSaving}
              />
              <button type="submit" disabled={isSaving}>
                {isSaving
                  ? "Please wait..."
                  : authMode === "login"
                    ? "Log in"
                    : "Create account"}
              </button>
            </form>
            <p className="auth-switch">
              {authMode === "login" ? "New here?" : "Already have an account?"}{" "}
              <button
                type="button"
                onClick={() => {
                  setAuthMode(authMode === "login" ? "register" : "login");
                  setAuthForm({ username: "", password: "" });
                  setError("");
                }}
              >
                {authMode === "login" ? "Create an account" : "Log in"}
              </button>
            </p>
          </section>
        ) : (
          <>
            <div className="user-bar">
              <span>Signed in as <strong>{user.username}</strong></span>
              <button type="button" onClick={handleLogout}>Log out</button>
            </div>
            <form className="add-form" onSubmit={handleAddTask}>
              <label className="visually-hidden" htmlFor="new-task">New task</label>
              <input
                id="new-task"
                type="text"
                maxLength={50}
                placeholder="Add a task..."
                value={newTitle}
                onChange={(event) => setNewTitle(event.target.value)}
                disabled={isSaving}
              />
              <button type="submit" disabled={isSaving || !newTitle.trim()}>
                {isSaving ? "Saving..." : "Add task"}
              </button>
            </form>

            <div className="task-list" aria-live="polite">
              {tasks.length === 0 ? (
                <div className="empty-state">
                  <span className="empty-icon" aria-hidden="true">✦</span>
                  <h2>No tasks yet</h2>
                  <p>Add your first task above and get started.</p>
                </div>
              ) : (
                tasks.map((task) => (
                  <article className="task-card" key={task.id}>
                    {editingTaskId === task.id ? (
                      <form
                        className="edit-form"
                        onSubmit={(event) => handleEditTask(event, task.id)}
                      >
                        <label className="visually-hidden" htmlFor={`edit-task-${task.id}`}>
                          Edit task
                        </label>
                        <input
                          id={`edit-task-${task.id}`}
                          type="text"
                          maxLength={50}
                          value={editTitle}
                          onChange={(event) => setEditTitle(event.target.value)}
                          disabled={isSaving}
                          autoFocus
                        />
                        <div className="task-actions">
                          <button type="submit" disabled={isSaving || !editTitle.trim()}>
                            Save
                          </button>
                          <button
                            className="button-secondary"
                            type="button"
                            onClick={() => setEditingTaskId(null)}
                            disabled={isSaving}
                          >
                            Cancel
                          </button>
                        </div>
                      </form>
                    ) : (
                      <>
                        <div className="task-copy">
                          <h2>{task.title}</h2>
                          <span className={`task-status${task.completed ? " is-complete" : ""}`}>
                            <span className="status-dot" aria-hidden="true" />
                            {task.completed ? "Completed" : "In progress"}
                          </span>
                        </div>
                        <div className="task-actions">
                          <button
                            className="edit-button"
                            type="button"
                            onClick={() => startEditing(task)}
                            aria-label={`Edit ${task.title}`}
                            disabled={deletingTaskId !== null}
                          >
                            Edit
                          </button>
                          <button
                            className="delete-button"
                            type="button"
                            onClick={() => handleDeleteTask(task.id)}
                            aria-label={`Delete ${task.title}`}
                            disabled={deletingTaskId !== null}
                          >
                            {deletingTaskId === task.id ? "Deleting..." : "Delete"}
                          </button>
                        </div>
                      </>
                    )}
                  </article>
                ))
              )}
            </div>
            {tasks.length > 0 && (
              <footer className="list-footer">
                {tasks.length} {tasks.length === 1 ? "task" : "tasks"} on your list
              </footer>
            )}
          </>
        )}
      </section>
    </main>
  );
}

export default App;