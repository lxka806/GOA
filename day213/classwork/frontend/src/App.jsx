
import { useEffect, useState } from "react";

function App() {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/tasks/")
      .then((response) => response.json())
      .then((data) => setTasks(data))
      .catch((error) => console.error(error));
  }, []);

  if(tasks.length === 0){
    return <h1>No Taskts yet</h1>
  }

  return (
    <div>
      <h1>To-Do List</h1>

      {tasks.map((task) => (
        <div key={task.id}>
          <h3>{task.title}</h3>
          <p>
            Status: {task.completed ? "Completed" : "Not completed"}
          </p>
        </div>
      ))}
    </div>
  );
}

export default App;
