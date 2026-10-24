
import api from "./api/axios";
import { useState, useEffect } from "react";

function App() {
  const [tasks, setTasks] = useState([]);
  const [task, setTask] = useState("");

  const getTasks = async () => {
    try {
      const response = await api.get("tasks/");
      setTasks(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  const handleChange = (e) => {
    setTask(e.target.value);
  };

  useEffect(() => {
    getTasks();
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!task.trim()) return;

    try {
      await api.post("tasks/", {
        title: task,
      });

      setTask("");
      await getTasks();
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="min-h-screen bg-slate-950 px-4 py-12 text-white">
      <div className="mx-auto max-w-2xl">
        <header className="mb-10 text-center">
          <p className="mb-3 text-sm font-semibold uppercase tracking-[0.3em] text-indigo-400">
            Stay organized
          </p>
          <h1 className="text-4xl font-extrabold tracking-tight sm:text-5xl">
            My Tasks<span className="text-indigo-500">.</span>
          </h1>
          <p className="mt-3 text-slate-400">
            Keep track of everything you need to get done.
          </p>
        </header>

        <form
          onSubmit={handleSubmit}
          className="mb-8 flex flex-col gap-3 rounded-2xl border border-slate-800 bg-slate-900 p-4 shadow-xl shadow-black/20 sm:flex-row"
        >
          <input
            type="text"
            name="task"
            value={task}
            onChange={handleChange}
            placeholder="What needs to get done?"
            className="min-w-0 flex-1 rounded-xl border border-slate-700 bg-slate-950 px-4 py-3 text-white outline-none transition placeholder:text-slate-500 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-500/20"
          />
          <button
            type="submit"
            className="rounded-xl bg-indigo-600 px-6 py-3 font-semibold text-white transition hover:bg-indigo-500 active:scale-95"
          >
            + Add Task
          </button>
        </form>

        <div className="mb-4 flex items-center justify-between">
          <h2 className="text-lg font-bold text-slate-200">
            Your tasks
          </h2>
          <span className="rounded-full border border-slate-700 bg-slate-900 px-3 py-1 text-sm text-slate-400">
            {tasks.length} {tasks.length === 1 ? "task" : "tasks"}
          </span>
        </div>

        <div className="space-y-3">
          {tasks.length === 0 ? (
            <div className="rounded-2xl border border-dashed border-slate-700 bg-slate-900/50 px-6 py-12 text-center">
              <p className="text-lg font-semibold text-slate-300">
                No tasks yet
              </p>
              <p className="mt-2 text-sm text-slate-500">
                Add your first task using the form above.
              </p>
            </div>
          ) : (
            tasks.map((task) => (
              <div
                key={task.id}
                className="group flex items-center gap-4 rounded-2xl border border-slate-800 bg-slate-900 p-5 transition duration-200 hover:border-indigo-500/50 hover:bg-slate-800/80"
              >
                <div className="flex h-10 w-10 shrink-0 items-center justify-center rounded-xl bg-indigo-500/10 font-bold text-indigo-400 transition group-hover:bg-indigo-500/20">
                  {task.id}
                </div>
                <h3 className="min-w-0 flex-1 break-words text-base font-medium text-slate-200">
                  {task.title}
                </h3>
                <span className="h-2 w-2 shrink-0 rounded-full bg-emerald-400"></span>
              </div>
            ))
          )}
        </div>

        <footer className="mt-10 text-center text-xs text-slate-600">
          Built with React, Tailwind CSS & Django REST Framework
        </footer>
      </div>
    </div>
  );
}

export default App;
