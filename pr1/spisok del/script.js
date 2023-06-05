var tasks = [];

function addTask() {
  var input = document.getElementById("taskInput");
  var task = input.value;

  if (task === "") {
    alert("Пожалуйста, введите задачу!");
    return;
  }

  tasks.push({ title: task, completed: false });
  input.value = "";
  saveTasks();
  renderTasks();
}

function deleteTask(index) {
  tasks.splice(index, 1);
  saveTasks();
  renderTasks();
}

function toggleTask(index) {
  tasks[index].completed = !tasks[index].completed;
  saveTasks();
  renderTasks();
}

function editTask(index) {
  var newTitle = prompt("Введите новый текст задачи:", tasks[index].title);

  if (newTitle === null) {
    return; // Нажата отмена, ничего не меняем
  }

  tasks[index].title = newTitle;
  saveTasks();
  renderTasks();
}

function filterTasks() {
  var filterSelect = document.getElementById("filterSelect");
  var selectedValue = filterSelect.value;

  var filteredTasks = [];

  switch (selectedValue) {
    case "completed":
      filteredTasks = tasks.filter(function(task) {
        return task.completed;
      });
      break;
    case "active":
      filteredTasks = tasks.filter(function(task) {
        return !task.completed;
      });
      break;
    default:
      filteredTasks = tasks;
  }

  renderTasks(filteredTasks);
}

function saveTasks() {
  localStorage.setItem("tasks", JSON.stringify(tasks));
}

function loadTasks() {
  var savedTasks = localStorage.getItem("tasks");

  if (savedTasks) {
    tasks = JSON.parse(savedTasks);
  }
}

function renderTasks(tasksToRender) {
  var taskList = document.getElementById("taskList");
  taskList.innerHTML = "";

  var tasksToDisplay = tasksToRender || tasks;

  for (var i = 0; i < tasksToDisplay.length; i++) {
    var task = tasksToDisplay[i];
    var li = document.createElement("li");

    if (task.completed) {
      li.classList.add("completed");
    }

    li.appendChild(document.createTextNode(task.title));

    var deleteButton = document.createElement("button");
    deleteButton.appendChild(document.createTextNode("Удалить"));
    deleteButton.onclick = deleteTask.bind(null, i);
    li.appendChild(deleteButton);

    var editButton = document.createElement("button");
    editButton.appendChild(document.createTextNode("Редактировать"));
    editButton.onclick = editTask.bind(null, i);
    li.appendChild(editButton);

    var toggleButton = document.createElement("button");
    toggleButton.appendChild(document.createTextNode("Выполнено"));
    toggleButton.onclick = toggleTask.bind(null, i);
    li.appendChild(toggleButton);

    taskList.appendChild(li);
  }
}

// Загрузка списка задач при загрузке страницы
window.onload = function() {
  loadTasks();
  renderTasks();
};
