import { useEffect, useState } from "react";

const TASKS_URL = "http://127.0.0.1:8000/api/tasks/";

async function saveTask(url, method, title) {
  const response = await fetch(url, {
    method,
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title }),
  });

  if (!response.ok) {
    throw new Error("Could not save your task. Please try again.");
  }

  return response.json();
}

function App() {
  const [tasks, setTasks] = useState([]);
  const [newTitle, setNewTitle] = useState("");
  const [editingTaskId, setEditingTaskId] = useState(null);
  const [editTitle, setEditTitle] = useState("");
  const [isLoading, setIsLoading] = useState(true);
  const [isSaving, setIsSaving] = useState(false);
  const [deletingTaskId, setDeletingTaskId] = useState(null);
  const [error, setError] = useState("");

  useEffect(() => {
    let isCurrent = true;

    fetch(TASKS_URL)
      .then((response) => {
        if (!response.ok) {
          throw new Error("Could not load tasks. Please try again.");
        }
        return response.json();
      })
      .then((data) => {
        if (isCurrent) setTasks(data);
      })
      .catch(() => {
        if (isCurrent) setError("Could not load tasks. Check that the server is running.");
      })
      .finally(() => {
        if (isCurrent) setIsLoading(false);
      });

    return () => {
      isCurrent = false;
    };
  }, []);

  async function handleAddTask(event) {
    event.preventDefault();
    const title = newTitle.trim();
    if (!title) return;

    setIsSaving(true);
    setError("");
    try {
      const task = await saveTask(TASKS_URL, "POST", title);
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
      const updatedTask = await saveTask(`${TASKS_URL}${taskId}/`, "PATCH", title);
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
      const response = await fetch(`${TASKS_URL}${taskId}/`, { method: "DELETE" });
      if (!response.ok) {
        throw new Error("Could not delete your task. Please try again.");
      }
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

        <form className="add-form" onSubmit={handleAddTask}>
          <label className="visually-hidden" htmlFor="new-task">
            New task
          </label>
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

        {error && (
          <p className="error-message" role="alert">
            {error}
          </p>
        )}

        <div className="task-list" aria-live="polite">
          {isLoading ? (
            <p className="list-message">Loading your tasks...</p>
          ) : tasks.length === 0 ? (
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

        {!isLoading && tasks.length > 0 && (
          <footer className="list-footer">
            {tasks.length} {tasks.length === 1 ? "task" : "tasks"} on your list
          </footer>
        )}
      </section>
    </main>
  );
}

export default App;
