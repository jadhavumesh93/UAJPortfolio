window.onload = function(){
    setActive(document.getElementById("project1"), 1)
}

function setActive(element, project_id) {
    document.querySelectorAll(".header").forEach(h => {
        h.classList.remove("project_active_tab");
    });

    element.classList.add("project_active_tab");
    project_desc(project_id)
}

function project_desc(project_id = 1){
    //console.log(`project id = ${project_id}`)
    
    //console.log("Click project = ", project_id)
    fetch('/projectdesc', {
        method : 'POST',
        headers: {
                    'Content-Type': 'application/json',
                },
        body: JSON.stringify({'project_id': project_id})
        //body : {'project_id' : project_id}
    })
    .then(response => response.json())
    .then(data => {
        //console.log("Data = ", data)
        document.getElementById("project_video").src = data.video_url
        document.getElementById("tech_stack").textContent = data.tech_stack
        document.getElementById("tech_stack").style.fontStyle = "italic"
        document.getElementById("project_url").href = data.project_url
        if(project_id == 3){
            document.getElementById("project_url").textContent = "Complete Analysis here"
        }
        const ul = document.getElementById("project_desc")
        ul.innerHTML = "";
        data.desc.forEach(element => {
            const li = document.createElement("li");
            li.textContent = element;
            ul.appendChild(li);
        });
    })
    .catch((error) => {
        console.log("Error = ", error)
    })
}

function ViewScroll(view){
    const section = document.getElementById(view)
    section.scrollIntoView({
        behavior : "smooth",
        block : "center"
    })
}