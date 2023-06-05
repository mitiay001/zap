function addTask() {
    var input = document.getElementById("taskInput");
    var task = input.value;
  
    if (task === "") {
      alert("Пожалуйста, введите задачу!");
      return;
    }
  
    var taskList = document.getElementById("taskList");
    var li = document.createElement("li");
    li.appendChild(document.createTextNode(task));
    taskList.appendChild(li);
  
    input.value = "";
  }
  