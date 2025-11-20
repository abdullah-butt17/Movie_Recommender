// Dark Mode Toggle
document.getElementById("darkToggle").addEventListener("change", function () {
    document.body.classList.toggle("dark-mode");
});

// Handle Movie Recommendation
document.getElementById("searchForm").addEventListener("submit", function (e) {
    e.preventDefault();

    let movieName = document.getElementById("movieInput").value;

    fetch("/recommend", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: "movie=" + encodeURIComponent(movieName)
    })
    .then(response => response.json())
    .then(data => {
        let list = document.getElementById("resultList");
        list.innerHTML = "";

        data.forEach(m => {
            let li = document.createElement("li");
            li.className = "list-group-item";
            li.textContent = m;
            list.appendChild(li);
        });
    });
});
